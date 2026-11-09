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
from .livekit_stack_type import LivekitStackType


class GetConvAiSettingsResponseModel(BaseModel):
    """GetConvAiSettingsResponseModel

    :param conversation_initiation_client_data_webhook: conversation_initiation_client_data_webhook, defaults to None
    :type conversation_initiation_client_data_webhook: ConversationInitiationClientDataWebhook, optional
    :param webhooks: webhooks, defaults to None
    :type webhooks: ConvAiWebhooks, optional
    :param can_use_mcp_servers: Whether the workspace can use MCP servers, defaults to None
    :type can_use_mcp_servers: bool, optional
    :param rag_retention_period_days: rag_retention_period_days, defaults to None
    :type rag_retention_period_days: int, optional
    :param conversation_embedding_retention_days: Days to retain conversation embeddings. None means use the system default (30 days)., defaults to None
    :type conversation_embedding_retention_days: int, optional
    :param default_livekit_stack: default_livekit_stack, defaults to None
    :type default_livekit_stack: LivekitStackType, optional
    """

    conversation_initiation_client_data_webhook: Optional[
        ConversationInitiationClientDataWebhook
    ] = Field(default=None)
    webhooks: Optional[ConvAiWebhooks] = Field(default=None)
    can_use_mcp_servers: Optional[bool] = Field(
        default=None, description="Whether the workspace can use MCP servers"
    )
    rag_retention_period_days: Optional[int] = Field(default=None)
    conversation_embedding_retention_days: Optional[int] = Field(
        default=None,
        description="Days to retain conversation embeddings. None means use the system default (30 days).",
    )
    default_livekit_stack: Optional[LivekitStackType] = Field(default=None)
