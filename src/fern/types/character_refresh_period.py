from __future__ import annotations
import typing
from typing import Any

CharacterRefreshPeriod = typing.Union[
    typing.Literal[
        "monthly_period", "3_month_period", "6_month_period", "annual_period"
    ],
    typing.Any,
]
