from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .tool_interruption_mode import ToolInterruptionMode
from .pre_tool_speech_mode import PreToolSpeechMode
from .dynamic_variable_assignment import DynamicVariableAssignment
from .tool_call_sound_type import ToolCallSoundType
from .tool_call_sound_behavior import ToolCallSoundBehavior
from .tool_error_handling_mode import ToolErrorHandlingMode
from .dynamic_variables_config import DynamicVariablesConfig
from .tool_execution_mode import ToolExecutionMode
from .api_integration_webhook_overrides import ApiIntegrationWebhookOverrides

ApiIntegrationWebhookToolConfigOutputType = typing.Union[
    typing.Literal["api_integration_webhook"], typing.Any
]


class ApiIntegrationWebhookToolConfigOutput(BaseModel):
    """ApiIntegrationWebhookToolConfigOutput

    :param type: type
    :type type: ApiIntegrationWebhookToolConfigOutputType
    :param name: name
    :type name: str
    :param description: Description of when the tool should be used and what it does.
    :type description: str
    :param response_timeout_secs: The maximum time in seconds to wait for the tool call to complete. Must be between 5 and 120 seconds (inclusive).
    :type response_timeout_secs: int
    :param disable_interruptions: DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
    :type disable_interruptions: bool
    :param interruption_mode: interruption_mode
    :type interruption_mode: ToolInterruptionMode
    :param force_pre_tool_speech: DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
    :type force_pre_tool_speech: bool
    :param pre_tool_speech: pre_tool_speech
    :type pre_tool_speech: PreToolSpeechMode
    :param assignments: Configuration for extracting values from tool responses and assigning them to dynamic variables
    :type assignments: List[DynamicVariableAssignment]
    :param tool_call_sound: Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
    :type tool_call_sound: ToolCallSoundType
    :param tool_call_sound_behavior: Determines how the tool call sound should be played.
    :type tool_call_sound_behavior: ToolCallSoundBehavior
    :param tool_error_handling_mode: Controls how tool errors are processed before being shared with the agent.
    :type tool_error_handling_mode: ToolErrorHandlingMode
    :param dynamic_variables: dynamic_variables
    :type dynamic_variables: DynamicVariablesConfig
    :param execution_mode: execution_mode
    :type execution_mode: ToolExecutionMode
    :param tool_version: The version of the API integration tool
    :type tool_version: str
    :param api_integration_id: api_integration_id
    :type api_integration_id: str
    :param api_integration_connection_id: api_integration_connection_id
    :type api_integration_connection_id: str
    :param api_schema_overrides: User overrides applied on top of the base api_schema
    :type api_schema_overrides: ApiIntegrationWebhookOverrides
    """

    type: ApiIntegrationWebhookToolConfigOutputType = Field(
        default="api_integration_webhook"
    )
    name: str
    description: str = Field(
        description="Description of when the tool should be used and what it does."
    )
    response_timeout_secs: int = Field(
        description="The maximum time in seconds to wait for the tool call to complete. Must be between 5 and 120 seconds (inclusive)."
    )
    disable_interruptions: bool = Field(
        description="DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running."
    )
    interruption_mode: ToolInterruptionMode
    force_pre_tool_speech: bool = Field(
        description="DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call."
    )
    pre_tool_speech: PreToolSpeechMode
    assignments: List[DynamicVariableAssignment] = Field(
        description="Configuration for extracting values from tool responses and assigning them to dynamic variables"
    )
    tool_call_sound: ToolCallSoundType = Field(
        description="Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played."
    )
    tool_call_sound_behavior: ToolCallSoundBehavior = Field(
        description="Determines how the tool call sound should be played."
    )
    tool_error_handling_mode: ToolErrorHandlingMode = Field(
        description="Controls how tool errors are processed before being shared with the agent."
    )
    dynamic_variables: DynamicVariablesConfig
    execution_mode: ToolExecutionMode
    tool_version: str = Field(description="The version of the API integration tool")
    api_integration_id: str
    api_integration_connection_id: str
    api_schema_overrides: Optional[ApiIntegrationWebhookOverrides] = Field(
        description="User overrides applied on top of the base api_schema"
    )
