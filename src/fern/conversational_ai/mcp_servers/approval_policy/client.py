from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    HttpValidationError,
    McpApprovalPolicy,
    McpApprovalPolicyUpdateRequestModel,
    McpServerResponseModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class ApprovalPolicyClient(BaseService):
    """
    Fern-style resource client for ApprovalPolicyClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._update_config: SdkConfig = {}

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    @property
    def with_raw_response(self) -> "RawApprovalPolicyClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawApprovalPolicyClient(self)

    @cast_models
    def update(
        self,
        mcp_server_id: str,
        *,
        approval_policy: McpApprovalPolicy,
        request_options: Optional[RequestOptions] = None,
    ) -> McpServerResponseModel:
        """
        Update the approval policy configuration for an MCP server. DEPRECATED: Use PATCH /mcp-servers/{id} endpoint instead.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        approval_policy : McpApprovalPolicy
            Defines the MCP server-level approval policy for tool execution.

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
        client.conversational_ai.mcp_servers.approval_policy.update(
            mcp_server_id="mcp_server_id",
            approval_policy="auto_approve_all",
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = McpApprovalPolicyUpdateRequestModel(
            approval_policy=approval_policy
        )
        Validator(McpApprovalPolicyUpdateRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}/approval-policy",
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


class RawApprovalPolicyClient:
    """
    Raw-response client for ApprovalPolicyClient.

    Each method delegates to the matching :class:`ApprovalPolicyClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ApprovalPolicyClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def update(
        self,
        mcp_server_id: str,
        *,
        approval_policy: McpApprovalPolicy,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = ApprovalPolicyClient.update(
            self._client,
            mcp_server_id,
            approval_policy=approval_policy,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncApprovalPolicyClient(ApprovalPolicyClient):
    """
    Async wrapper for ApprovalPolicyClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawApprovalPolicyClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawApprovalPolicyClient(self)

    def update(
        self,
        mcp_server_id: str,
        *,
        approval_policy: McpApprovalPolicy,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[McpServerResponseModel]:  # type: ignore[override]
        """
        Update the approval policy configuration for an MCP server. DEPRECATED: Use PATCH /mcp-servers/{id} endpoint instead.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        approval_policy : McpApprovalPolicy
            Defines the MCP server-level approval policy for tool execution.

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
            await client.conversational_ai.mcp_servers.approval_policy.update(
                mcp_server_id="mcp_server_id",
                approval_policy="auto_approve_all",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            mcp_server_id,
            approval_policy=approval_policy,
            request_options=request_options,
        )


class AsyncRawApprovalPolicyClient:
    """
    Async raw-response client for AsyncApprovalPolicyClient.
    """

    def __init__(self, client: AsyncApprovalPolicyClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def update(
        self,
        mcp_server_id: str,
        *,
        approval_policy: McpApprovalPolicy,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[McpServerResponseModel]:
        data = await AsyncApprovalPolicyClient.update(
            self._client,
            mcp_server_id,
            approval_policy=approval_policy,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
