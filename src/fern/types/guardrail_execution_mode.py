from __future__ import annotations
import typing
from typing import Any

GuardrailExecutionMode = typing.Union[
    typing.Literal["streaming", "blocking"], typing.Any
]
