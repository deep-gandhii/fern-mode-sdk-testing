from __future__ import annotations
import typing
from typing import Any

GetSharedSort = typing.Union[
    typing.Literal[
        "created_date", "usage_character_count_1y", "trending", "cloned_by_count"
    ],
    typing.Any,
]
