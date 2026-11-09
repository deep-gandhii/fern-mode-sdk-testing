from __future__ import annotations
import typing
from typing import Any

SearchStrategy = typing.Union[
    typing.Literal["cat", "keyword", "semantic", "ls"], typing.Any
]
