from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .tool_type import ToolType
from .conversation_history_transcript_tool_call_webhook_details import (
    ConversationHistoryTranscriptToolCallWebhookDetails,
)
from .conversation_history_transcript_tool_call_client_details import (
    ConversationHistoryTranscriptToolCallClientDetails,
)
from .conversation_history_transcript_tool_call_mcp_details import (
    ConversationHistoryTranscriptToolCallMcpDetails,
)
from .conversation_history_transcript_tool_call_api_integration_webhook_details_input import (
    ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsInput,
)


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
class ConversationHistoryTranscriptToolCallCommonModelInputToolDetails_Webhook(
    ConversationHistoryTranscriptToolCallWebhookDetails
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
class ConversationHistoryTranscriptToolCallCommonModelInputToolDetails_Client(
    ConversationHistoryTranscriptToolCallClientDetails
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
class ConversationHistoryTranscriptToolCallCommonModelInputToolDetails_Mcp(
    ConversationHistoryTranscriptToolCallMcpDetails
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
class ConversationHistoryTranscriptToolCallCommonModelInputToolDetails_ApiIntegrationWebhook(
    ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsInput
):
    pass


# Union type for ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
# Pydantic will attempt to validate against each type in order
ConversationHistoryTranscriptToolCallCommonModelInputToolDetails = Union[
    ConversationHistoryTranscriptToolCallWebhookDetails,
    ConversationHistoryTranscriptToolCallClientDetails,
    ConversationHistoryTranscriptToolCallMcpDetails,
    ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsInput,
]
# TypeAdapter for runtime validation of ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConversationHistoryTranscriptToolCallCommonModelInputToolDetails_adapter = TypeAdapter(
    ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
)


class ConversationHistoryTranscriptToolCallCommonModelInput(BaseModel):
    """ConversationHistoryTranscriptToolCallCommonModelInput

    :param type: type, defaults to None
    :type type: ToolType, optional
    :param request_id: request_id
    :type request_id: str
    :param tool_name: tool_name
    :type tool_name: str
    :param params_as_json: params_as_json
    :type params_as_json: str
    :param tool_has_been_called: tool_has_been_called
    :type tool_has_been_called: bool
    :param tool_details: tool_details, defaults to None
    :type tool_details: ConversationHistoryTranscriptToolCallCommonModelInputToolDetails, optional
    """

    type: Optional[ToolType] = Field(default=None)
    request_id: str
    tool_name: str
    params_as_json: str
    tool_has_been_called: bool
    tool_details: Optional[
        ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
    ] = Field(default=None)
