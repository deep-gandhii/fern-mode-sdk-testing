from __future__ import annotations
import typing
from typing import Any

KnowledgeBaseDocumentType = typing.Union[
    typing.Literal["file", "url", "text", "folder"], typing.Any
]
