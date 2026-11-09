from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyUpsertOrderItemV1ProductionsOrdersOrderIdItemsPost,
    HttpValidationError,
    RemoveOrderItemResponse,
    UpsertOrderItemRequest,
    UpsertOrderItemResponse,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class ItemsClient(BaseService):
    """
    Fern-style resource client for ItemsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._upsert_config: SdkConfig = {}
        self._remove_config: SdkConfig = {}

    def set_upsert_config(self, config: SdkConfig):
        """
        Sets method-level configuration for upsert.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._upsert_config = config
        return self

    def set_remove_config(self, config: SdkConfig):
        """
        Sets method-level configuration for remove.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._remove_config = config
        return self

    @property
    def with_raw_response(self) -> "RawItemsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawItemsClient(self)

    @cast_models
    def upsert(
        self,
        order_id: str,
        *,
        request: UpsertOrderItemRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> UpsertOrderItemResponse:
        """
        Adds or updates an order item on an open order. Returns the item ID and the quoted price.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request : UpsertOrderItemRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertOrderItemResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.items.upsert(
            order_id="prodorder_25fg4ia9atfzunn1ksao552dcm",
            request={
                "item": {
                    "kind": "dub",
                    "media_id": "prodmedia_fcje038bz1qi1l9zzvs1seiglh",
                    "source_language": "source_language",
                    "destination_languages": [
                        "destination_languages"
                    ],
                    "include_captions": False,
                    "include_source_captions": False,
                    "instructions": "instructions",
                    "captions_sdh": False
                },
                "item_id": "proditem_dqzjt90fyfyjvab26xp96f0zhr"
            },
        )
        """

        Validator(str).validate(order_id, "order_id")

        resolved_config = self._get_resolved_config(
            self._upsert_config, request_options
        )

        request_body = BodyUpsertOrderItemV1ProductionsOrdersOrderIdItemsPost(
            request=request
        )
        Validator(BodyUpsertOrderItemV1ProductionsOrdersOrderIdItemsPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/{{order_id}}/items",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("order_id", order_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                UpsertOrderItemResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(UpsertOrderItemResponse, response)
            )
        )

    @cast_models
    def remove(
        self,
        order_id: str,
        item_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> RemoveOrderItemResponse:
        """
        Removes an order item from an open order.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        item_id : str
            The ID of the order item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveOrderItemResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.items.remove(
            order_id="prodorder_r6rykg1lupzli4hfgspojdfno4",
            item_id="proditem_scx8zjb4wxlf9lkw9qcvweswxb",
        )
        """

        Validator(str).validate(order_id, "order_id")
        Validator(str).validate(item_id, "item_id")

        resolved_config = self._get_resolved_config(
            self._remove_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/{{order_id}}/items/{{item_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("order_id", order_id)
            .add_path("item_id", item_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                RemoveOrderItemResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(RemoveOrderItemResponse, response)
            )
        )


class RawItemsClient:
    """
    Raw-response client for ItemsClient.

    Each method delegates to the matching :class:`ItemsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ItemsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def upsert(
        self,
        order_id: str,
        *,
        request: UpsertOrderItemRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[UpsertOrderItemResponse]:
        data = ItemsClient.upsert(
            self._client, order_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def remove(
        self,
        order_id: str,
        item_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[RemoveOrderItemResponse]:
        data = ItemsClient.remove(
            self._client, order_id, item_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncItemsClient(ItemsClient):
    """
    Async wrapper for ItemsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawItemsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawItemsClient(self)

    def upsert(
        self,
        order_id: str,
        *,
        request: UpsertOrderItemRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[UpsertOrderItemResponse]:  # type: ignore[override]
        """
        Adds or updates an order item on an open order. Returns the item ID and the quoted price.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request : UpsertOrderItemRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertOrderItemResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.items.upsert(
                order_id="prodorder_25fg4ia9atfzunn1ksao552dcm",
                request={
                    "item": {
                        "kind": "dub",
                        "media_id": "prodmedia_fcje038bz1qi1l9zzvs1seiglh",
                        "source_language": "source_language",
                        "destination_languages": [
                            "destination_languages"
                        ],
                        "include_captions": False,
                        "include_source_captions": False,
                        "instructions": "instructions",
                        "captions_sdh": False
                    },
                    "item_id": "proditem_dqzjt90fyfyjvab26xp96f0zhr"
                },
            )


        asyncio.run(main())
        """
        return to_async(super().upsert)(
            order_id, request=request, request_options=request_options
        )

    def remove(
        self,
        order_id: str,
        item_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[RemoveOrderItemResponse]:  # type: ignore[override]
        """
        Removes an order item from an open order.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        item_id : str
            The ID of the order item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveOrderItemResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.items.remove(
                order_id="prodorder_r6rykg1lupzli4hfgspojdfno4",
                item_id="proditem_scx8zjb4wxlf9lkw9qcvweswxb",
            )


        asyncio.run(main())
        """
        return to_async(super().remove)(
            order_id, item_id, request_options=request_options
        )


class AsyncRawItemsClient:
    """
    Async raw-response client for AsyncItemsClient.
    """

    def __init__(self, client: AsyncItemsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def upsert(
        self,
        order_id: str,
        *,
        request: UpsertOrderItemRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[UpsertOrderItemResponse]:
        data = await AsyncItemsClient.upsert(
            self._client, order_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def remove(
        self,
        order_id: str,
        item_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[RemoveOrderItemResponse]:
        data = await AsyncItemsClient.remove(
            self._client, order_id, item_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
