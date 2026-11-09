from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConversationHistoryRagUsageCommonModel(BaseModel):
    """ConversationHistoryRagUsageCommonModel

    :param usage_count: usage_count
    :type usage_count: int
    :param embedding_model: embedding_model
    :type embedding_model: str
    """

    usage_count: int
    embedding_model: str
