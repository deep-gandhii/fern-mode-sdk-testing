from typing import Any, Optional, Dict, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    DynamicVariableAssignment,
    HttpValidationError,
    McpServerResponseModel,
    McpToolConfigOverrideCreateRequestModel,
    McpToolConfigOverrideCreateRequestModelInputOverridesValue,
    McpToolConfigOverrideCreateRequestModelToolCallSound,
    McpToolConfigOverrideOutput,
    McpToolConfigOverrideUpdateRequestModel,
    McpToolConfigOverrideUpdateRequestModelInputOverridesValue,
    McpToolConfigOverrideUpdateRequestModelToolCallSound,
    PreToolSpeechMode,
    ToolCallSoundBehavior,
    ToolExecutionMode,
    ToolInterruptionMode,
    ToolResponseMockConfigInput,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class ToolConfigsClient(BaseService):
    """
    Fern-style resource client for ToolConfigsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

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
    def with_raw_response(self) -> "RawToolConfigsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawToolConfigsClient(self)

    @cast_models
    def create(
        self,
        mcp_server_id: str,
        *,
        tool_name: str,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Union[
            McpToolConfigOverrideCreateRequestModelToolCallSound, None
        ] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        assignments: Union[List[DynamicVariableAssignment], None] = SENTINEL,
        input_overrides: Union[
            Dict[str, McpToolConfigOverrideCreateRequestModelInputOverridesValue], None
        ] = SENTINEL,
        response_mocks: Union[List[ToolResponseMockConfigInput], None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> McpServerResponseModel:
        """
        Create configuration overrides for a specific MCP tool.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            The name of the MCP tool

        force_pre_tool_speech : typing.Optional[bool]
            DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool.

        pre_tool_speech : typing.Optional[PreToolSpeechMode]
            If set, overrides the server's pre_tool_speech setting for this tool.

        disable_interruptions : typing.Optional[bool]
            DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool.

        interruption_mode : typing.Optional[ToolInterruptionMode]
            If set, overrides the server's interruption_mode setting for this tool.

        tool_call_sound : typing.Optional[McpToolConfigOverrideCreateRequestModelToolCallSound]
            Overrides the server's tool_call_sound setting for this tool. A sound name plays that sound; 'off' overrides to no sound (silence); null means do not override (inherit the server default).

        tool_call_sound_behavior : typing.Optional[ToolCallSoundBehavior]
            If set, overrides the server's tool_call_sound_behavior setting for this tool

        execution_mode : typing.Optional[ToolExecutionMode]
            If set, overrides the server's execution_mode setting for this tool

        response_timeout_secs : typing.Optional[int]
            If set, overrides the server's response timeout for this MCP tool.

        assignments : typing.Optional[typing.Sequence[DynamicVariableAssignment]]
            Dynamic variable assignments for this MCP tool

        input_overrides : typing.Optional[typing.Dict[str, McpToolConfigOverrideCreateRequestModelInputOverridesValue]]
            Mapping of json path to input override configuration

        response_mocks : typing.Optional[typing.Sequence[ToolResponseMockConfigInput]]
            Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.

        environment : typing.Optional[str]
            Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

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
        client.conversational_ai.mcp_servers.tool_configs.create(
            mcp_server_id="mcp_server_id",
            environment="production",
            pre_tool_speech="auto",
            interruption_mode="allow",
            tool_call_sound="typing",
            tool_call_sound_behavior="auto",
            execution_mode="immediate",
            response_timeout_secs=39,
            assignments=[
                {
                    "source": "response",
                    "dynamic_variable": "dynamic_variable",
                    "value_path": "value_path",
                    "sanitize": True,
                    "preserve_native_type": True
                }
            ],
            input_overrides={},
            response_mocks=[
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
            ],
            tool_name="tool_name",
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")
        Validator(str).is_optional().is_nullable().validate(environment, "environment")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = McpToolConfigOverrideCreateRequestModel(
            tool_name=tool_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "assignments": assignments,
                        "input_overrides": input_overrides,
                        "response_mocks": response_mocks,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(McpToolConfigOverrideCreateRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}/tool-configs",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
            .add_query("environment", environment, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
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
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> McpToolConfigOverrideOutput:
        """
        Retrieve configuration overrides for a specific MCP tool.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            Name of the MCP tool to retrieve config overrides for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpToolConfigOverrideOutput
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.mcp_servers.tool_configs.get(
            mcp_server_id="mcp_server_id",
            tool_name="tool_name",
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")
        Validator(str).validate(tool_name, "tool_name")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}/tool-configs/{{tool_name}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
            .add_path("tool_name", tool_name)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                McpToolConfigOverrideOutput.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(McpToolConfigOverrideOutput, response)
            )
        )

    @cast_models
    def update(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Union[
            McpToolConfigOverrideUpdateRequestModelToolCallSound, None
        ] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        assignments: Union[List[DynamicVariableAssignment], None] = SENTINEL,
        input_overrides: Union[
            Dict[str, McpToolConfigOverrideUpdateRequestModelInputOverridesValue], None
        ] = SENTINEL,
        response_mocks: Union[List[ToolResponseMockConfigInput], None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> McpServerResponseModel:
        """
        Update configuration overrides for a specific MCP tool.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            Name of the MCP tool to update config overrides for.

        force_pre_tool_speech : typing.Optional[bool]
            DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool.

        pre_tool_speech : typing.Optional[PreToolSpeechMode]
            If set, overrides the server's pre_tool_speech setting for this tool.

        disable_interruptions : typing.Optional[bool]
            DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool.

        interruption_mode : typing.Optional[ToolInterruptionMode]
            If set, overrides the server's interruption_mode setting for this tool.

        tool_call_sound : typing.Optional[McpToolConfigOverrideUpdateRequestModelToolCallSound]
            Overrides the server's tool_call_sound setting for this tool. A sound name plays that sound; 'off' overrides to no sound (silence); null means do not override (inherit the server default).

        tool_call_sound_behavior : typing.Optional[ToolCallSoundBehavior]
            If set, overrides the server's tool_call_sound_behavior setting for this tool

        execution_mode : typing.Optional[ToolExecutionMode]
            If set, overrides the server's execution_mode setting for this tool

        response_timeout_secs : typing.Optional[int]
            If set, overrides the server's response timeout for this MCP tool.

        assignments : typing.Optional[typing.Sequence[DynamicVariableAssignment]]
            Dynamic variable assignments for this MCP tool

        input_overrides : typing.Optional[typing.Dict[str, McpToolConfigOverrideUpdateRequestModelInputOverridesValue]]
            Mapping of json path to input override configuration

        response_mocks : typing.Optional[typing.Sequence[ToolResponseMockConfigInput]]
            Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.

        environment : typing.Optional[str]
            Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

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
        client.conversational_ai.mcp_servers.tool_configs.update(
            mcp_server_id="mcp_server_id",
            tool_name="tool_name",
            environment="production",
            pre_tool_speech="auto",
            interruption_mode="allow",
            tool_call_sound="typing",
            tool_call_sound_behavior="auto",
            execution_mode="immediate",
            response_timeout_secs=55,
            assignments=[
                {
                    "source": "response",
                    "dynamic_variable": "dynamic_variable",
                    "value_path": "value_path",
                    "sanitize": True,
                    "preserve_native_type": True
                }
            ],
            input_overrides={},
            response_mocks=[
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
            ],
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")
        Validator(str).validate(tool_name, "tool_name")
        Validator(str).is_optional().is_nullable().validate(environment, "environment")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = McpToolConfigOverrideUpdateRequestModel(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "assignments": assignments,
                        "input_overrides": input_overrides,
                        "response_mocks": response_mocks,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(McpToolConfigOverrideUpdateRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}/tool-configs/{{tool_name}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
            .add_path("tool_name", tool_name)
            .add_query("environment", environment, nullable=True)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
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
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> McpServerResponseModel:
        """
        Remove configuration overrides for a specific MCP tool.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            Name of the MCP tool to remove config overrides for.

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
        client.conversational_ai.mcp_servers.tool_configs.delete(
            mcp_server_id="mcp_server_id",
            tool_name="tool_name",
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")
        Validator(str).validate(tool_name, "tool_name")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}/tool-configs/{{tool_name}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
            .add_path("tool_name", tool_name)
            .serialize()
            .set_method("DELETE")
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


class RawToolConfigsClient:
    """
    Raw-response client for ToolConfigsClient.

    Each method delegates to the matching :class:`ToolConfigsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ToolConfigsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        mcp_server_id: str,
        *,
        tool_name: str,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Union[
            McpToolConfigOverrideCreateRequestModelToolCallSound, None
        ] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        assignments: Union[List[DynamicVariableAssignment], None] = SENTINEL,
        input_overrides: Union[
            Dict[str, McpToolConfigOverrideCreateRequestModelInputOverridesValue], None
        ] = SENTINEL,
        response_mocks: Union[List[ToolResponseMockConfigInput], None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = ToolConfigsClient.create(
            self._client,
            mcp_server_id,
            tool_name=tool_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "assignments": assignments,
                        "input_overrides": input_overrides,
                        "response_mocks": response_mocks,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpToolConfigOverrideOutput]:
        data = ToolConfigsClient.get(
            self._client, mcp_server_id, tool_name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Union[
            McpToolConfigOverrideUpdateRequestModelToolCallSound, None
        ] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        assignments: Union[List[DynamicVariableAssignment], None] = SENTINEL,
        input_overrides: Union[
            Dict[str, McpToolConfigOverrideUpdateRequestModelInputOverridesValue], None
        ] = SENTINEL,
        response_mocks: Union[List[ToolResponseMockConfigInput], None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = ToolConfigsClient.update(
            self._client,
            mcp_server_id,
            tool_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "assignments": assignments,
                        "input_overrides": input_overrides,
                        "response_mocks": response_mocks,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = ToolConfigsClient.delete(
            self._client, mcp_server_id, tool_name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncToolConfigsClient(ToolConfigsClient):
    """
    Async wrapper for ToolConfigsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawToolConfigsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawToolConfigsClient(self)

    def create(
        self,
        mcp_server_id: str,
        *,
        tool_name: str,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Union[
            McpToolConfigOverrideCreateRequestModelToolCallSound, None
        ] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        assignments: Union[List[DynamicVariableAssignment], None] = SENTINEL,
        input_overrides: Union[
            Dict[str, McpToolConfigOverrideCreateRequestModelInputOverridesValue], None
        ] = SENTINEL,
        response_mocks: Union[List[ToolResponseMockConfigInput], None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[McpServerResponseModel]:  # type: ignore[override]
        """
        Create configuration overrides for a specific MCP tool.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            The name of the MCP tool

        force_pre_tool_speech : typing.Optional[bool]
            DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool.

        pre_tool_speech : typing.Optional[PreToolSpeechMode]
            If set, overrides the server's pre_tool_speech setting for this tool.

        disable_interruptions : typing.Optional[bool]
            DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool.

        interruption_mode : typing.Optional[ToolInterruptionMode]
            If set, overrides the server's interruption_mode setting for this tool.

        tool_call_sound : typing.Optional[McpToolConfigOverrideCreateRequestModelToolCallSound]
            Overrides the server's tool_call_sound setting for this tool. A sound name plays that sound; 'off' overrides to no sound (silence); null means do not override (inherit the server default).

        tool_call_sound_behavior : typing.Optional[ToolCallSoundBehavior]
            If set, overrides the server's tool_call_sound_behavior setting for this tool

        execution_mode : typing.Optional[ToolExecutionMode]
            If set, overrides the server's execution_mode setting for this tool

        response_timeout_secs : typing.Optional[int]
            If set, overrides the server's response timeout for this MCP tool.

        assignments : typing.Optional[typing.Sequence[DynamicVariableAssignment]]
            Dynamic variable assignments for this MCP tool

        input_overrides : typing.Optional[typing.Dict[str, McpToolConfigOverrideCreateRequestModelInputOverridesValue]]
            Mapping of json path to input override configuration

        response_mocks : typing.Optional[typing.Sequence[ToolResponseMockConfigInput]]
            Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.

        environment : typing.Optional[str]
            Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

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
            await client.conversational_ai.mcp_servers.tool_configs.create(
                mcp_server_id="mcp_server_id",
                environment="production",
                pre_tool_speech="auto",
                interruption_mode="allow",
                tool_call_sound="typing",
                tool_call_sound_behavior="auto",
                execution_mode="immediate",
                response_timeout_secs=39,
                assignments=[
                    {
                        "source": "response",
                        "dynamic_variable": "dynamic_variable",
                        "value_path": "value_path",
                        "sanitize": True,
                        "preserve_native_type": True
                    }
                ],
                input_overrides={},
                response_mocks=[
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
                ],
                tool_name="tool_name",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            mcp_server_id,
            tool_name=tool_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "assignments": assignments,
                        "input_overrides": input_overrides,
                        "response_mocks": response_mocks,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[McpToolConfigOverrideOutput]:  # type: ignore[override]
        """
        Retrieve configuration overrides for a specific MCP tool.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            Name of the MCP tool to retrieve config overrides for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpToolConfigOverrideOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.mcp_servers.tool_configs.get(
                mcp_server_id="mcp_server_id",
                tool_name="tool_name",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            mcp_server_id, tool_name, request_options=request_options
        )

    def update(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Union[
            McpToolConfigOverrideUpdateRequestModelToolCallSound, None
        ] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        assignments: Union[List[DynamicVariableAssignment], None] = SENTINEL,
        input_overrides: Union[
            Dict[str, McpToolConfigOverrideUpdateRequestModelInputOverridesValue], None
        ] = SENTINEL,
        response_mocks: Union[List[ToolResponseMockConfigInput], None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[McpServerResponseModel]:  # type: ignore[override]
        """
        Update configuration overrides for a specific MCP tool.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            Name of the MCP tool to update config overrides for.

        force_pre_tool_speech : typing.Optional[bool]
            DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool.

        pre_tool_speech : typing.Optional[PreToolSpeechMode]
            If set, overrides the server's pre_tool_speech setting for this tool.

        disable_interruptions : typing.Optional[bool]
            DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool.

        interruption_mode : typing.Optional[ToolInterruptionMode]
            If set, overrides the server's interruption_mode setting for this tool.

        tool_call_sound : typing.Optional[McpToolConfigOverrideUpdateRequestModelToolCallSound]
            Overrides the server's tool_call_sound setting for this tool. A sound name plays that sound; 'off' overrides to no sound (silence); null means do not override (inherit the server default).

        tool_call_sound_behavior : typing.Optional[ToolCallSoundBehavior]
            If set, overrides the server's tool_call_sound_behavior setting for this tool

        execution_mode : typing.Optional[ToolExecutionMode]
            If set, overrides the server's execution_mode setting for this tool

        response_timeout_secs : typing.Optional[int]
            If set, overrides the server's response timeout for this MCP tool.

        assignments : typing.Optional[typing.Sequence[DynamicVariableAssignment]]
            Dynamic variable assignments for this MCP tool

        input_overrides : typing.Optional[typing.Dict[str, McpToolConfigOverrideUpdateRequestModelInputOverridesValue]]
            Mapping of json path to input override configuration

        response_mocks : typing.Optional[typing.Sequence[ToolResponseMockConfigInput]]
            Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.

        environment : typing.Optional[str]
            Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

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
            await client.conversational_ai.mcp_servers.tool_configs.update(
                mcp_server_id="mcp_server_id",
                tool_name="tool_name",
                environment="production",
                pre_tool_speech="auto",
                interruption_mode="allow",
                tool_call_sound="typing",
                tool_call_sound_behavior="auto",
                execution_mode="immediate",
                response_timeout_secs=55,
                assignments=[
                    {
                        "source": "response",
                        "dynamic_variable": "dynamic_variable",
                        "value_path": "value_path",
                        "sanitize": True,
                        "preserve_native_type": True
                    }
                ],
                input_overrides={},
                response_mocks=[
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
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            mcp_server_id,
            tool_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "assignments": assignments,
                        "input_overrides": input_overrides,
                        "response_mocks": response_mocks,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[McpServerResponseModel]:  # type: ignore[override]
        """
        Remove configuration overrides for a specific MCP tool.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            Name of the MCP tool to remove config overrides for.

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
            await client.conversational_ai.mcp_servers.tool_configs.delete(
                mcp_server_id="mcp_server_id",
                tool_name="tool_name",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            mcp_server_id, tool_name, request_options=request_options
        )


class AsyncRawToolConfigsClient:
    """
    Async raw-response client for AsyncToolConfigsClient.
    """

    def __init__(self, client: AsyncToolConfigsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        mcp_server_id: str,
        *,
        tool_name: str,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Union[
            McpToolConfigOverrideCreateRequestModelToolCallSound, None
        ] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        assignments: Union[List[DynamicVariableAssignment], None] = SENTINEL,
        input_overrides: Union[
            Dict[str, McpToolConfigOverrideCreateRequestModelInputOverridesValue], None
        ] = SENTINEL,
        response_mocks: Union[List[ToolResponseMockConfigInput], None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = await AsyncToolConfigsClient.create(
            self._client,
            mcp_server_id,
            tool_name=tool_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "assignments": assignments,
                        "input_overrides": input_overrides,
                        "response_mocks": response_mocks,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpToolConfigOverrideOutput]:
        data = await AsyncToolConfigsClient.get(
            self._client, mcp_server_id, tool_name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        force_pre_tool_speech: Union[bool, None] = SENTINEL,
        pre_tool_speech: Optional[PreToolSpeechMode] = SENTINEL,
        disable_interruptions: Union[bool, None] = SENTINEL,
        interruption_mode: Optional[ToolInterruptionMode] = SENTINEL,
        tool_call_sound: Union[
            McpToolConfigOverrideUpdateRequestModelToolCallSound, None
        ] = SENTINEL,
        tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = SENTINEL,
        execution_mode: Optional[ToolExecutionMode] = SENTINEL,
        response_timeout_secs: Union[int, None] = SENTINEL,
        assignments: Union[List[DynamicVariableAssignment], None] = SENTINEL,
        input_overrides: Union[
            Dict[str, McpToolConfigOverrideUpdateRequestModelInputOverridesValue], None
        ] = SENTINEL,
        response_mocks: Union[List[ToolResponseMockConfigInput], None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = await AsyncToolConfigsClient.update(
            self._client,
            mcp_server_id,
            tool_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "force_pre_tool_speech": force_pre_tool_speech,
                        "pre_tool_speech": pre_tool_speech,
                        "disable_interruptions": disable_interruptions,
                        "interruption_mode": interruption_mode,
                        "tool_call_sound": tool_call_sound,
                        "tool_call_sound_behavior": tool_call_sound_behavior,
                        "execution_mode": execution_mode,
                        "response_timeout_secs": response_timeout_secs,
                        "assignments": assignments,
                        "input_overrides": input_overrides,
                        "response_mocks": response_mocks,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = await AsyncToolConfigsClient.delete(
            self._client, mcp_server_id, tool_name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
