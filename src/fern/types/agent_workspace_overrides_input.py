from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_initiation_client_data_webhook import (
    ConversationInitiationClientDataWebhook,
)
from .conv_ai_webhooks import ConvAiWebhooks


class AgentWorkspaceOverridesInput(BaseModel):
    """AgentWorkspaceOverridesInput

    :param conversation_initiation_client_data_webhook: The webhook to send conversation initiation client data to, defaults to None
    :type conversation_initiation_client_data_webhook: ConversationInitiationClientDataWebhook, optional
    :param webhooks: webhooks, defaults to None
    :type webhooks: ConvAiWebhooks, optional
    """

    conversation_initiation_client_data_webhook: Optional[
        ConversationInitiationClientDataWebhook
    ] = Field(
        default=None,
        description="The webhook to send conversation initiation client data to",
    )
    webhooks: Optional[ConvAiWebhooks] = Field(default=None)
