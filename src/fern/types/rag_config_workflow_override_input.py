from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .embedding_model_enum import EmbeddingModelEnum


class RagConfigWorkflowOverrideInput(BaseModel):
    """RagConfigWorkflowOverrideInput

    :param enabled: enabled, defaults to None
    :type enabled: bool, optional
    :param embedding_model: embedding_model, defaults to None
    :type embedding_model: EmbeddingModelEnum, optional
    :param max_vector_distance: Maximum vector distance of retrieved chunks., defaults to None
    :type max_vector_distance: float, optional
    :param max_documents_length: Maximum total length of document chunks retrieved from RAG., defaults to None
    :type max_documents_length: int, optional
    :param max_retrieved_rag_chunks_count: Maximum number of RAG document chunks to initially retrieve from the vector store. These are then further filtered by vector distance and total length., defaults to None
    :type max_retrieved_rag_chunks_count: int, optional
    :param num_candidates: Number of candidates evaluated in ANN vector search. Higher number means better results, but higher latency. Minimum recommended value is 100. If disabled, the default value is used., defaults to None
    :type num_candidates: int, optional
    :param query_rewrite_prompt_override: Custom prompt for rewriting user queries before RAG retrieval. The conversation history will be automatically appended at the end. If not set, the default prompt will be used., defaults to None
    :type query_rewrite_prompt_override: str, optional
    """

    enabled: Optional[bool] = Field(default=None)
    embedding_model: Optional[EmbeddingModelEnum] = Field(default=None)
    max_vector_distance: Optional[float] = Field(
        default=None, description="Maximum vector distance of retrieved chunks."
    )
    max_documents_length: Optional[int] = Field(
        default=None,
        description="Maximum total length of document chunks retrieved from RAG.",
    )
    max_retrieved_rag_chunks_count: Optional[int] = Field(
        default=None,
        description="Maximum number of RAG document chunks to initially retrieve from the vector store. These are then further filtered by vector distance and total length.",
    )
    num_candidates: Optional[int] = Field(
        default=None,
        description="Number of candidates evaluated in ANN vector search. Higher number means better results, but higher latency. Minimum recommended value is 100. If disabled, the default value is used.",
    )
    query_rewrite_prompt_override: Optional[str] = Field(
        default=None,
        description="Custom prompt for rewriting user queries before RAG retrieval. The conversation history will be automatically appended at the end. If not set, the default prompt will be used.",
    )
