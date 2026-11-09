from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .conv_ai_secret_locator import ConvAiSecretLocator

# Union type for ConversationInitiationClientDataWebhookRequestHeadersValue
# Pydantic will attempt to validate against each type in order
ConversationInitiationClientDataWebhookRequestHeadersValue = Union[
    str, ConvAiSecretLocator
]
# TypeAdapter for runtime validation of ConversationInitiationClientDataWebhookRequestHeadersValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConversationInitiationClientDataWebhookRequestHeadersValue_adapter = TypeAdapter(
    ConversationInitiationClientDataWebhookRequestHeadersValue
)


class ConversationInitiationClientDataWebhook(BaseModel):
    """ConversationInitiationClientDataWebhook

    :param url: The URL to send the webhook to
    :type url: str
    :param request_headers: The headers to send with the webhook request
    :type request_headers: Dict[str, ConversationInitiationClientDataWebhookRequestHeadersValue]
    """

    url: str = Field(description="The URL to send the webhook to")
    request_headers: Dict[
        str, ConversationInitiationClientDataWebhookRequestHeadersValue
    ] = Field(description="The headers to send with the webhook request")
