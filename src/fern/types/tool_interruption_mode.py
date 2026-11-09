from __future__ import annotations
import typing
from typing import Any

ToolInterruptionMode = typing.Union[
    typing.Literal["allow", "disable_during_tool", "disable_during_tool_and_turn"],
    typing.Any,
]
