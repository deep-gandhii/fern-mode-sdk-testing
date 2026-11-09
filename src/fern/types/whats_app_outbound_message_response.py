from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class WhatsAppOutboundMessageResponse(BaseModel):
    """WhatsAppOutboundMessageResponse

    :param conversation_id: conversation_id
    :type conversation_id: str
    """

    conversation_id: str
