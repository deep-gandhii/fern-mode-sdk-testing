from __future__ import annotations
import typing
from typing import Any

UsageAggregationInterval = typing.Union[
    typing.Literal["hour", "day", "week", "month", "cumulative"], typing.Any
]
