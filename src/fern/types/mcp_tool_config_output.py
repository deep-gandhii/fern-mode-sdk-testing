from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .tool_interruption_mode import ToolInterruptionMode
from .pre_tool_speech_mode import PreToolSpeechMode
from .dynamic_variable_assignment import DynamicVariableAssignment
from .tool_call_sound_type import ToolCallSoundType
from .tool_call_sound_behavior import ToolCallSoundBehavior
from .tool_error_handling_mode import ToolErrorHandlingMode
from .integration_type import IntegrationType
from .object_json_schema_property_output import ObjectJsonSchemaPropertyOutput
from .mcp_approval_policy import McpApprovalPolicy
from .tool_execution_mode import ToolExecutionMode
from .constant_schema_override import ConstantSchemaOverride
from .dynamic_variable_schema_override import DynamicVariableSchemaOverride
from .llm_schema_override import LlmSchemaOverride
from .omit_schema_override import OmitSchemaOverride

McpToolConfigOutputType = typing.Union[typing.Literal["mcp"], typing.Any]


# fernMode variant type for a shared-component member of McpToolConfigOutputInputOverridesValue
class McpToolConfigOutputInputOverridesValue_Constant(ConstantSchemaOverride):
    pass


# fernMode variant type for a shared-component member of McpToolConfigOutputInputOverridesValue
class McpToolConfigOutputInputOverridesValue_DynamicVariable(
    DynamicVariableSchemaOverride
):
    pass


# fernMode variant type for a shared-component member of McpToolConfigOutputInputOverridesValue
class McpToolConfigOutputInputOverridesValue_Llm(LlmSchemaOverride):
    pass


# fernMode variant type for a shared-component member of McpToolConfigOutputInputOverridesValue
class McpToolConfigOutputInputOverridesValue_Omit(OmitSchemaOverride):
    pass


# Union type for McpToolConfigOutputInputOverridesValue
# Pydantic will attempt to validate against each type in order
McpToolConfigOutputInputOverridesValue = Union[
    ConstantSchemaOverride,
    DynamicVariableSchemaOverride,
    LlmSchemaOverride,
    OmitSchemaOverride,
]
# TypeAdapter for runtime validation of McpToolConfigOutputInputOverridesValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpToolConfigOutputInputOverridesValue_adapter = TypeAdapter(
    McpToolConfigOutputInputOverridesValue
)


class McpToolConfigOutput(BaseModel):
    """An MCP tool configuration that can be used to call MCP servers

    :param type: type, defaults to None
    :type type: McpToolConfigOutputType, optional
    :param name: name
    :type name: str
    :param description: Description of when the tool should be used and what it does.
    :type description: str
    :param response_timeout_secs: The maximum time in seconds to wait for the MCP tool call to complete. Must be between 5 and 300 seconds (inclusive)., defaults to None
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
    :param integration_type: integration_type
    :type integration_type: IntegrationType
    :param parameters: Schema for any parameters the LLM needs to provide to the MCP tool., defaults to None
    :type parameters: ObjectJsonSchemaPropertyOutput, optional
    :param approval_policy: Defines the MCP server-level approval policy for tool execution., defaults to None
    :type approval_policy: McpApprovalPolicy, optional
    :param mcp_tool_name: The name of the MCP tool to call
    :type mcp_tool_name: str
    :param mcp_tool_description: The description of the MCP tool to call
    :type mcp_tool_description: str
    :param mcp_server_id: The id of the MCP server to call
    :type mcp_server_id: str
    :param mcp_server_name: The name of the MCP server to call
    :type mcp_server_name: str
    :param mcp_input_schema: Original inputSchema dict for consistent hashing, defaults to None
    :type mcp_input_schema: Dict[str, Any], optional
    :param execution_mode: execution_mode, defaults to None
    :type execution_mode: ToolExecutionMode, optional
    :param input_overrides: Input parameter overrides for this tool, defaults to None
    :type input_overrides: Dict[str, McpToolConfigOutputInputOverridesValue], optional
    """

    type: Optional[McpToolConfigOutputType] = Field(default=None)
    name: str
    description: str = Field(
        description="Description of when the tool should be used and what it does."
    )
    response_timeout_secs: Optional[int] = Field(
        default=None,
        description="The maximum time in seconds to wait for the MCP tool call to complete. Must be between 5 and 300 seconds (inclusive).",
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
    integration_type: IntegrationType
    parameters: Optional[ObjectJsonSchemaPropertyOutput] = Field(
        default=None,
        description="Schema for any parameters the LLM needs to provide to the MCP tool.",
    )
    approval_policy: Optional[McpApprovalPolicy] = Field(
        default=None,
        description="Defines the MCP server-level approval policy for tool execution.",
    )
    mcp_tool_name: str = Field(description="The name of the MCP tool to call")
    mcp_tool_description: str = Field(
        description="The description of the MCP tool to call"
    )
    mcp_server_id: str = Field(description="The id of the MCP server to call")
    mcp_server_name: str = Field(description="The name of the MCP server to call")
    mcp_input_schema: Optional[Dict[str, Any]] = Field(
        default=None, description="Original inputSchema dict for consistent hashing"
    )
    execution_mode: Optional[ToolExecutionMode] = Field(default=None)
    input_overrides: Optional[Dict[str, McpToolConfigOutputInputOverridesValue]] = (
        Field(default=None, description="Input parameter overrides for this tool")
    )
