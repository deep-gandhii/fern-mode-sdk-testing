from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .rag_chunk_metadata import RagChunkMetadata
from .embedding_model_enum import EmbeddingModelEnum


class RagRetrievalInfo(BaseModel):
    """RagRetrievalInfo

    :param chunks: chunks
    :type chunks: List[RagChunkMetadata]
    :param embedding_model: embedding_model
    :type embedding_model: EmbeddingModelEnum
    :param retrieval_query: retrieval_query
    :type retrieval_query: str
    :param rag_latency_secs: rag_latency_secs
    :type rag_latency_secs: float
    :param used_chunk_ids: used_chunk_ids, defaults to None
    :type used_chunk_ids: List[str], optional
    """

    chunks: List[RagChunkMetadata]
    embedding_model: EmbeddingModelEnum
    retrieval_query: str
    rag_latency_secs: float
    used_chunk_ids: Optional[List[str]] = Field(default=None)
