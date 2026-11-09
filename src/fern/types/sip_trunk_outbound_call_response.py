from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SipTrunkOutboundCallResponse(BaseModel):
    """SipTrunkOutboundCallResponse

    :param success: success
    :type success: bool
    :param message: message
    :type message: str
    :param conversation_id: conversation_id
    :type conversation_id: str
    :param sip_call_id: sip_call_id
    :type sip_call_id: str
    """

    success: bool
    message: str
    conversation_id: Optional[str]
    sip_call_id: Optional[str]
