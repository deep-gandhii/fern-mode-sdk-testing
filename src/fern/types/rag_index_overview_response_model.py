from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .rag_index_overview_embedding_model_response_model import (
    RagIndexOverviewEmbeddingModelResponseModel,
)


class RagIndexOverviewResponseModel(BaseModel):
    """RagIndexOverviewResponseModel

    :param total_used_bytes: total_used_bytes
    :type total_used_bytes: int
    :param total_max_bytes: total_max_bytes
    :type total_max_bytes: int
    :param models: models
    :type models: List[RagIndexOverviewEmbeddingModelResponseModel]
    """

    total_used_bytes: int
    total_max_bytes: int
    models: List[RagIndexOverviewEmbeddingModelResponseModel]
