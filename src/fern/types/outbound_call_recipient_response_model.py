from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .batch_call_recipient_status import BatchCallRecipientStatus
from .conversation_initiation_client_data_internal import (
    ConversationInitiationClientDataInternal,
)


class OutboundCallRecipientResponseModel(BaseModel):
    """OutboundCallRecipientResponseModel

    :param id: id
    :type id: str
    :param phone_number: phone_number, defaults to None
    :type phone_number: str, optional
    :param whatsapp_user_id: whatsapp_user_id, defaults to None
    :type whatsapp_user_id: str, optional
    :param status: status
    :type status: BatchCallRecipientStatus
    :param created_at_unix: created_at_unix
    :type created_at_unix: int
    :param updated_at_unix: updated_at_unix
    :type updated_at_unix: int
    :param conversation_id: conversation_id
    :type conversation_id: str
    :param conversation_initiation_client_data: conversation_initiation_client_data, defaults to None
    :type conversation_initiation_client_data: ConversationInitiationClientDataInternal, optional
    """

    id: str
    phone_number: Optional[str] = Field(default=None)
    whatsapp_user_id: Optional[str] = Field(default=None)
    status: BatchCallRecipientStatus
    created_at_unix: int
    updated_at_unix: int
    conversation_id: Optional[str]
    conversation_initiation_client_data: Optional[
        ConversationInitiationClientDataInternal
    ] = Field(default=None)
