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
from .pre_tool_speech_mode import PreToolSpeechMode
from .tool_interruption_mode import ToolInterruptionMode
from .tool_call_sound_behavior import ToolCallSoundBehavior
from .tool_execution_mode import ToolExecutionMode
from .dynamic_variable_assignment import DynamicVariableAssignment
from .tool_response_mock_config_output import ToolResponseMockConfigOutput
from .tool_call_sound_type import ToolCallSoundType
from .constant_schema_override import ConstantSchemaOverride
from .dynamic_variable_schema_override import DynamicVariableSchemaOverride
from .llm_schema_override import LlmSchemaOverride
from .omit_schema_override import OmitSchemaOverride

ToolCallSound21 = typing.Union[typing.Literal["off"], typing.Any]


# Union type for McpToolConfigOverrideOutputToolCallSound
# Pydantic will attempt to validate against each type in order
McpToolConfigOverrideOutputToolCallSound = Union[str, str]
# TypeAdapter for runtime validation of McpToolConfigOverrideOutputToolCallSound
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpToolConfigOverrideOutputToolCallSound_adapter = TypeAdapter(
    McpToolConfigOverrideOutputToolCallSound
)


# fernMode variant type for a shared-component member of McpToolConfigOverrideOutputInputOverridesValue
class McpToolConfigOverrideOutputInputOverridesValue_Constant(ConstantSchemaOverride):
    pass


# fernMode variant type for a shared-component member of McpToolConfigOverrideOutputInputOverridesValue
class McpToolConfigOverrideOutputInputOverridesValue_DynamicVariable(
    DynamicVariableSchemaOverride
):
    pass


# fernMode variant type for a shared-component member of McpToolConfigOverrideOutputInputOverridesValue
class McpToolConfigOverrideOutputInputOverridesValue_Llm(LlmSchemaOverride):
    pass


# fernMode variant type for a shared-component member of McpToolConfigOverrideOutputInputOverridesValue
class McpToolConfigOverrideOutputInputOverridesValue_Omit(OmitSchemaOverride):
    pass


# Union type for McpToolConfigOverrideOutputInputOverridesValue
# Pydantic will attempt to validate against each type in order
McpToolConfigOverrideOutputInputOverridesValue = Union[
    ConstantSchemaOverride,
    DynamicVariableSchemaOverride,
    LlmSchemaOverride,
    OmitSchemaOverride,
]
# TypeAdapter for runtime validation of McpToolConfigOverrideOutputInputOverridesValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpToolConfigOverrideOutputInputOverridesValue_adapter = TypeAdapter(
    McpToolConfigOverrideOutputInputOverridesValue
)


class McpToolConfigOverrideOutput(BaseModel):
    """McpToolConfigOverrideOutput

    :param tool_name: The name of the MCP tool
    :type tool_name: str
    :param force_pre_tool_speech: DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool., defaults to None
    :type force_pre_tool_speech: bool, optional
    :param pre_tool_speech: If set, overrides the server's pre_tool_speech setting for this tool., defaults to None
    :type pre_tool_speech: PreToolSpeechMode, optional
    :param disable_interruptions: DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool., defaults to None
    :type disable_interruptions: bool, optional
    :param interruption_mode: If set, overrides the server's interruption_mode setting for this tool., defaults to None
    :type interruption_mode: ToolInterruptionMode, optional
    :param tool_call_sound: Overrides the server's tool_call_sound setting for this tool. A sound name plays that sound; 'off' overrides to no sound (silence); null means do not override (inherit the server default)., defaults to None
    :type tool_call_sound: McpToolConfigOverrideOutputToolCallSound, optional
    :param tool_call_sound_behavior: If set, overrides the server's tool_call_sound_behavior setting for this tool, defaults to None
    :type tool_call_sound_behavior: ToolCallSoundBehavior, optional
    :param execution_mode: If set, overrides the server's execution_mode setting for this tool, defaults to None
    :type execution_mode: ToolExecutionMode, optional
    :param response_timeout_secs: If set, overrides the server's response timeout for this MCP tool (seconds)., defaults to None
    :type response_timeout_secs: int, optional
    :param assignments: Dynamic variable assignments for this MCP tool, defaults to None
    :type assignments: List[DynamicVariableAssignment], optional
    :param input_overrides: Mapping of json path to input override configuration, defaults to None
    :type input_overrides: Dict[str, McpToolConfigOverrideOutputInputOverridesValue], optional
    :param response_mocks: Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins., defaults to None
    :type response_mocks: List[ToolResponseMockConfigOutput], optional
    """

    tool_name: str = Field(description="The name of the MCP tool")
    force_pre_tool_speech: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool.",
    )
    pre_tool_speech: Optional[PreToolSpeechMode] = Field(
        default=None,
        description="If set, overrides the server's pre_tool_speech setting for this tool.",
    )
    disable_interruptions: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool.",
    )
    interruption_mode: Optional[ToolInterruptionMode] = Field(
        default=None,
        description="If set, overrides the server's interruption_mode setting for this tool.",
    )
    tool_call_sound: Optional[McpToolConfigOverrideOutputToolCallSound] = Field(
        default=None,
        description="Overrides the server's tool_call_sound setting for this tool. A sound name plays that sound; 'off' overrides to no sound (silence); null means do not override (inherit the server default).",
    )
    tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = Field(
        default=None,
        description="If set, overrides the server's tool_call_sound_behavior setting for this tool",
    )
    execution_mode: Optional[ToolExecutionMode] = Field(
        default=None,
        description="If set, overrides the server's execution_mode setting for this tool",
    )
    response_timeout_secs: Optional[int] = Field(
        default=None,
        description="If set, overrides the server's response timeout for this MCP tool (seconds).",
    )
    assignments: Optional[List[DynamicVariableAssignment]] = Field(
        default=None, description="Dynamic variable assignments for this MCP tool"
    )
    input_overrides: Optional[
        Dict[str, McpToolConfigOverrideOutputInputOverridesValue]
    ] = Field(
        default=None, description="Mapping of json path to input override configuration"
    )
    response_mocks: Optional[List[ToolResponseMockConfigOutput]] = Field(
        default=None,
        description="Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.",
    )
