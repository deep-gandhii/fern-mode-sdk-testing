from __future__ import annotations
import typing
from typing import Any

LlmReasoningEffort = typing.Union[
    typing.Literal["none", "minimal", "low", "medium", "high", "xhigh", "max"],
    typing.Any,
]
