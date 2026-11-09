from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConversationHistoryElevenAssistantCommonModel(BaseModel):
    """ConversationHistoryElevenAssistantCommonModel

    :param is_eleven_assistant: is_eleven_assistant, defaults to None
    :type is_eleven_assistant: bool, optional
    """

    is_eleven_assistant: Optional[bool] = Field(default=None)
