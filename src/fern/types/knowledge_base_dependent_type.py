from __future__ import annotations
import typing
from typing import Any

KnowledgeBaseDependentType = typing.Union[
    typing.Literal["direct", "transitive", "all"], typing.Any
]
