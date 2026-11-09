from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

SmsConversationInfoDirection = typing.Union[
    typing.Literal["inbound", "outbound"], typing.Any
]


class SmsConversationInfo(BaseModel):
    """SmsConversationInfo

    :param direction: direction
    :type direction: SmsConversationInfoDirection
    :param phone_number_id: phone_number_id, defaults to None
    :type phone_number_id: str, optional
    :param sms_user_phone_number: sms_user_phone_number
    :type sms_user_phone_number: str
    :param agent_phone_number: agent_phone_number, defaults to None
    :type agent_phone_number: str, optional
    """

    direction: SmsConversationInfoDirection
    phone_number_id: Optional[str] = Field(default=None)
    sms_user_phone_number: str
    agent_phone_number: Optional[str] = Field(default=None)
