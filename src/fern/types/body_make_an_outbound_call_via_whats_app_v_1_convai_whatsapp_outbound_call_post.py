from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_initiation_client_data_request_input import (
    ConversationInitiationClientDataRequestInput,
)


class BodyMakeAnOutboundCallViaWhatsAppV1ConvaiWhatsappOutboundCallPost(BaseModel):
    """BodyMakeAnOutboundCallViaWhatsAppV1ConvaiWhatsappOutboundCallPost

    :param whatsapp_phone_number_id: whatsapp_phone_number_id
    :type whatsapp_phone_number_id: str
    :param whatsapp_user_id: whatsapp_user_id
    :type whatsapp_user_id: str
    :param whatsapp_call_permission_request_template_name: whatsapp_call_permission_request_template_name
    :type whatsapp_call_permission_request_template_name: str
    :param whatsapp_call_permission_request_template_language_code: whatsapp_call_permission_request_template_language_code
    :type whatsapp_call_permission_request_template_language_code: str
    :param agent_id: agent_id
    :type agent_id: str
    :param conversation_initiation_client_data: conversation_initiation_client_data, defaults to None
    :type conversation_initiation_client_data: ConversationInitiationClientDataRequestInput, optional
    """

    whatsapp_phone_number_id: str
    whatsapp_user_id: str
    whatsapp_call_permission_request_template_name: str
    whatsapp_call_permission_request_template_language_code: str
    agent_id: str
    conversation_initiation_client_data: Optional[
        ConversationInitiationClientDataRequestInput
    ] = Field(default=None)
