from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .mcp_approval_policy import McpApprovalPolicy
from .pre_tool_speech_mode import PreToolSpeechMode
from .tool_interruption_mode import ToolInterruptionMode
from .tool_call_sound_type import ToolCallSoundType
from .tool_call_sound_behavior import ToolCallSoundBehavior
from .tool_execution_mode import ToolExecutionMode
from .conv_ai_secret_locator import ConvAiSecretLocator
from .conv_ai_dynamic_variable import ConvAiDynamicVariable
from .conv_ai_env_var_locator import ConvAiEnvVarLocator
from .auth_connection_locator import AuthConnectionLocator
from .environment_auth_connection_locator import EnvironmentAuthConnectionLocator

# Union type for McpServerConfigUpdateRequestModelRequestHeadersValue
# Pydantic will attempt to validate against each type in order
McpServerConfigUpdateRequestModelRequestHeadersValue = Union[
    str, ConvAiSecretLocator, ConvAiDynamicVariable, ConvAiEnvVarLocator
]
# TypeAdapter for runtime validation of McpServerConfigUpdateRequestModelRequestHeadersValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpServerConfigUpdateRequestModelRequestHeadersValue_adapter = TypeAdapter(
    McpServerConfigUpdateRequestModelRequestHeadersValue
)


# Union type for McpServerConfigUpdateRequestModelAuthConnection
# Pydantic will attempt to validate against each type in order
McpServerConfigUpdateRequestModelAuthConnection = Union[
    AuthConnectionLocator, EnvironmentAuthConnectionLocator
]
# TypeAdapter for runtime validation of McpServerConfigUpdateRequestModelAuthConnection
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpServerConfigUpdateRequestModelAuthConnection_adapter = TypeAdapter(
    McpServerConfigUpdateRequestModelAuthConnection
)


class McpServerConfigUpdateRequestModel(BaseModel):
    """Unified request model for updating MCP Server configuration.

    :param approval_policy: The approval mode to set for the MCP server, defaults to None
    :type approval_policy: McpApprovalPolicy, optional
    :param force_pre_tool_speech: DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool., defaults to None
    :type force_pre_tool_speech: bool, optional
    :param pre_tool_speech: If set, overrides the server's pre_tool_speech setting for this tool., defaults to None
    :type pre_tool_speech: PreToolSpeechMode, optional
    :param disable_interruptions: DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool., defaults to None
    :type disable_interruptions: bool, optional
    :param interruption_mode: If set, overrides the server's interruption_mode setting for this tool., defaults to None
    :type interruption_mode: ToolInterruptionMode, optional
    :param tool_call_sound: Predefined tool call sound type to play during tool execution for all tools from this MCP server, defaults to None
    :type tool_call_sound: ToolCallSoundType, optional
    :param tool_call_sound_behavior: Determines when the tool call sound should play for all tools from this MCP server, defaults to None
    :type tool_call_sound_behavior: ToolCallSoundBehavior, optional
    :param execution_mode: If set, overrides the server's execution_mode setting for this tool, defaults to None
    :type execution_mode: ToolExecutionMode, optional
    :param response_timeout_secs: The maximum time in seconds to wait for each MCP tool call to complete., defaults to None
    :type response_timeout_secs: int, optional
    :param request_headers: The headers to include in requests to the MCP server, defaults to None
    :type request_headers: Dict[str, McpServerConfigUpdateRequestModelRequestHeadersValue], optional
    :param disable_compression: Whether to disable HTTP compression for this MCP server, defaults to None
    :type disable_compression: bool, optional
    :param secret_token: Optional secret token for authentication with this MCP server, defaults to None
    :type secret_token: ConvAiSecretLocator, optional
    :param auth_connection: Optional auth connection to use for authentication with this MCP server, defaults to None
    :type auth_connection: McpServerConfigUpdateRequestModelAuthConnection, optional
    """

    approval_policy: Optional[McpApprovalPolicy] = Field(
        default=None, description="The approval mode to set for the MCP server"
    )
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
    tool_call_sound: Optional[ToolCallSoundType] = Field(
        default=None,
        description="Predefined tool call sound type to play during tool execution for all tools from this MCP server",
    )
    tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = Field(
        default=None,
        description="Determines when the tool call sound should play for all tools from this MCP server",
    )
    execution_mode: Optional[ToolExecutionMode] = Field(
        default=None,
        description="If set, overrides the server's execution_mode setting for this tool",
    )
    response_timeout_secs: Optional[int] = Field(
        default=None,
        description="The maximum time in seconds to wait for each MCP tool call to complete.",
    )
    request_headers: Optional[
        Dict[str, McpServerConfigUpdateRequestModelRequestHeadersValue]
    ] = Field(
        default=None, description="The headers to include in requests to the MCP server"
    )
    disable_compression: Optional[bool] = Field(
        default=None,
        description="Whether to disable HTTP compression for this MCP server",
    )
    secret_token: Optional[ConvAiSecretLocator] = Field(
        default=None,
        description="Optional secret token for authentication with this MCP server",
    )
    auth_connection: Optional[McpServerConfigUpdateRequestModelAuthConnection] = Field(
        default=None,
        description="Optional auth connection to use for authentication with this MCP server",
    )
