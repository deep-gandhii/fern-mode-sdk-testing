from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import HttpValidationError, User
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .subscription.client import (
        SubscriptionClient as _SubscriptionClient,
        AsyncSubscriptionClient as _AsyncSubscriptionClient,
    )


class UserClient(BaseService):
    """
    Fern-style resource client for UserClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._subscription: Any = None
        self._get_config: SdkConfig = {}

    @property
    def subscription(self) -> "_SubscriptionClient":
        """Lazily construct and return the subscription sub-resource client."""
        if self._subscription is None:
            from .subscription.client import SubscriptionClient

            _child = SubscriptionClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._subscription = _child
        return self._subscription

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
        if self._subscription is not None:
            self._subscription.set_base_url(base_url)

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
        if self._subscription is not None:
            self._subscription.set_config(config)

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
        if self._subscription is not None:
            self._subscription.set_timeout(timeout)

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
    def with_raw_response(self) -> "RawUserClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawUserClient(self)

    @cast_models
    def get(self, *, request_options: Optional[RequestOptions] = None) -> User:
        """
        Gets information about the user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.user.get()
        """

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/user",
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
                User.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(User, response)
            )
        )


class RawUserClient:
    """
    Raw-response client for UserClient.

    Each method delegates to the matching :class:`UserClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: UserClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        data = UserClient.get(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncUserClient(UserClient):
    """
    Async wrapper for UserClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def subscription(self) -> "_AsyncSubscriptionClient":
        """Lazily construct and return the async subscription sub-resource client."""
        if self._subscription is None:
            from .subscription.client import AsyncSubscriptionClient

            _child = AsyncSubscriptionClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._subscription = _child
        return self._subscription

    @property
    def with_raw_response(self) -> "AsyncRawUserClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawUserClient(self)

    def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[User]:  # type: ignore[override]
        """
        Gets information about the user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.user.get()


        asyncio.run(main())
        """
        return to_async(super().get)(request_options=request_options)


class AsyncRawUserClient:
    """
    Async raw-response client for AsyncUserClient.
    """

    def __init__(self, client: AsyncUserClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        data = await AsyncUserClient.get(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)
