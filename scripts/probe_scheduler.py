"""Bounded media-probe admission: queued URLs do not spend their probe budget."""
from collections import deque
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from urllib.parse import urlsplit

from url_utils import redact_text
from verify_sources import CheckResult


def iter_probe_results(jobs, checker, *, workers, per_host):
    """Yield (candidate, result), checking every job once with fair host queues.

    A job is (Candidate, keyword arguments). Only admitted jobs enter the
    executor; the HTTP semaphore still protects redirected/child resources.
    Ports and schemes share one host quota to avoid multiplying server load.
    """
    workers, per_host = max(1, int(workers)), max(1, int(per_host))
    buckets = {}
    for cand, kwargs in jobs:
        host = (urlsplit(cand.url).hostname or "unknown").lower()
        buckets.setdefault(host, deque()).append((cand, kwargs))
    ready = deque(buckets)
    ready_set = set(ready)
    active = dict.fromkeys(buckets, 0)
    pending = {}

    def mark_ready(host):
        if buckets[host] and active[host] < per_host and host not in ready_set:
            ready.append(host)
            ready_set.add(host)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        while ready or pending:
            while ready and len(pending) < workers:
                host = ready.popleft()
                ready_set.remove(host)
                if active[host] >= per_host or not buckets[host]:
                    continue
                cand, kwargs = buckets[host].popleft()
                pending[executor.submit(checker, cand, **kwargs)] = (cand, host)
                active[host] += 1
                mark_ready(host)
            if not pending:
                break
            done, _ = wait(pending, return_when=FIRST_COMPLETED)
            for future in done:
                cand, host = pending.pop(future)
                active[host] -= 1
                mark_ready(host)
                try:
                    result = future.result()
                except Exception as exc:
                    # One unexpected probe failure must not lose other results.
                    result = CheckResult(cand, False, "probe exception: " + redact_text(repr(exc))[:240])
                yield cand, result
