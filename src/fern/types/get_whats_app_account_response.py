from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class GetWhatsAppAccountResponse(BaseModel):
    """GetWhatsAppAccountResponse

    :param business_account_id: business_account_id
    :type business_account_id: str
    :param phone_number_id: phone_number_id
    :type phone_number_id: str
    :param business_account_name: business_account_name
    :type business_account_name: str
    :param phone_number_name: phone_number_name
    :type phone_number_name: str
    :param phone_number: phone_number
    :type phone_number: str
    :param assigned_agent_id: assigned_agent_id, defaults to None
    :type assigned_agent_id: str, optional
    :param enable_messaging: enable_messaging, defaults to None
    :type enable_messaging: bool, optional
    :param enable_audio_message_response: enable_audio_message_response, defaults to None
    :type enable_audio_message_response: bool, optional
    :param enable_typing_indicator: enable_typing_indicator, defaults to None
    :type enable_typing_indicator: bool, optional
    :param assigned_agent_name: assigned_agent_name
    :type assigned_agent_name: str
    :param is_token_expired: is_token_expired, defaults to None
    :type is_token_expired: bool, optional
    """

    business_account_id: str
    phone_number_id: str
    business_account_name: str
    phone_number_name: str
    phone_number: str
    assigned_agent_id: Optional[str] = Field(default=None)
    enable_messaging: Optional[bool] = Field(default=None)
    enable_audio_message_response: Optional[bool] = Field(default=None)
    enable_typing_indicator: Optional[bool] = Field(default=None)
    assigned_agent_name: Optional[str]
    is_token_expired: Optional[bool] = Field(default=None)
