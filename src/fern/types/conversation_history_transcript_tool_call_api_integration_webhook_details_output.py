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

ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsOutputType = (
    typing.Union[typing.Literal["api_integration_webhook"], typing.Any]
)


class ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsOutput(
    BaseModel
):
    """ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsOutput

    :param type: type
    :type type: ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsOutputType
    :param integration_id: integration_id
    :type integration_id: str
    :param credential_id: credential_id
    :type credential_id: str
    :param integration_connection_id: integration_connection_id
    :type integration_connection_id: str
    :param webhook_details: webhook_details
    :type webhook_details: ConversationHistoryTranscriptToolCallWebhookDetails
    """

    type: ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsOutputType = Field(
        default="api_integration_webhook"
    )
    integration_id: str
    credential_id: str
    integration_connection_id: str
    webhook_details: ConversationHistoryTranscriptToolCallWebhookDetails
