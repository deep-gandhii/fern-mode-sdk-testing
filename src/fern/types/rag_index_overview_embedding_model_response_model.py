from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .embedding_model_enum import EmbeddingModelEnum


class RagIndexOverviewEmbeddingModelResponseModel(BaseModel):
    """RagIndexOverviewEmbeddingModelResponseModel

    :param model: model
    :type model: EmbeddingModelEnum
    :param used_bytes: used_bytes
    :type used_bytes: int
    """

    model: EmbeddingModelEnum
    used_bytes: int
