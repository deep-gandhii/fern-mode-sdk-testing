from __future__ import annotations
import typing
from typing import Any

RagIndexStatus = typing.Union[
    typing.Literal[
        "new",
        "created",
        "processing",
        "failed",
        "succeeded",
        "rag_limit_exceeded",
        "document_too_small",
        "cannot_index_folder",
    ],
    typing.Any,
]
