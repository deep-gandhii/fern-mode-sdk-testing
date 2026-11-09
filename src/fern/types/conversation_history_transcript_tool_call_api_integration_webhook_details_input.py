from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_history_transcript_tool_call_webhook_details import (
    ConversationHistoryTranscriptToolCallWebhookDetails,
)

ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsInputType = (
    typing.Union[typing.Literal["api_integration_webhook"], typing.Any]
)


class ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsInput(BaseModel):
    """ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsInput

    :param type: type, defaults to None
    :type type: ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsInputType, optional
    :param integration_id: integration_id, defaults to None
    :type integration_id: str, optional
    :param credential_id: credential_id, defaults to None
    :type credential_id: str, optional
    :param integration_connection_id: integration_connection_id, defaults to None
    :type integration_connection_id: str, optional
    :param webhook_details: webhook_details
    :type webhook_details: ConversationHistoryTranscriptToolCallWebhookDetails
    """

    type: Optional[
        ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsInputType
    ] = Field(default=None)
    integration_id: Optional[str] = Field(default=None)
    credential_id: Optional[str] = Field(default=None)
    integration_connection_id: Optional[str] = Field(default=None)
    webhook_details: ConversationHistoryTranscriptToolCallWebhookDetails
