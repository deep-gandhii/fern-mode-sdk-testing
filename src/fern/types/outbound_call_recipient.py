from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_initiation_client_data_request_input import (
    ConversationInitiationClientDataRequestInput,
)


class OutboundCallRecipient(BaseModel):
    """OutboundCallRecipient

    :param id: id, defaults to None
    :type id: str, optional
    :param phone_number: phone_number, defaults to None
    :type phone_number: str, optional
    :param whatsapp_user_id: whatsapp_user_id, defaults to None
    :type whatsapp_user_id: str, optional
    :param conversation_initiation_client_data: conversation_initiation_client_data, defaults to None
    :type conversation_initiation_client_data: ConversationInitiationClientDataRequestInput, optional
    """

    id: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    whatsapp_user_id: Optional[str] = Field(default=None)
    conversation_initiation_client_data: Optional[
        ConversationInitiationClientDataRequestInput
    ] = Field(default=None)
