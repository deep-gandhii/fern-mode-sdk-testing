from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import HttpValidationError, ListMcpToolsResponseModel
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class ToolsClient(BaseService):
    """
    Fern-style resource client for ToolsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    @property
    def with_raw_response(self) -> "RawToolsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawToolsClient(self)

    @cast_models
    def list(
        self,
        mcp_server_id: str,
        *,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ListMcpToolsResponseModel:
        """
        Retrieve all tools available for a specific MCP server configuration.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        environment : typing.Optional[str]
            Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMcpToolsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.mcp_servers.tools.list(
            mcp_server_id="mcp_server_id",
            environment="production",
        )
        """

        Validator(str).validate(mcp_server_id, "mcp_server_id")
        Validator(str).is_optional().is_nullable().validate(environment, "environment")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/mcp-servers/{{mcp_server_id}}/tools",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("mcp_server_id", mcp_server_id)
            .add_query("environment", environment, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListMcpToolsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListMcpToolsResponseModel, response)
            )
        )


class RawToolsClient:
    """
    Raw-response client for ToolsClient.

    Each method delegates to the matching :class:`ToolsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ToolsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        mcp_server_id: str,
        *,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMcpToolsResponseModel]:
        data = ToolsClient.list(
            self._client,
            mcp_server_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"environment": environment}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncToolsClient(ToolsClient):
    """
    Async wrapper for ToolsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawToolsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawToolsClient(self)

    def list(
        self,
        mcp_server_id: str,
        *,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListMcpToolsResponseModel]:  # type: ignore[override]
        """
        Retrieve all tools available for a specific MCP server configuration.

        Parameters
        ----------
        mcp_server_id : str
            ID of the MCP Server.

        environment : typing.Optional[str]
            Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMcpToolsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.mcp_servers.tools.list(
                mcp_server_id="mcp_server_id",
                environment="production",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            mcp_server_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"environment": environment}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawToolsClient:
    """
    Async raw-response client for AsyncToolsClient.
    """

    def __init__(self, client: AsyncToolsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        mcp_server_id: str,
        *,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMcpToolsResponseModel]:
        data = await AsyncToolsClient.list(
            self._client,
            mcp_server_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"environment": environment}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
