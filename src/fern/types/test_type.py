from __future__ import annotations
import typing
from typing import Any

TestType = typing.Union[
    typing.Literal["llm", "tool", "simulation", "folder"], typing.Any
]
