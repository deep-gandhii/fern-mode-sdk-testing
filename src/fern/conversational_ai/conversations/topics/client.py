from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import GetAgentTopicsResponseModel, HttpValidationError
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class TopicsClient(BaseService):
    """
    Fern-style resource client for TopicsClient.
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
    def with_raw_response(self) -> "RawTopicsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTopicsClient(self)

    @cast_models
    def get(
        self,
        agent_id: str,
        *,
        from_unix_secs: Union[int, None] = SENTINEL,
        to_unix_secs: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetAgentTopicsResponseModel:
        """
        Returns the latest topic discovery run results for a given agent.

        Parameters
        ----------
        agent_id : str
            ID of the agent

        from_unix_secs : typing.Optional[int]
            Start of the window to view topics for. When set with to_unix_secs, per-day topics in the range are aggregated together.

        to_unix_secs : typing.Optional[int]
            End of the window to view topics for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentTopicsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.topics.get(
            agent_id="agent_id",
            from_unix_secs=1,
            to_unix_secs=1,
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(int).is_optional().is_nullable().validate(
            from_unix_secs, "from_unix_secs"
        )
        Validator(int).is_optional().is_nullable().validate(
            to_unix_secs, "to_unix_secs"
        )

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/topics",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_query("from_unix_secs", from_unix_secs, nullable=True)
            .add_query("to_unix_secs", to_unix_secs, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetAgentTopicsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAgentTopicsResponseModel, response)
            )
        )


class RawTopicsClient:
    """
    Raw-response client for TopicsClient.

    Each method delegates to the matching :class:`TopicsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TopicsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        agent_id: str,
        *,
        from_unix_secs: Union[int, None] = SENTINEL,
        to_unix_secs: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentTopicsResponseModel]:
        data = TopicsClient.get(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "from_unix_secs": from_unix_secs,
                        "to_unix_secs": to_unix_secs,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncTopicsClient(TopicsClient):
    """
    Async wrapper for TopicsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawTopicsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTopicsClient(self)

    def get(
        self,
        agent_id: str,
        *,
        from_unix_secs: Union[int, None] = SENTINEL,
        to_unix_secs: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetAgentTopicsResponseModel]:  # type: ignore[override]
        """
        Returns the latest topic discovery run results for a given agent.

        Parameters
        ----------
        agent_id : str
            ID of the agent

        from_unix_secs : typing.Optional[int]
            Start of the window to view topics for. When set with to_unix_secs, per-day topics in the range are aggregated together.

        to_unix_secs : typing.Optional[int]
            End of the window to view topics for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentTopicsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.topics.get(
                agent_id="agent_id",
                from_unix_secs=1,
                to_unix_secs=1,
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "from_unix_secs": from_unix_secs,
                        "to_unix_secs": to_unix_secs,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawTopicsClient:
    """
    Async raw-response client for AsyncTopicsClient.
    """

    def __init__(self, client: AsyncTopicsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        agent_id: str,
        *,
        from_unix_secs: Union[int, None] = SENTINEL,
        to_unix_secs: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentTopicsResponseModel]:
        data = await AsyncTopicsClient.get(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "from_unix_secs": from_unix_secs,
                        "to_unix_secs": to_unix_secs,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
