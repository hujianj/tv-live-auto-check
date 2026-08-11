#!/usr/bin/env python3
"""Cross-process exit-code contract for the maintenance pipeline."""

# A guard policy rejection is recoverable through one confirmation pass. Any
# other non-zero guard exit is a deterministic program/configuration failure.
GUARD_REJECTED_EXIT_CODE = 3
