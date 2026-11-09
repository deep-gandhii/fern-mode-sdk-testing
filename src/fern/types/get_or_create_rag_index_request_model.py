from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .embedding_model_enum import EmbeddingModelEnum


class GetOrCreateRagIndexRequestModel(BaseModel):
    """GetOrCreateRagIndexRequestModel

    :param document_id: ID of the knowledgebase document for which to retrieve the index
    :type document_id: str
    :param create_if_missing: Whether to create the RAG index if it does not exist
    :type create_if_missing: bool
    :param model: model
    :type model: EmbeddingModelEnum
    """

    document_id: str = Field(
        description="ID of the knowledgebase document for which to retrieve the index"
    )
    create_if_missing: bool = Field(
        description="Whether to create the RAG index if it does not exist"
    )
    model: EmbeddingModelEnum
