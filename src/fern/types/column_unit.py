from __future__ import annotations
import typing
from typing import Any

ColumnUnit = typing.Union[
    typing.Literal[
        "ms",
        "s",
        "min",
        "duration",
        "credits",
        "usd",
        "eur",
        "inr",
        "pln",
        "ratio",
        "rating",
    ],
    typing.Any,
]
