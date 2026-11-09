from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dynamic_variable_update_common_model import DynamicVariableUpdateCommonModel

ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutputType = (
    typing.Union[typing.Literal["api_integration_webhook"], typing.Any]
)


class ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput(
    BaseModel
):
    """ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput

    :param request_id: request_id
    :type request_id: str
    :param tool_name: tool_name
    :type tool_name: str
    :param result_value: result_value
    :type result_value: str
    :param is_error: is_error
    :type is_error: bool
    :param is_blocked: is_blocked
    :type is_blocked: bool
    :param tool_has_been_called: tool_has_been_called
    :type tool_has_been_called: bool
    :param tool_latency_secs: tool_latency_secs
    :type tool_latency_secs: float
    :param error_type: error_type
    :type error_type: str
    :param raw_error_message: raw_error_message
    :type raw_error_message: str
    :param dynamic_variable_updates: dynamic_variable_updates
    :type dynamic_variable_updates: List[DynamicVariableUpdateCommonModel]
    :param type: type
    :type type: ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutputType
    :param integration_id: integration_id
    :type integration_id: str
    :param credential_id: credential_id
    :type credential_id: str
    :param integration_connection_id: integration_connection_id
    :type integration_connection_id: str
    """

    request_id: str
    tool_name: str
    result_value: str
    is_error: bool
    is_blocked: bool
    tool_has_been_called: bool
    tool_latency_secs: float
    error_type: str
    raw_error_message: str
    dynamic_variable_updates: List[DynamicVariableUpdateCommonModel]
    type: ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutputType = Field(
        default="api_integration_webhook"
    )
    integration_id: str
    credential_id: str
    integration_connection_id: str
