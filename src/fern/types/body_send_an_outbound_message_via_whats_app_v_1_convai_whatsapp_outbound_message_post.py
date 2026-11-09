from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .conversation_initiation_client_data_request_input import (
    ConversationInitiationClientDataRequestInput,
)
from .whats_app_template_header_component_params import (
    WhatsAppTemplateHeaderComponentParams,
)
from .whats_app_template_body_component_params import (
    WhatsAppTemplateBodyComponentParams,
)
from .whats_app_template_button_component_params import (
    WhatsAppTemplateButtonComponentParams,
)


# fernMode variant type for a shared-component member of BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
class BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem_Header(
    WhatsAppTemplateHeaderComponentParams
):
    pass


# fernMode variant type for a shared-component member of BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
class BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem_Body(
    WhatsAppTemplateBodyComponentParams
):
    pass


# fernMode variant type for a shared-component member of BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
class BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem_Button(
    WhatsAppTemplateButtonComponentParams
):
    pass


# Union type for BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
# Pydantic will attempt to validate against each type in order
BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem = Union[
    WhatsAppTemplateHeaderComponentParams,
    WhatsAppTemplateBodyComponentParams,
    WhatsAppTemplateButtonComponentParams,
]
# TypeAdapter for runtime validation of BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem_adapter = TypeAdapter(
    BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
)


class BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePost(
    BaseModel
):
    """BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePost

    :param whatsapp_phone_number_id: whatsapp_phone_number_id
    :type whatsapp_phone_number_id: str
    :param whatsapp_user_id: whatsapp_user_id
    :type whatsapp_user_id: str
    :param template_name: template_name
    :type template_name: str
    :param template_language_code: template_language_code
    :type template_language_code: str
    :param template_params: template_params
    :type template_params: List[BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem]
    :param agent_id: agent_id
    :type agent_id: str
    :param conversation_initiation_client_data: conversation_initiation_client_data, defaults to None
    :type conversation_initiation_client_data: ConversationInitiationClientDataRequestInput, optional
    """

    whatsapp_phone_number_id: str
    whatsapp_user_id: str
    template_name: str
    template_language_code: str
    template_params: List[
        BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
    ]
    agent_id: str
    conversation_initiation_client_data: Optional[
        ConversationInitiationClientDataRequestInput
    ] = Field(default=None)
