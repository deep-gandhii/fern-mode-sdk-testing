from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class WhatsAppOutboundCallResponse(BaseModel):
    """WhatsAppOutboundCallResponse

    :param success: success
    :type success: bool
    :param message: message
    :type message: str
    :param conversation_id: conversation_id
    :type conversation_id: str
    """

    success: bool
    message: str
    conversation_id: Optional[str]
