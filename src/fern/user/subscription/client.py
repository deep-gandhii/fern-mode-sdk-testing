from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import HttpValidationError, Subscription
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class SubscriptionClient(BaseService):
    """
    Fern-style resource client for SubscriptionClient.
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
    def with_raw_response(self) -> "RawSubscriptionClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSubscriptionClient(self)

    @cast_models
    def get(self, *, request_options: Optional[RequestOptions] = None) -> Subscription:
        """
        Gets extended information about the users subscription

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subscription
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.user.subscription.get()
        """

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/user/subscription",
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
                Subscription.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(Subscription, response)
            )
        )


class RawSubscriptionClient:
    """
    Raw-response client for SubscriptionClient.

    Each method delegates to the matching :class:`SubscriptionClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SubscriptionClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Subscription]:
        data = SubscriptionClient.get(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSubscriptionClient(SubscriptionClient):
    """
    Async wrapper for SubscriptionClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSubscriptionClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSubscriptionClient(self)

    def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Subscription]:  # type: ignore[override]
        """
        Gets extended information about the users subscription

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subscription
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.user.subscription.get()


        asyncio.run(main())
        """
        return to_async(super().get)(request_options=request_options)


class AsyncRawSubscriptionClient:
    """
    Async raw-response client for AsyncSubscriptionClient.
    """

    def __init__(self, client: AsyncSubscriptionClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Subscription]:
        data = await AsyncSubscriptionClient.get(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
