from __future__ import annotations
import typing
from typing import Any

InteractionBudget = typing.Union[
    typing.Literal["realtime", "5_minutes", "10_minutes", "1_hour"], typing.Any
]
