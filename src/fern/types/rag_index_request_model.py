from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .embedding_model_enum import EmbeddingModelEnum


class RagIndexRequestModel(BaseModel):
    """RagIndexRequestModel

    :param model: model
    :type model: EmbeddingModelEnum
    """

    model: EmbeddingModelEnum
