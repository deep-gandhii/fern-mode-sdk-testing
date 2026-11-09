from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .mcp_approval_policy import McpApprovalPolicy
from .mcp_tool_approval_hash import McpToolApprovalHash
from .mcp_server_transport import McpServerTransport
from .pre_tool_speech_mode import PreToolSpeechMode
from .tool_interruption_mode import ToolInterruptionMode
from .tool_call_sound_type import ToolCallSoundType
from .tool_call_sound_behavior import ToolCallSoundBehavior
from .tool_execution_mode import ToolExecutionMode
from .mcp_tool_config_override_input import McpToolConfigOverrideInput
from .conv_ai_secret_locator import ConvAiSecretLocator
from .conv_ai_user_secret_db_model import ConvAiUserSecretDbModel
from .conv_ai_dynamic_variable import ConvAiDynamicVariable
from .conv_ai_env_var_locator import ConvAiEnvVarLocator
from .auth_connection_locator import AuthConnectionLocator
from .environment_auth_connection_locator import EnvironmentAuthConnectionLocator

# Union type for McpServerConfigInputUrl
# Pydantic will attempt to validate against each type in order
McpServerConfigInputUrl = Union[str, ConvAiSecretLocator]
# TypeAdapter for runtime validation of McpServerConfigInputUrl
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpServerConfigInputUrl_adapter = TypeAdapter(McpServerConfigInputUrl)


# Union type for McpServerConfigInputSecretToken
# Pydantic will attempt to validate against each type in order
McpServerConfigInputSecretToken = Union[ConvAiSecretLocator, ConvAiUserSecretDbModel]
# TypeAdapter for runtime validation of McpServerConfigInputSecretToken
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpServerConfigInputSecretToken_adapter = TypeAdapter(McpServerConfigInputSecretToken)


# Union type for McpServerConfigInputRequestHeadersValue
# Pydantic will attempt to validate against each type in order
McpServerConfigInputRequestHeadersValue = Union[
    str, ConvAiSecretLocator, ConvAiDynamicVariable, ConvAiEnvVarLocator
]
# TypeAdapter for runtime validation of McpServerConfigInputRequestHeadersValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpServerConfigInputRequestHeadersValue_adapter = TypeAdapter(
    McpServerConfigInputRequestHeadersValue
)


# Union type for McpServerConfigInputAuthConnection
# Pydantic will attempt to validate against each type in order
McpServerConfigInputAuthConnection = Union[
    AuthConnectionLocator, EnvironmentAuthConnectionLocator
]
# TypeAdapter for runtime validation of McpServerConfigInputAuthConnection
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpServerConfigInputAuthConnection_adapter = TypeAdapter(
    McpServerConfigInputAuthConnection
)


class McpServerConfigInput(BaseModel):
    """McpServerConfigInput

    :param approval_policy: Defines the MCP server-level approval policy for tool execution., defaults to None
    :type approval_policy: McpApprovalPolicy, optional
    :param tool_approval_hashes: List of tool approval hashes for per-tool approval when approval_policy is REQUIRE_APPROVAL_PER_TOOL, defaults to None
    :type tool_approval_hashes: List[McpToolApprovalHash], optional
    :param transport: Supported MCP server transport types., defaults to None
    :type transport: McpServerTransport, optional
    :param url: The URL of the MCP server, if this contains a secret please store as a workspace secret, otherwise store as a plain string. Must use https
    :type url: McpServerConfigInputUrl
    :param secret_token: The secret token (Authorization header) stored as a workspace secret or in-place secret, defaults to None
    :type secret_token: McpServerConfigInputSecretToken, optional
    :param request_headers: The headers included in the request, defaults to None
    :type request_headers: Dict[str, McpServerConfigInputRequestHeadersValue], optional
    :param auth_connection: Optional auth connection to use for authentication with this MCP server, defaults to None
    :type auth_connection: McpServerConfigInputAuthConnection, optional
    :param name: name
    :type name: str
    :param description: description, defaults to None
    :type description: str, optional
    :param force_pre_tool_speech: DEPRECATED: use `pre_tool_speech` instead. If true, all tools from this MCP server will require pre-tool execution speech., defaults to None
    :type force_pre_tool_speech: bool, optional
    :param pre_tool_speech: pre_tool_speech, defaults to None
    :type pre_tool_speech: PreToolSpeechMode, optional
    :param disable_interruptions: DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while any tool from this MCP server is running., defaults to None
    :type disable_interruptions: bool, optional
    :param interruption_mode: interruption_mode, defaults to None
    :type interruption_mode: ToolInterruptionMode, optional
    :param tool_call_sound: Predefined tool call sound type to play during tool execution for all tools from this MCP server, defaults to None
    :type tool_call_sound: ToolCallSoundType, optional
    :param tool_call_sound_behavior: Determines how the tool call sound should be played., defaults to None
    :type tool_call_sound_behavior: ToolCallSoundBehavior, optional
    :param execution_mode: execution_mode, defaults to None
    :type execution_mode: ToolExecutionMode, optional
    :param response_timeout_secs: The maximum time in seconds to wait for each MCP tool call to complete. Must be between 5 and 300 seconds (inclusive)., defaults to None
    :type response_timeout_secs: int, optional
    :param tool_config_overrides: List of per-tool configuration overrides that override the server-level defaults for specific tools, defaults to None
    :type tool_config_overrides: List[McpToolConfigOverrideInput], optional
    :param disable_compression: Whether to disable HTTP compression for this MCP server. Enable this if the server does not support compressed responses., defaults to None
    :type disable_compression: bool, optional
    """

    approval_policy: Optional[McpApprovalPolicy] = Field(
        default=None,
        description="Defines the MCP server-level approval policy for tool execution.",
    )
    tool_approval_hashes: Optional[List[McpToolApprovalHash]] = Field(
        default=None,
        description="List of tool approval hashes for per-tool approval when approval_policy is REQUIRE_APPROVAL_PER_TOOL",
    )
    transport: Optional[McpServerTransport] = Field(
        default=None, description="Supported MCP server transport types."
    )
    url: McpServerConfigInputUrl = Field(
        description="The URL of the MCP server, if this contains a secret please store as a workspace secret, otherwise store as a plain string. Must use https"
    )
    secret_token: Optional[McpServerConfigInputSecretToken] = Field(
        default=None,
        description="The secret token (Authorization header) stored as a workspace secret or in-place secret",
    )
    request_headers: Optional[Dict[str, McpServerConfigInputRequestHeadersValue]] = (
        Field(default=None, description="The headers included in the request")
    )
    auth_connection: Optional[McpServerConfigInputAuthConnection] = Field(
        default=None,
        description="Optional auth connection to use for authentication with this MCP server",
    )
    name: str
    description: Optional[str] = Field(default=None)
    force_pre_tool_speech: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `pre_tool_speech` instead. If true, all tools from this MCP server will require pre-tool execution speech.",
    )
    pre_tool_speech: Optional[PreToolSpeechMode] = Field(default=None)
    disable_interruptions: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while any tool from this MCP server is running.",
    )
    interruption_mode: Optional[ToolInterruptionMode] = Field(default=None)
    tool_call_sound: Optional[ToolCallSoundType] = Field(
        default=None,
        description="Predefined tool call sound type to play during tool execution for all tools from this MCP server",
    )
    tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = Field(
        default=None, description="Determines how the tool call sound should be played."
    )
    execution_mode: Optional[ToolExecutionMode] = Field(default=None)
    response_timeout_secs: Optional[int] = Field(
        default=None,
        description="The maximum time in seconds to wait for each MCP tool call to complete. Must be between 5 and 300 seconds (inclusive).",
    )
    tool_config_overrides: Optional[List[McpToolConfigOverrideInput]] = Field(
        default=None,
        description="List of per-tool configuration overrides that override the server-level defaults for specific tools",
    )
    disable_compression: Optional[bool] = Field(
        default=None,
        description="Whether to disable HTTP compression for this MCP server. Enable this if the server does not support compressed responses.",
    )
