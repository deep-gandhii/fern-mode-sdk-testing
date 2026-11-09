from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

WhatsAppConversationInfoDirection = typing.Union[
    typing.Literal["inbound", "outbound", "unknown"], typing.Any
]


class WhatsAppConversationInfo(BaseModel):
    """WhatsAppConversationInfo

    :param direction: direction, defaults to None
    :type direction: WhatsAppConversationInfoDirection, optional
    :param whatsapp_phone_number_id: whatsapp_phone_number_id, defaults to None
    :type whatsapp_phone_number_id: str, optional
    :param whatsapp_user_id: whatsapp_user_id
    :type whatsapp_user_id: str
    :param awaiting_first_user_message: awaiting_first_user_message, defaults to None
    :type awaiting_first_user_message: bool, optional
    """

    direction: Optional[WhatsAppConversationInfoDirection] = Field(default=None)
    whatsapp_phone_number_id: Optional[str] = Field(default=None)
    whatsapp_user_id: str
    awaiting_first_user_message: Optional[bool] = Field(default=None)
