from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import GetAgentEmbedResponseModel, HttpValidationError
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .avatar.client import (
        AvatarClient as _AvatarClient,
        AsyncAvatarClient as _AsyncAvatarClient,
    )


class WidgetClient(BaseService):
    """
    Fern-style resource client for WidgetClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._avatar: Any = None
        self._get_config: SdkConfig = {}

    @property
    def avatar(self) -> "_AvatarClient":
        """Lazily construct and return the avatar sub-resource client."""
        if self._avatar is None:
            from .avatar.client import AvatarClient

            _child = AvatarClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._avatar = _child
        return self._avatar

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
        if self._avatar is not None:
            self._avatar.set_base_url(base_url)

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
        if self._avatar is not None:
            self._avatar.set_config(config)

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
        if self._avatar is not None:
            self._avatar.set_timeout(timeout)

        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    @property
    def with_raw_response(self) -> "RawWidgetClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawWidgetClient(self)

    @cast_models
    def get(
        self,
        agent_id: str,
        *,
        conversation_signature: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetAgentEmbedResponseModel:
        """
        Retrieve the widget configuration for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        conversation_signature : typing.Optional[str]
            An expiring token that enables a websocket conversation to start. These can be generated for an agent using the /v1/convai/conversation/get_signed_url endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentEmbedResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.widget.get(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            conversation_signature="conversation_signature",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).is_optional().is_nullable().validate(
            conversation_signature, "conversation_signature"
        )

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/widget",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_query("conversation_signature", conversation_signature, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetAgentEmbedResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAgentEmbedResponseModel, response)
            )
        )


class RawWidgetClient:
    """
    Raw-response client for WidgetClient.

    Each method delegates to the matching :class:`WidgetClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: WidgetClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        agent_id: str,
        *,
        conversation_signature: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentEmbedResponseModel]:
        data = WidgetClient.get(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_signature": conversation_signature
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncWidgetClient(WidgetClient):
    """
    Async wrapper for WidgetClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def avatar(self) -> "_AsyncAvatarClient":
        """Lazily construct and return the async avatar sub-resource client."""
        if self._avatar is None:
            from .avatar.client import AsyncAvatarClient

            _child = AsyncAvatarClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._avatar = _child
        return self._avatar

    @property
    def with_raw_response(self) -> "AsyncRawWidgetClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawWidgetClient(self)

    def get(
        self,
        agent_id: str,
        *,
        conversation_signature: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetAgentEmbedResponseModel]:  # type: ignore[override]
        """
        Retrieve the widget configuration for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        conversation_signature : typing.Optional[str]
            An expiring token that enables a websocket conversation to start. These can be generated for an agent using the /v1/convai/conversation/get_signed_url endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentEmbedResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.widget.get(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                conversation_signature="conversation_signature",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_signature": conversation_signature
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawWidgetClient:
    """
    Async raw-response client for AsyncWidgetClient.
    """

    def __init__(self, client: AsyncWidgetClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        agent_id: str,
        *,
        conversation_signature: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentEmbedResponseModel]:
        data = await AsyncWidgetClient.get(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_signature": conversation_signature
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
