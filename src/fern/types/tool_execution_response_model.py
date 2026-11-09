from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .conversation_history_transcript_tool_call_webhook_details import (
    ConversationHistoryTranscriptToolCallWebhookDetails,
)
from .conversation_history_transcript_tool_call_client_details import (
    ConversationHistoryTranscriptToolCallClientDetails,
)
from .conversation_history_transcript_tool_call_mcp_details import (
    ConversationHistoryTranscriptToolCallMcpDetails,
)
from .conversation_history_transcript_tool_call_api_integration_webhook_details_output import (
    ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsOutput,
)


# fernMode variant type for a shared-component member of ToolExecutionResponseModelToolCallDetails
class ToolExecutionResponseModelToolCallDetails_Webhook(
    ConversationHistoryTranscriptToolCallWebhookDetails
):
    pass


# fernMode variant type for a shared-component member of ToolExecutionResponseModelToolCallDetails
class ToolExecutionResponseModelToolCallDetails_Client(
    ConversationHistoryTranscriptToolCallClientDetails
):
    pass


# fernMode variant type for a shared-component member of ToolExecutionResponseModelToolCallDetails
class ToolExecutionResponseModelToolCallDetails_Mcp(
    ConversationHistoryTranscriptToolCallMcpDetails
):
    pass


# fernMode variant type for a shared-component member of ToolExecutionResponseModelToolCallDetails
class ToolExecutionResponseModelToolCallDetails_ApiIntegrationWebhook(
    ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsOutput
):
    pass


# Union type for ToolExecutionResponseModelToolCallDetails
# Pydantic will attempt to validate against each type in order
ToolExecutionResponseModelToolCallDetails = Union[
    ConversationHistoryTranscriptToolCallWebhookDetails,
    ConversationHistoryTranscriptToolCallClientDetails,
    ConversationHistoryTranscriptToolCallMcpDetails,
    ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetailsOutput,
]
# TypeAdapter for runtime validation of ToolExecutionResponseModelToolCallDetails
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ToolExecutionResponseModelToolCallDetails_adapter = TypeAdapter(
    ToolExecutionResponseModelToolCallDetails
)


class ToolExecutionResponseModel(BaseModel):
    """ToolExecutionResponseModel

    :param tool_id: The ID of the tool that was executed
    :type tool_id: str
    :param tool_request_id: The request/call ID associated with this tool execution
    :type tool_request_id: str
    :param conversation_id: The ID of the conversation where the tool was executed
    :type conversation_id: str
    :param agent_id: The ID of the agent that ran the tool
    :type agent_id: str
    :param branch_id: The branch ID if the agent has branches, defaults to None
    :type branch_id: str, optional
    :param timestamp: Unix timestamp when the tool was executed
    :type timestamp: float
    :param latency_secs: How long the tool execution took
    :type latency_secs: float
    :param is_error: Whether the tool execution failed, defaults to None
    :type is_error: bool, optional
    :param request_payload: LLM-extracted parameters sent to the tool (JSON string), defaults to None
    :type request_payload: str, optional
    :param response_payload: Response returned by the tool, defaults to None
    :type response_payload: str, optional
    :param error_message: Error message if the tool execution failed, defaults to None
    :type error_message: str, optional
    :param error_type: Error category (internal, customer_config, customer_auth, external_server, external_client, client_timeout, unknown), defaults to None
    :type error_type: str, optional
    :param id: id
    :type id: str
    :param tool_call_details: tool_call_details, defaults to None
    :type tool_call_details: ToolExecutionResponseModelToolCallDetails, optional
    """

    tool_id: str = Field(description="The ID of the tool that was executed")
    tool_request_id: str = Field(
        description="The request/call ID associated with this tool execution"
    )
    conversation_id: str = Field(
        description="The ID of the conversation where the tool was executed"
    )
    agent_id: str = Field(description="The ID of the agent that ran the tool")
    branch_id: Optional[str] = Field(
        default=None, description="The branch ID if the agent has branches"
    )
    timestamp: float = Field(description="Unix timestamp when the tool was executed")
    latency_secs: float = Field(description="How long the tool execution took")
    is_error: Optional[bool] = Field(
        default=None, description="Whether the tool execution failed"
    )
    request_payload: Optional[str] = Field(
        default=None,
        description="LLM-extracted parameters sent to the tool (JSON string)",
    )
    response_payload: Optional[str] = Field(
        default=None, description="Response returned by the tool"
    )
    error_message: Optional[str] = Field(
        default=None, description="Error message if the tool execution failed"
    )
    error_type: Optional[str] = Field(
        default=None,
        description="Error category (internal, customer_config, customer_auth, external_server, external_client, client_timeout, unknown)",
    )
    id: str
    tool_call_details: Optional[ToolExecutionResponseModelToolCallDetails] = Field(
        default=None
    )
