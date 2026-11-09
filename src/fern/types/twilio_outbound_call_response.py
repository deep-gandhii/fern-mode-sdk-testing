from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class TwilioOutboundCallResponse(BaseModel):
    """TwilioOutboundCallResponse

    :param success: success
    :type success: bool
    :param message: message
    :type message: str
    :param conversation_id: conversation_id
    :type conversation_id: str
    :param call_sid: call_sid
    :type call_sid: str
    """

    success: bool
    message: str
    conversation_id: Optional[str]
    call_sid: Optional[str] = Field(alias="callSid", serialization_alias="callSid")
