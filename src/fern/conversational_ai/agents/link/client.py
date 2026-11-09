from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import GetAgentLinkResponseModel, HttpValidationError
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class LinkClient(BaseService):
    """
    Fern-style resource client for LinkClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    @property
    def with_raw_response(self) -> "RawLinkClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawLinkClient(self)

    @cast_models
    def get(
        self, agent_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetAgentLinkResponseModel:
        """
        Get the current link used to share the agent with others

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentLinkResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.link.get(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/link",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetAgentLinkResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAgentLinkResponseModel, response)
            )
        )


class RawLinkClient:
    """
    Raw-response client for LinkClient.

    Each method delegates to the matching :class:`LinkClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: LinkClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self, agent_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentLinkResponseModel]:
        data = LinkClient.get(self._client, agent_id, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncLinkClient(LinkClient):
    """
    Async wrapper for LinkClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawLinkClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawLinkClient(self)

    def get(
        self, agent_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetAgentLinkResponseModel]:  # type: ignore[override]
        """
        Get the current link used to share the agent with others

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentLinkResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.link.get(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(agent_id, request_options=request_options)


class AsyncRawLinkClient:
    """
    Async raw-response client for AsyncLinkClient.
    """

    def __init__(self, client: AsyncLinkClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, agent_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentLinkResponseModel]:
        data = await AsyncLinkClient.get(
            self._client, agent_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
