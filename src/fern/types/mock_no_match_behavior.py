from __future__ import annotations
import typing
from typing import Any

MockNoMatchBehavior = typing.Union[
    typing.Literal["call_real_tool", "raise_error"], typing.Any
]
