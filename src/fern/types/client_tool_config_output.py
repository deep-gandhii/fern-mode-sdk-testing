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
from .object_json_schema_property_output import ObjectJsonSchemaPropertyOutput
from .dynamic_variables_config import DynamicVariablesConfig
from .tool_execution_mode import ToolExecutionMode

ClientToolConfigOutputType = typing.Union[typing.Literal["client"], typing.Any]


class ClientToolConfigOutput(BaseModel):
    """A client tool is one that sends an event to the user's client to trigger something client side

    :param type: The type of tool, defaults to None
    :type type: ClientToolConfigOutputType, optional
    :param name: name
    :type name: str
    :param description: Description of when the tool should be used and what it does.
    :type description: str
    :param response_timeout_secs: The maximum time in seconds to wait for the tool call to complete. Must be between 1 and 120 seconds (inclusive)., defaults to None
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
    :param parameters: Schema for any parameters to pass to the client, defaults to None
    :type parameters: ObjectJsonSchemaPropertyOutput, optional
    :param expects_response: If true, calling this tool should block the conversation until the client responds with some response which is passed to the llm. If false then we will continue the conversation without waiting for the client to respond, this is useful to show content to a user but not block the conversation, defaults to None
    :type expects_response: bool, optional
    :param dynamic_variables: dynamic_variables, defaults to None
    :type dynamic_variables: DynamicVariablesConfig, optional
    :param execution_mode: execution_mode, defaults to None
    :type execution_mode: ToolExecutionMode, optional
    """

    type: Optional[ClientToolConfigOutputType] = Field(
        default=None, description="The type of tool"
    )
    name: str
    description: str = Field(
        description="Description of when the tool should be used and what it does."
    )
    response_timeout_secs: Optional[int] = Field(
        default=None,
        description="The maximum time in seconds to wait for the tool call to complete. Must be between 1 and 120 seconds (inclusive).",
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
    parameters: Optional[ObjectJsonSchemaPropertyOutput] = Field(
        default=None, description="Schema for any parameters to pass to the client"
    )
    expects_response: Optional[bool] = Field(
        default=None,
        description="If true, calling this tool should block the conversation until the client responds with some response which is passed to the llm. If false then we will continue the conversation without waiting for the client to respond, this is useful to show content to a user but not block the conversation",
    )
    dynamic_variables: Optional[DynamicVariablesConfig] = Field(default=None)
    execution_mode: Optional[ToolExecutionMode] = Field(default=None)
