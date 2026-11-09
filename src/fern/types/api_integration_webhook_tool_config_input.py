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

ApiIntegrationWebhookToolConfigInputType = typing.Union[
    typing.Literal["api_integration_webhook"], typing.Any
]


class ApiIntegrationWebhookToolConfigInput(BaseModel):
    """ApiIntegrationWebhookToolConfigInput

    :param type: type, defaults to None
    :type type: ApiIntegrationWebhookToolConfigInputType, optional
    :param name: name
    :type name: str
    :param description: Description of when the tool should be used and what it does.
    :type description: str
    :param response_timeout_secs: The maximum time in seconds to wait for the tool call to complete. Must be between 5 and 120 seconds (inclusive)., defaults to None
    :type response_timeout_secs: int, optional
    :param disable_interruptions: DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running., defaults to None
    :type disable_interruptions: bool, optional
    :param interruption_mode: interruption_mode, defaults to None
    :type interruption_mode: ToolInterruptionMode, optional
    :param force_pre_tool_speech: DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call., defaults to None
    :type force_pre_tool_speech: bool, optional
    :param pre_tool_speech: pre_tool_speech, defaults to None
    :type pre_tool_speech: PreToolSpeechMode, optional
    :param assignments: Configuration for extracting values from tool responses and assigning them to dynamic variables, defaults to None
    :type assignments: List[DynamicVariableAssignment], optional
    :param tool_call_sound: Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played., defaults to None
    :type tool_call_sound: ToolCallSoundType, optional
    :param tool_call_sound_behavior: Determines how the tool call sound should be played., defaults to None
    :type tool_call_sound_behavior: ToolCallSoundBehavior, optional
    :param tool_error_handling_mode: Controls how tool errors are processed before being shared with the agent., defaults to None
    :type tool_error_handling_mode: ToolErrorHandlingMode, optional
    :param dynamic_variables: dynamic_variables, defaults to None
    :type dynamic_variables: DynamicVariablesConfig, optional
    :param execution_mode: execution_mode, defaults to None
    :type execution_mode: ToolExecutionMode, optional
    :param tool_version: The version of the API integration tool, defaults to None
    :type tool_version: str, optional
    :param api_integration_id: api_integration_id
    :type api_integration_id: str
    :param api_integration_connection_id: api_integration_connection_id
    :type api_integration_connection_id: str
    :param api_schema_overrides: User overrides applied on top of the base api_schema, defaults to None
    :type api_schema_overrides: ApiIntegrationWebhookOverrides, optional
    """

    type: Optional[ApiIntegrationWebhookToolConfigInputType] = Field(default=None)
    name: str
    description: str = Field(
        description="Description of when the tool should be used and what it does."
    )
    response_timeout_secs: Optional[int] = Field(
        default=None,
        description="The maximum time in seconds to wait for the tool call to complete. Must be between 5 and 120 seconds (inclusive).",
    )
    disable_interruptions: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.",
    )
    interruption_mode: Optional[ToolInterruptionMode] = Field(default=None)
    force_pre_tool_speech: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.",
    )
    pre_tool_speech: Optional[PreToolSpeechMode] = Field(default=None)
    assignments: Optional[List[DynamicVariableAssignment]] = Field(
        default=None,
        description="Configuration for extracting values from tool responses and assigning them to dynamic variables",
    )
    tool_call_sound: Optional[ToolCallSoundType] = Field(
        default=None,
        description="Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.",
    )
    tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = Field(
        default=None, description="Determines how the tool call sound should be played."
    )
    tool_error_handling_mode: Optional[ToolErrorHandlingMode] = Field(
        default=None,
        description="Controls how tool errors are processed before being shared with the agent.",
    )
    dynamic_variables: Optional[DynamicVariablesConfig] = Field(default=None)
    execution_mode: Optional[ToolExecutionMode] = Field(default=None)
    tool_version: Optional[str] = Field(
        default=None, description="The version of the API integration tool"
    )
    api_integration_id: str
    api_integration_connection_id: str
    api_schema_overrides: Optional[ApiIntegrationWebhookOverrides] = Field(
        default=None, description="User overrides applied on top of the base api_schema"
    )
