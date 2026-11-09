from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .speech_history_item_response import SpeechHistoryItemResponse


class GetSpeechHistoryResponse(BaseModel):
    """GetSpeechHistoryResponse

    :param history: A list of speech history items.
    :type history: List[SpeechHistoryItemResponse]
    :param last_history_item_id: The ID of the last history item., defaults to None
    :type last_history_item_id: str, optional
    :param has_more: Whether there are more history items to fetch.
    :type has_more: bool
    :param scanned_until: The timestamp of the last history item., defaults to None
    :type scanned_until: int, optional
    """

    history: List[SpeechHistoryItemResponse] = Field(
        description="A list of speech history items."
    )
    last_history_item_id: Optional[str] = Field(
        default=None, description="The ID of the last history item."
    )
    has_more: bool = Field(description="Whether there are more history items to fetch.")
    scanned_until: Optional[int] = Field(
        default=None, description="The timestamp of the last history item."
    )
