from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types.languages_response import LanguagesResponse_adapter
from ....types import HttpValidationError, LanguagesResponse, OrderItemKind
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class LanguagesClient(BaseService):
    """
    Fern-style resource client for LanguagesClient.
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
    def with_raw_response(self) -> "RawLanguagesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawLanguagesClient(self)

    @cast_models
    def list(
        self,
        order_item_kind: OrderItemKind,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> LanguagesResponse:
        """
        Returns the available languages for a given order item kind.

        Parameters
        ----------
        order_item_kind : OrderItemKind
            The kind of order item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LanguagesResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import OrderItemKind

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.languages.list(
            order_item_kind="dub",
        )
        """

        Validator(OrderItemKind).validate(order_item_kind, "order_item_kind")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/languages/{{order_item_kind}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("order_item_kind", order_item_kind)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                LanguagesResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(LanguagesResponse, response)
            )
        )


class RawLanguagesClient:
    """
    Raw-response client for LanguagesClient.

    Each method delegates to the matching :class:`LanguagesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: LanguagesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        order_item_kind: OrderItemKind,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[LanguagesResponse]:
        data = LanguagesClient.list(
            self._client, order_item_kind, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncLanguagesClient(LanguagesClient):
    """
    Async wrapper for LanguagesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawLanguagesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawLanguagesClient(self)

    def list(
        self,
        order_item_kind: OrderItemKind,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[LanguagesResponse]:  # type: ignore[override]
        """
        Returns the available languages for a given order item kind.

        Parameters
        ----------
        order_item_kind : OrderItemKind
            The kind of order item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LanguagesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import OrderItemKind

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.languages.list(
                order_item_kind="dub",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(order_item_kind, request_options=request_options)


class AsyncRawLanguagesClient:
    """
    Async raw-response client for AsyncLanguagesClient.
    """

    def __init__(self, client: AsyncLanguagesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        order_item_kind: OrderItemKind,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[LanguagesResponse]:
        data = await AsyncLanguagesClient.list(
            self._client, order_item_kind, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
