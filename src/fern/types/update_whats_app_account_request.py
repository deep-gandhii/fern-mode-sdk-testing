from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class UpdateWhatsAppAccountRequest(BaseModel):
    """UpdateWhatsAppAccountRequest

    :param assigned_agent_id: assigned_agent_id, defaults to None
    :type assigned_agent_id: str, optional
    :param enable_messaging: enable_messaging, defaults to None
    :type enable_messaging: bool, optional
    :param enable_audio_message_response: enable_audio_message_response, defaults to None
    :type enable_audio_message_response: bool, optional
    :param enable_typing_indicator: enable_typing_indicator, defaults to None
    :type enable_typing_indicator: bool, optional
    """

    assigned_agent_id: Optional[str] = Field(default=None)
    enable_messaging: Optional[bool] = Field(default=None)
    enable_audio_message_response: Optional[bool] = Field(default=None)
    enable_typing_indicator: Optional[bool] = Field(default=None)
