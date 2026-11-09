from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .get_or_create_rag_index_request_model import GetOrCreateRagIndexRequestModel


class BodyComputeRagIndexesInBatchV1ConvaiKnowledgeBaseRagIndexPost(BaseModel):
    """BodyComputeRagIndexesInBatchV1ConvaiKnowledgeBaseRagIndexPost

    :param items: List of requested RAG indexes. Minimum 1, maximum 100 items.
    :type items: List[GetOrCreateRagIndexRequestModel]
    """

    items: List[GetOrCreateRagIndexRequestModel] = Field(
        description="List of requested RAG indexes. Minimum 1, maximum 100 items."
    )
