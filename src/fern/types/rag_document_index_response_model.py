from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .embedding_model_enum import EmbeddingModelEnum
from .rag_index_status import RagIndexStatus
from .rag_document_index_usage import RagDocumentIndexUsage


class RagDocumentIndexResponseModel(BaseModel):
    """RagDocumentIndexResponseModel

    :param id: id
    :type id: str
    :param model: model
    :type model: EmbeddingModelEnum
    :param status: status
    :type status: RagIndexStatus
    :param progress_percentage: progress_percentage
    :type progress_percentage: float
    :param document_model_index_usage: document_model_index_usage
    :type document_model_index_usage: RagDocumentIndexUsage
    """

    id: str
    model: EmbeddingModelEnum
    status: RagIndexStatus
    progress_percentage: float
    document_model_index_usage: RagDocumentIndexUsage
