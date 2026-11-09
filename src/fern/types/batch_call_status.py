from __future__ import annotations
import typing
from typing import Any

BatchCallStatus = typing.Union[
    typing.Literal["pending", "in_progress", "completed", "failed", "cancelled"],
    typing.Any,
]
