from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    HttpValidationError,
    McpServerResponseModel,
    McpToolAddApprovalRequestModel,
    McpToolApprovalPolicy,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class ToolApprovalsClient(BaseService):
    """
    Fern-style resource client for ToolApprovalsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
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
    def with_raw_response(self) -> "RawToolApprovalsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawToolApprovalsClient(self)

    @cast_models
    def create(
        self,
        mcp_server_id: str,
        *,
        tool_name: str,
        tool_description: str,
        input_schema: Optional[dict] = SENTINEL,
        approval_policy: Optional[McpToolApprovalPolicy] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> McpServerResponseModel:
        """
        Add approval for a specific MCP tool when using per-tool approval mode.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            The name of the MCP tool

        tool_description : str
            The description of the MCP tool

        input_schema : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The input schema of the MCP tool (the schema defined on the MCP server before ElevenLabs does any extra processing)

        approval_policy : typing.Optional[McpToolApprovalPolicy]
            Defines the tool-level approval policy.

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
        client.conversational_ai.mcp_servers.tool_approvals.create(
            mcp_server_id="mcp_server_id",
            tool_name="tool_name",
            tool_description="tool_description",
            input_schema={},
            approval_policy="auto_approved",
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = McpToolAddApprovalRequestModel(
            tool_name=tool_name,
            tool_description=tool_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "input_schema": input_schema,
                        "approval_policy": approval_policy,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(McpToolAddApprovalRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}/tool-approvals",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
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
    def delete(
        self,
        mcp_server_id: str,
        tool_name: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> McpServerResponseModel:
        """
        Remove approval for a specific MCP tool when using per-tool approval mode.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            Name of the MCP tool to remove approval for.

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
        client.conversational_ai.mcp_servers.tool_approvals.delete(
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
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}/tool-approvals/{{tool_name}}",
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


class RawToolApprovalsClient:
    """
    Raw-response client for ToolApprovalsClient.

    Each method delegates to the matching :class:`ToolApprovalsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ToolApprovalsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        mcp_server_id: str,
        *,
        tool_name: str,
        tool_description: str,
        input_schema: Optional[dict] = SENTINEL,
        approval_policy: Optional[McpToolApprovalPolicy] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = ToolApprovalsClient.create(
            self._client,
            mcp_server_id,
            tool_name=tool_name,
            tool_description=tool_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "input_schema": input_schema,
                        "approval_policy": approval_policy,
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
        data = ToolApprovalsClient.delete(
            self._client, mcp_server_id, tool_name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncToolApprovalsClient(ToolApprovalsClient):
    """
    Async wrapper for ToolApprovalsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawToolApprovalsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawToolApprovalsClient(self)

    def create(
        self,
        mcp_server_id: str,
        *,
        tool_name: str,
        tool_description: str,
        input_schema: Optional[dict] = SENTINEL,
        approval_policy: Optional[McpToolApprovalPolicy] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[McpServerResponseModel]:  # type: ignore[override]
        """
        Add approval for a specific MCP tool when using per-tool approval mode.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            The name of the MCP tool

        tool_description : str
            The description of the MCP tool

        input_schema : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The input schema of the MCP tool (the schema defined on the MCP server before ElevenLabs does any extra processing)

        approval_policy : typing.Optional[McpToolApprovalPolicy]
            Defines the tool-level approval policy.

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
            await client.conversational_ai.mcp_servers.tool_approvals.create(
                mcp_server_id="mcp_server_id",
                tool_name="tool_name",
                tool_description="tool_description",
                input_schema={},
                approval_policy="auto_approved",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            mcp_server_id,
            tool_name=tool_name,
            tool_description=tool_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "input_schema": input_schema,
                        "approval_policy": approval_policy,
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
        Remove approval for a specific MCP tool when using per-tool approval mode.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        tool_name : str
            Name of the MCP tool to remove approval for.

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
            await client.conversational_ai.mcp_servers.tool_approvals.delete(
                mcp_server_id="mcp_server_id",
                tool_name="tool_name",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            mcp_server_id, tool_name, request_options=request_options
        )


class AsyncRawToolApprovalsClient:
    """
    Async raw-response client for AsyncToolApprovalsClient.
    """

    def __init__(self, client: AsyncToolApprovalsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        mcp_server_id: str,
        *,
        tool_name: str,
        tool_description: str,
        input_schema: Optional[dict] = SENTINEL,
        approval_policy: Optional[McpToolApprovalPolicy] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = await AsyncToolApprovalsClient.create(
            self._client,
            mcp_server_id,
            tool_name=tool_name,
            tool_description=tool_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "input_schema": input_schema,
                        "approval_policy": approval_policy,
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
        data = await AsyncToolApprovalsClient.delete(
            self._client, mcp_server_id, tool_name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
