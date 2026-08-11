#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Canonical category/channel ordering shared by generators and validators."""
from __future__ import annotations

from collections import defaultdict
from typing import Protocol, TypeVar

from channel_identity import canonical_channel_key
from channel_utils import cctv_sort_key
from playlist_config import load_rules


class OrderedRow(Protocol):
    group: str
    name: str


RowT = TypeVar("RowT", bound=OrderedRow)


def _channel_sort_key(group: str, name: str, identity: str, groups: list[str]) -> tuple:
    group_index = groups.index(group)
    if group_index == 0:
        return group_index, cctv_sort_key(name), name, identity
    if group_index == 1:
        priorities = [str(item) for item in load_rules().get("satellite_priority", [])]
        priority_index = priorities.index(name) if name in priorities else len(priorities)
        return group_index, priority_index, name, identity
    return group_index, name, identity


def canonicalize_channel_rows(groups: list[str], rows: list[RowT]) -> list[RowT]:
    """Sort channel identities canonically while preserving each line's priority."""
    expected = set(groups)
    unexpected = sorted({row.group for row in rows} - expected)
    if unexpected:
        raise ValueError(f"playlist rows contain unknown categories: {unexpected!r}")

    grouped: dict[str, dict[str, list[RowT]]] = defaultdict(dict)
    for row in rows:
        identity = canonical_channel_key(row.name) or row.name
        grouped[row.group].setdefault(identity, []).append(row)

    ordered: list[RowT] = []
    for group in groups:
        identities = grouped.get(group, {})
        for identity, identity_rows in sorted(
            identities.items(),
            key=lambda item: _channel_sort_key(group, item[1][0].name, item[0], groups),
        ):
            ordered.extend(identity_rows)
    return ordered
