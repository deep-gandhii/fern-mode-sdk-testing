from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import GetLiveCountResponse, HttpValidationError
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class LiveCountClient(BaseService):
    """
    Fern-style resource client for LiveCountClient.
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
    def with_raw_response(self) -> "RawLiveCountClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawLiveCountClient(self)

    @cast_models
    def get(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetLiveCountResponse:
        """
        Get the live count of the ongoing conversations.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The id of an agent to restrict the analytics to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLiveCountResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.analytics.live_count.get(
            agent_id="agent_id",
        )
        """

        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/analytics/live-count",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("agent_id", agent_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetLiveCountResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetLiveCountResponse, response)
            )
        )


class RawLiveCountClient:
    """
    Raw-response client for LiveCountClient.

    Each method delegates to the matching :class:`LiveCountClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: LiveCountClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLiveCountResponse]:
        data = LiveCountClient.get(
            self._client,
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncLiveCountClient(LiveCountClient):
    """
    Async wrapper for LiveCountClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawLiveCountClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawLiveCountClient(self)

    def get(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetLiveCountResponse]:  # type: ignore[override]
        """
        Get the live count of the ongoing conversations.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The id of an agent to restrict the analytics to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLiveCountResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.analytics.live_count.get(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )


class AsyncRawLiveCountClient:
    """
    Async raw-response client for AsyncLiveCountClient.
    """

    def __init__(self, client: AsyncLiveCountClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLiveCountResponse]:
        data = await AsyncLiveCountClient.get(
            self._client,
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
