from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .telephony_direction import TelephonyDirection

ConversationHistoryTwilioPhoneCallModelType = typing.Union[
    typing.Literal["twilio"], typing.Any
]


class ConversationHistoryTwilioPhoneCallModel(BaseModel):
    """ConversationHistoryTwilioPhoneCallModel

    :param direction: direction
    :type direction: TelephonyDirection
    :param phone_number_id: phone_number_id
    :type phone_number_id: str
    :param agent_number: agent_number
    :type agent_number: str
    :param external_number: external_number
    :type external_number: str
    :param type: type
    :type type: ConversationHistoryTwilioPhoneCallModelType
    :param stream_sid: stream_sid
    :type stream_sid: str
    :param call_sid: call_sid
    :type call_sid: str
    """

    direction: TelephonyDirection
    phone_number_id: str
    agent_number: str
    external_number: str
    type: ConversationHistoryTwilioPhoneCallModelType = Field(default="twilio")
    stream_sid: str
    call_sid: str
