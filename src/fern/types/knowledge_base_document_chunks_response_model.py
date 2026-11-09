from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .knowledge_base_document_chunk_response_model import (
    KnowledgeBaseDocumentChunkResponseModel,
)


class KnowledgeBaseDocumentChunksResponseModel(BaseModel):
    """KnowledgeBaseDocumentChunksResponseModel

    :param chunks: chunks
    :type chunks: List[KnowledgeBaseDocumentChunkResponseModel]
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    """

    chunks: List[KnowledgeBaseDocumentChunkResponseModel]
    next_cursor: Optional[str] = Field(default=None)
