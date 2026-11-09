from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class HistoryItemResponse(BaseModel):
    """HistoryItemResponse

    :param state: state, defaults to None
    :type state: Any, optional
    :param voice_category: voice_category, defaults to None
    :type voice_category: Any, optional
    """

    state: Optional[Any] = Field(default=None)
    voice_category: Optional[Any] = Field(default=None)
