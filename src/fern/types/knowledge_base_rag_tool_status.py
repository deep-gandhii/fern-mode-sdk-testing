from __future__ import annotations
import typing
from typing import Any

KnowledgeBaseRagToolStatus = typing.Union[
    typing.Literal["success", "no_documents", "no_results"], typing.Any
]
