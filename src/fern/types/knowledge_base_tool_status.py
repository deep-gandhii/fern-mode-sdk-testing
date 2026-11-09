from __future__ import annotations
import typing
from typing import Any

KnowledgeBaseToolStatus = typing.Union[
    typing.Literal["success", "no_matching_documents", "no_results"], typing.Any
]
