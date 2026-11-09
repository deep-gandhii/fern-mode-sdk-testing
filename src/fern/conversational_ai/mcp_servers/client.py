from typing import Any, Optional, Dict, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    ConvAiSecretLocator,
    HttpValidationError,
    McpApprovalPolicy,
    McpServerConfigInput,
    McpServerConfigUpdateRequestModel,
    McpServerConfigUpdateRequestModelAuthConnection,
    McpServerConfigUpdateRequestModelRequestHeadersValue,
    McpServerRequestModel,
    McpServerResponseModel,
    McpServersResponseModel,
    PreToolSpeechMode,
    ToolCallSoundBehavior,
    ToolCallSoundType,
    ToolExecutionMode,
    ToolInterruptionMode,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tools.client import (
        ToolsClient as _ToolsClient,
        AsyncToolsClient as _AsyncToolsClient,
    )
    from .approval_policy.client import (
        ApprovalPolicyClient as _ApprovalPolicyClient,
        AsyncApprovalPolicyClient as _AsyncApprovalPolicyClient,
    )
    from .tool_approvals.client import (
        ToolApprovalsClient as _ToolApprovalsClient,
        AsyncToolApprovalsClient as _AsyncToolApprovalsClient,
    )
    from .tool_configs.client import (
        ToolConfigsClient as _ToolConfigsClient,
        AsyncToolConfigsClient as _AsyncToolConfigsClient,
    )


class McpServersClient(BaseService):
    """
    Fern-style resource client for McpServersClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._tools: Any = None
        self._approval_policy: Any = None
        self._tool_approvals: Any = None
        self._tool_configs: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    @property
    def tools(self) -> "_ToolsClient":
        """Lazily construct and return the tools sub-resource client."""
        if self._tools is None:
            from .tools.client import ToolsClient

            _child = ToolsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tools = _child
        return self._tools

    @property
    def approval_policy(self) -> "_ApprovalPolicyClient":
        """Lazily construct and return the approval_policy sub-resource client."""
        if self._approval_policy is None:
            from .approval_policy.client import ApprovalPolicyClient

            _child = ApprovalPolicyClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._approval_policy = _child
        return self._approval_policy

    @property
    def tool_approvals(self) -> "_ToolApprovalsClient":
        """Lazily construct and return the tool_approvals sub-resource client."""
        if self._tool_approvals is None:
            from .tool_approvals.client import ToolApprovalsClient

            _child = ToolApprovalsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tool_approvals = _child
        return self._tool_approvals

    @property
    def tool_configs(self) -> "_ToolConfigsClient":
        """Lazily construct and return the tool_configs sub-resource client."""
        if self._tool_configs is None:
            from .tool_configs.client import ToolConfigsClient

            _child = ToolConfigsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tool_configs = _child
        return self._tool_configs

    def set_base_url(self, base_url: Union[ElevenLabsEnvironment, str]):
        """
        Sets the base URL for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's base URL and then cached, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error.

        :param base_url: The base URL to be set, as a string or an ElevenLabsEnvironment enum member.
        :return: The resource client.
        """
        super().set_base_url(base_url)
        if self._tools is not None:
            self._tools.set_base_url(base_url)
        if self._approval_policy is not None:
            self._approval_policy.set_base_url(base_url)
        if self._tool_approvals is not None:
            self._tool_approvals.set_base_url(base_url)
        if self._tool_configs is not None:
            self._tool_configs.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for this resource client and every sub-resource client
        already built.

        A child is constructed holding a reference to this client's config and is then cached,
        and both this setter and `set_retry` REBIND `_service_config` rather than mutating it --
        so an already-materialised child kept the config it was born with. The parent wins:
        last writer overwrites, the same rule `set_base_url` and `set_timeout` follow, which keeps
        a client and its children in exact agreement. Narrower scopes are untouched, because
        method-level config (`set_<method>_config`) and per-call `request_options` live in their
        own attributes and are never overwritten by this.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The resource client.
        """
        super().set_config(config)
        if self._tools is not None:
            self._tools.set_config(config)
        if self._approval_policy is not None:
            self._approval_policy.set_config(config)
        if self._tool_approvals is not None:
            self._tool_approvals.set_config(config)
        if self._tool_configs is not None:
            self._tool_configs.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's timeout and its request handler is
        built from it, so the inherited setter -- which only rebinds the receiver and rebuilds the
        receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The resource client.
        """
        super().set_timeout(timeout)
        if self._tools is not None:
            self._tools.set_timeout(timeout)
        if self._approval_policy is not None:
            self._approval_policy.set_timeout(timeout)
        if self._tool_approvals is not None:
            self._tool_approvals.set_timeout(timeout)
        if self._tool_configs is not None:
            self._tool_configs.set_timeout(timeout)

        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    @property
    def with_raw_response(self) -> "RawMcpServersClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawMcpServersClient(self)

    @cast_models
    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> McpServersResponseModel:
        """
        Retrieve all MCP server configurations available in the workspace.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServersResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.mcp_servers.list()
        """

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                McpServersResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(McpServersResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        config: McpServerConfigInput,
        request_options: Optional[RequestOptions] = None,
    ) -> McpServerResponseModel:
        """
        Create a new MCP server configuration in the workspace.

        Parameters
        ----------
        config : McpServerConfigInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServerResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.mcp_servers.create(
            config={
                "approval_policy": "auto_approve_all",
                "tool_approval_hashes": [
                    {
                        "tool_name": "tool_name",
                        "tool_hash": "tool_hash",
                        "approval_policy": "auto_approved"
                    }
                ],
                "transport": "SSE",
                "url": "quis cillum inc",
                "secret_token": {
                    "secret_id": "secret_id"
                },
                "request_headers": {},
                "auth_connection": {
                    "auth_connection_id": "auth_connection_id"
                },
                "name": "name",
                "description": "description",
                "pre_tool_speech": "auto",
                "interruption_mode": "allow",
                "tool_call_sound": "typing",
                "tool_call_sound_behavior": "auto",
                "execution_mode": "immediate",
                "response_timeout_secs": 30,
                "tool_config_overrides": [
                    {
                        "tool_name": "tool_name",
                        "pre_tool_speech": "auto",
                        "interruption_mode": "allow",
                        "tool_call_sound": "typing",
                        "tool_call_sound_behavior": "auto",
                        "execution_mode": "immediate",
                        "response_timeout_secs": 132,
                        "assignments": [
                            {
                                "source": "response",
                                "dynamic_variable": "dynamic_variable",
                                "value_path": "value_path",
                                "sanitize": True,
                                "preserve_native_type": True
                            }
                        ],
                        "input_overrides": {},
                        "response_mocks": [
                            {
                                "parameter_conditions": [
                                    {
                                        "eval": {
                                            "type": "llm",
                                            "description": "description"
                                        },
                                        "path": "path"
                                    }
                                ],
                                "mock_result": "mock_result",
                                "is_error": True
                            }
                        ]
                    }
                ],
                "disable_compression": False
            },
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = McpServerRequestModel(config=config)
        Validator(McpServerRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                McpServerResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(McpServerResponseModel, response)
            )
        )

    @cast_models
    def get(
        self, mcp_server_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> McpServerResponseModel:
        """
        Retrieve a specific MCP server configuration from the workspace.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServerResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.mcp_servers.get(
            mcp_server_id="mcp_server_id",
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                McpServerResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(McpServerResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        mcp_server_id: str,
        *,
        approval_policy: Optional[McpApprovalPolicy] = SENTINEL,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Optional[ToolCallSoundType] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        request_headers: Union[
            Dict[str, McpServerConfigUpdateRequestModelRequestHeadersValue], None
        ] = SENTINEL,
        disable_compression: Union[bool, None] = SENTINEL,
        secret_token: Optional[ConvAiSecretLocator] = SENTINEL,
        auth_connection: Union[
            McpServerConfigUpdateRequestModelAuthConnection, None
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> McpServerResponseModel:
        """
        Update the configuration settings for an MCP server.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        approval_policy : typing.Optional[McpApprovalPolicy]
            The approval mode to set for the MCP server

        force_pre_tool_speech : typing.Optional[bool]
            DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool.

        pre_tool_speech : typing.Optional[PreToolSpeechMode]
            If set, overrides the server's pre_tool_speech setting for this tool.

        disable_interruptions : typing.Optional[bool]
            DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool.

        interruption_mode : typing.Optional[ToolInterruptionMode]
            If set, overrides the server's interruption_mode setting for this tool.

        tool_call_sound : typing.Optional[ToolCallSoundType]
            Predefined tool call sound type to play during tool execution for all tools from this MCP server

        tool_call_sound_behavior : typing.Optional[ToolCallSoundBehavior]
            Determines when the tool call sound should play for all tools from this MCP server

        execution_mode : typing.Optional[ToolExecutionMode]
            If set, overrides the server's execution_mode setting for this tool

        response_timeout_secs : typing.Optional[int]
            The maximum time in seconds to wait for each MCP tool call to complete.

        request_headers : typing.Optional[typing.Dict[str, McpServerConfigUpdateRequestModelRequestHeadersValue]]
            The headers to include in requests to the MCP server

        disable_compression : typing.Optional[bool]
            Whether to disable HTTP compression for this MCP server

        secret_token : typing.Optional[ConvAiSecretLocator]
            Optional secret token for authentication with this MCP server

        auth_connection : typing.Optional[McpServerConfigUpdateRequestModelAuthConnection]
            Optional auth connection to use for authentication with this MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServerResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            approval_policy="auto_approve_all",
            pre_tool_speech="auto",
            interruption_mode="allow",
            tool_call_sound="typing",
            tool_call_sound_behavior="auto",
            execution_mode="immediate",
            response_timeout_secs=208,
            request_headers={},
            disable_compression=False,
            secret_token={
                "secret_id": "secret_id"
            },
            auth_connection={
                "auth_connection_id": "auth_connection_id"
            },
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = McpServerConfigUpdateRequestModel(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "approval_policy": approval_policy,
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "request_headers": request_headers,
                        "disable_compression": disable_compression,
                        "secret_token": secret_token,
                        "auth_connection": auth_connection,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(McpServerConfigUpdateRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                McpServerResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(McpServerResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, mcp_server_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Any:
        """
        Delete a specific MCP server configuration from the workspace.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.mcp_servers.delete(
            mcp_server_id="mcp_server_id",
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawMcpServersClient:
    """
    Raw-response client for McpServersClient.

    Each method delegates to the matching :class:`McpServersClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: McpServersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[McpServersResponseModel]:
        data = McpServersClient.list(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        config: McpServerConfigInput,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = McpServersClient.create(
            self._client, config=config, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, mcp_server_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[McpServerResponseModel]:
        data = McpServersClient.get(
            self._client, mcp_server_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        mcp_server_id: str,
        *,
        approval_policy: Optional[McpApprovalPolicy] = SENTINEL,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Optional[ToolCallSoundType] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        request_headers: Union[
            Dict[str, McpServerConfigUpdateRequestModelRequestHeadersValue], None
        ] = SENTINEL,
        disable_compression: Union[bool, None] = SENTINEL,
        secret_token: Optional[ConvAiSecretLocator] = SENTINEL,
        auth_connection: Union[
            McpServerConfigUpdateRequestModelAuthConnection, None
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = McpServersClient.update(
            self._client,
            mcp_server_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "approval_policy": approval_policy,
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "request_headers": request_headers,
                        "disable_compression": disable_compression,
                        "secret_token": secret_token,
                        "auth_connection": auth_connection,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, mcp_server_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = McpServersClient.delete(
            self._client, mcp_server_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncMcpServersClient(McpServersClient):
    """
    Async wrapper for McpServersClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def tools(self) -> "_AsyncToolsClient":
        """Lazily construct and return the async tools sub-resource client."""
        if self._tools is None:
            from .tools.client import AsyncToolsClient

            _child = AsyncToolsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tools = _child
        return self._tools

    @property
    def approval_policy(self) -> "_AsyncApprovalPolicyClient":
        """Lazily construct and return the async approval_policy sub-resource client."""
        if self._approval_policy is None:
            from .approval_policy.client import AsyncApprovalPolicyClient

            _child = AsyncApprovalPolicyClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._approval_policy = _child
        return self._approval_policy

    @property
    def tool_approvals(self) -> "_AsyncToolApprovalsClient":
        """Lazily construct and return the async tool_approvals sub-resource client."""
        if self._tool_approvals is None:
            from .tool_approvals.client import AsyncToolApprovalsClient

            _child = AsyncToolApprovalsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tool_approvals = _child
        return self._tool_approvals

    @property
    def tool_configs(self) -> "_AsyncToolConfigsClient":
        """Lazily construct and return the async tool_configs sub-resource client."""
        if self._tool_configs is None:
            from .tool_configs.client import AsyncToolConfigsClient

            _child = AsyncToolConfigsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tool_configs = _child
        return self._tool_configs

    @property
    def with_raw_response(self) -> "AsyncRawMcpServersClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawMcpServersClient(self)

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[McpServersResponseModel]:  # type: ignore[override]
        """
        Retrieve all MCP server configurations available in the workspace.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServersResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.mcp_servers.list()


        asyncio.run(main())
        """
        return to_async(super().list)(request_options=request_options)

    def create(
        self,
        *,
        config: McpServerConfigInput,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[McpServerResponseModel]:  # type: ignore[override]
        """
        Create a new MCP server configuration in the workspace.

        Parameters
        ----------
        config : McpServerConfigInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServerResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.mcp_servers.create(
                config={
                    "approval_policy": "auto_approve_all",
                    "tool_approval_hashes": [
                        {
                            "tool_name": "tool_name",
                            "tool_hash": "tool_hash",
                            "approval_policy": "auto_approved"
                        }
                    ],
                    "transport": "SSE",
                    "url": "quis cillum inc",
                    "secret_token": {
                        "secret_id": "secret_id"
                    },
                    "request_headers": {},
                    "auth_connection": {
                        "auth_connection_id": "auth_connection_id"
                    },
                    "name": "name",
                    "description": "description",
                    "pre_tool_speech": "auto",
                    "interruption_mode": "allow",
                    "tool_call_sound": "typing",
                    "tool_call_sound_behavior": "auto",
                    "execution_mode": "immediate",
                    "response_timeout_secs": 30,
                    "tool_config_overrides": [
                        {
                            "tool_name": "tool_name",
                            "pre_tool_speech": "auto",
                            "interruption_mode": "allow",
                            "tool_call_sound": "typing",
                            "tool_call_sound_behavior": "auto",
                            "execution_mode": "immediate",
                            "response_timeout_secs": 132,
                            "assignments": [
                                {
                                    "source": "response",
                                    "dynamic_variable": "dynamic_variable",
                                    "value_path": "value_path",
                                    "sanitize": True,
                                    "preserve_native_type": True
                                }
                            ],
                            "input_overrides": {},
                            "response_mocks": [
                                {
                                    "parameter_conditions": [
                                        {
                                            "eval": {
                                                "type": "llm",
                                                "description": "description"
                                            },
                                            "path": "path"
                                        }
                                    ],
                                    "mock_result": "mock_result",
                                    "is_error": True
                                }
                            ]
                        }
                    ],
                    "disable_compression": False
                },
            )


        asyncio.run(main())
        """
        return to_async(super().create)(config=config, request_options=request_options)

    def get(
        self, mcp_server_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[McpServerResponseModel]:  # type: ignore[override]
        """
        Retrieve a specific MCP server configuration from the workspace.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServerResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.mcp_servers.get(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(mcp_server_id, request_options=request_options)

    def update(
        self,
        mcp_server_id: str,
        *,
        approval_policy: Optional[McpApprovalPolicy] = SENTINEL,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Optional[ToolCallSoundType] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        request_headers: Union[
            Dict[str, McpServerConfigUpdateRequestModelRequestHeadersValue], None
        ] = SENTINEL,
        disable_compression: Union[bool, None] = SENTINEL,
        secret_token: Optional[ConvAiSecretLocator] = SENTINEL,
        auth_connection: Union[
            McpServerConfigUpdateRequestModelAuthConnection, None
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[McpServerResponseModel]:  # type: ignore[override]
        """
        Update the configuration settings for an MCP server.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        approval_policy : typing.Optional[McpApprovalPolicy]
            The approval mode to set for the MCP server

        force_pre_tool_speech : typing.Optional[bool]
            DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool.

        pre_tool_speech : typing.Optional[PreToolSpeechMode]
            If set, overrides the server's pre_tool_speech setting for this tool.

        disable_interruptions : typing.Optional[bool]
            DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool.

        interruption_mode : typing.Optional[ToolInterruptionMode]
            If set, overrides the server's interruption_mode setting for this tool.

        tool_call_sound : typing.Optional[ToolCallSoundType]
            Predefined tool call sound type to play during tool execution for all tools from this MCP server

        tool_call_sound_behavior : typing.Optional[ToolCallSoundBehavior]
            Determines when the tool call sound should play for all tools from this MCP server

        execution_mode : typing.Optional[ToolExecutionMode]
            If set, overrides the server's execution_mode setting for this tool

        response_timeout_secs : typing.Optional[int]
            The maximum time in seconds to wait for each MCP tool call to complete.

        request_headers : typing.Optional[typing.Dict[str, McpServerConfigUpdateRequestModelRequestHeadersValue]]
            The headers to include in requests to the MCP server

        disable_compression : typing.Optional[bool]
            Whether to disable HTTP compression for this MCP server

        secret_token : typing.Optional[ConvAiSecretLocator]
            Optional secret token for authentication with this MCP server

        auth_connection : typing.Optional[McpServerConfigUpdateRequestModelAuthConnection]
            Optional auth connection to use for authentication with this MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServerResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.mcp_servers.update(
                mcp_server_id="mcp_server_id",
                approval_policy="auto_approve_all",
                pre_tool_speech="auto",
                interruption_mode="allow",
                tool_call_sound="typing",
                tool_call_sound_behavior="auto",
                execution_mode="immediate",
                response_timeout_secs=208,
                request_headers={},
                disable_compression=False,
                secret_token={
                    "secret_id": "secret_id"
                },
                auth_connection={
                    "auth_connection_id": "auth_connection_id"
                },
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            mcp_server_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "approval_policy": approval_policy,
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "request_headers": request_headers,
                        "disable_compression": disable_compression,
                        "secret_token": secret_token,
                        "auth_connection": auth_connection,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, mcp_server_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete a specific MCP server configuration from the workspace.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.mcp_servers.delete(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(mcp_server_id, request_options=request_options)


class AsyncRawMcpServersClient:
    """
    Async raw-response client for AsyncMcpServersClient.
    """

    def __init__(self, client: AsyncMcpServersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[McpServersResponseModel]:
        data = await AsyncMcpServersClient.list(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        config: McpServerConfigInput,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = await AsyncMcpServersClient.create(
            self._client, config=config, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, mcp_server_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[McpServerResponseModel]:
        data = await AsyncMcpServersClient.get(
            self._client, mcp_server_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        mcp_server_id: str,
        *,
        approval_policy: Optional[McpApprovalPolicy] = SENTINEL,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Optional[ToolCallSoundType] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        request_headers: Union[
            Dict[str, McpServerConfigUpdateRequestModelRequestHeadersValue], None
        ] = SENTINEL,
        disable_compression: Union[bool, None] = SENTINEL,
        secret_token: Optional[ConvAiSecretLocator] = SENTINEL,
        auth_connection: Union[
            McpServerConfigUpdateRequestModelAuthConnection, None
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = await AsyncMcpServersClient.update(
            self._client,
            mcp_server_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "approval_policy": approval_policy,
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "request_headers": request_headers,
                        "disable_compression": disable_compression,
                        "secret_token": secret_token,
                        "auth_connection": auth_connection,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, mcp_server_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = await AsyncMcpServersClient.delete(
            self._client, mcp_server_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
