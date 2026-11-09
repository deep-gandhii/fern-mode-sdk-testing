from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyUpdateOrderV1ProductionsOrdersOrderIdPatch,
    CreateOrderRequest,
    CreateOrderResponse,
    HttpValidationError,
    ListOrdersResponse,
    OrderRequestState,
    OrderResponse,
    SubmitOrderResponse,
    UpdateOrderRequest,
    UpdateOrderResponse,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .media.client import (
        MediaClient as _MediaClient,
        AsyncMediaClient as _AsyncMediaClient,
    )
    from .items.client import (
        ItemsClient as _ItemsClient,
        AsyncItemsClient as _AsyncItemsClient,
    )
    from .deliverables.client import (
        DeliverablesClient as _DeliverablesClient,
        AsyncDeliverablesClient as _AsyncDeliverablesClient,
    )
    from .languages.client import (
        LanguagesClient as _LanguagesClient,
        AsyncLanguagesClient as _AsyncLanguagesClient,
    )


class OrdersClient(BaseService):
    """
    Fern-style resource client for OrdersClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._media: Any = None
        self._items: Any = None
        self._deliverables: Any = None
        self._languages: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._submit_config: SdkConfig = {}

    @property
    def media(self) -> "_MediaClient":
        """Lazily construct and return the media sub-resource client."""
        if self._media is None:
            from .media.client import MediaClient

            _child = MediaClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._media = _child
        return self._media

    @property
    def items(self) -> "_ItemsClient":
        """Lazily construct and return the items sub-resource client."""
        if self._items is None:
            from .items.client import ItemsClient

            _child = ItemsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._items = _child
        return self._items

    @property
    def deliverables(self) -> "_DeliverablesClient":
        """Lazily construct and return the deliverables sub-resource client."""
        if self._deliverables is None:
            from .deliverables.client import DeliverablesClient

            _child = DeliverablesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._deliverables = _child
        return self._deliverables

    @property
    def languages(self) -> "_LanguagesClient":
        """Lazily construct and return the languages sub-resource client."""
        if self._languages is None:
            from .languages.client import LanguagesClient

            _child = LanguagesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._languages = _child
        return self._languages

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
        if self._media is not None:
            self._media.set_base_url(base_url)
        if self._items is not None:
            self._items.set_base_url(base_url)
        if self._deliverables is not None:
            self._deliverables.set_base_url(base_url)
        if self._languages is not None:
            self._languages.set_base_url(base_url)

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
        if self._media is not None:
            self._media.set_config(config)
        if self._items is not None:
            self._items.set_config(config)
        if self._deliverables is not None:
            self._deliverables.set_config(config)
        if self._languages is not None:
            self._languages.set_config(config)

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
        if self._media is not None:
            self._media.set_timeout(timeout)
        if self._items is not None:
            self._items.set_timeout(timeout)
        if self._deliverables is not None:
            self._deliverables.set_timeout(timeout)
        if self._languages is not None:
            self._languages.set_timeout(timeout)

        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_submit_config(self, config: SdkConfig):
        """
        Sets method-level configuration for submit.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._submit_config = config
        return self

    @property
    def with_raw_response(self) -> "RawOrdersClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawOrdersClient(self)

    @cast_models
    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        offset: Union[int, None] = SENTINEL,
        status: Union[List[OrderRequestState], None] = SENTINEL,
        start_date: Union[str, None] = SENTINEL,
        end_date: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ListOrdersResponse:
        """
        Lists Productions orders in the workspace. Supports filtering by status and date range, with pagination.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Maximum number of orders to return per page.

        offset : typing.Optional[int]
            Number of orders to skip for pagination.

        status : typing.Optional[typing.Sequence[OrderRequestState]]
            Filter orders by one or more statuses.

        start_date : typing.Optional[str]
            Filter orders created on or after this date.

        end_date : typing.Optional[str]
            Filter orders created on or before this date.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrdersResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.list(
            page_size=20,
            offset=10,
            status=[
                "open"
            ],
            start_date="2023-07-20T21:03:51.582Z",
            end_date="2023-07-20T21:03:51.582Z",
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(int).is_optional().is_nullable().validate(offset, "offset")
        Validator(OrderRequestState).is_array().is_optional().is_nullable().validate(
            status, "status"
        )
        Validator(str).is_optional().is_nullable().validate(start_date, "start_date")
        Validator(str).is_optional().is_nullable().validate(end_date, "end_date")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("page_size", page_size, nullable=True)
            .add_query("offset", offset, nullable=True)
            .add_query("status", status, nullable=True)
            .add_query("start_date", start_date, nullable=True)
            .add_query("end_date", end_date, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListOrdersResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListOrdersResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        request: CreateOrderRequest = None,
        request_options: Optional[RequestOptions] = None,
    ) -> CreateOrderResponse:
        """
        Creates a new Productions order in the workspace. The order starts in the open state and can be configured with items before submission.

        Parameters
        ----------
        request : typing.Optional[CreateOrderRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateOrderResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import CreateOrderRequest

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.create(
            request=CreateOrderRequest(
                sandbox=False
            ),
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = request
        Validator(CreateOrderRequest).is_optional().is_nullable().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CreateOrderResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreateOrderResponse, response)
            )
        )

    @cast_models
    def get(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> OrderResponse:
        """
        Retrieves full details for a Productions order.

        Quote and pricing information may not be available immediately; if you wish to see the quote before submission, you may need to poll the order details until it is ready.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrderResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.get(
            order_id="prodorder_sut9m3vkzvrf8jz8516fglalxe",
        )
        """

        Validator(str).validate(order_id, "order_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/{{order_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("order_id", order_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                OrderResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(OrderResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        order_id: str,
        *,
        request: UpdateOrderRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> UpdateOrderResponse:
        """
        Updates an open order.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request : UpdateOrderRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateOrderResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.update(
            order_id="prodorder_wcszied6ivjj9wcm9huhwb0mad",
            request={
                "name": "name"
            },
        )
        """

        Validator(str).validate(order_id, "order_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdateOrderV1ProductionsOrdersOrderIdPatch(request=request)
        Validator(BodyUpdateOrderV1ProductionsOrdersOrderIdPatch).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/{{order_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("order_id", order_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                UpdateOrderResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(UpdateOrderResponse, response)
            )
        )

    @cast_models
    def submit(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> SubmitOrderResponse:
        """
        Submits an open order for processing. The order must have at least one item. Once submitted, items can no longer be modified.

        Upon submission, the workspace will be charged for the order. The quote is based on information extracted from the uploaded media, such as its duration. The quote may not be available immediately; if you wish to see the quote before submission, you may need to poll the order details until the quote is ready.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubmitOrderResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.submit(
            order_id="prodorder_9pp4826gmvqv1vo0d4t8ftttni",
        )
        """

        Validator(str).validate(order_id, "order_id")

        resolved_config = self._get_resolved_config(
            self._submit_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/{{order_id}}/submit",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("order_id", order_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SubmitOrderResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SubmitOrderResponse, response)
            )
        )


class RawOrdersClient:
    """
    Raw-response client for OrdersClient.

    Each method delegates to the matching :class:`OrdersClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: OrdersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        offset: Union[int, None] = SENTINEL,
        status: Union[List[OrderRequestState], None] = SENTINEL,
        start_date: Union[str, None] = SENTINEL,
        end_date: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListOrdersResponse]:
        data = OrdersClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "offset": offset,
                        "status": status,
                        "start_date": start_date,
                        "end_date": end_date,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        request: CreateOrderRequest = None,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateOrderResponse]:
        data = OrdersClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[OrderResponse]:
        data = OrdersClient.get(self._client, order_id, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        order_id: str,
        *,
        request: UpdateOrderRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateOrderResponse]:
        data = OrdersClient.update(
            self._client, order_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def submit(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[SubmitOrderResponse]:
        data = OrdersClient.submit(
            self._client, order_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncOrdersClient(OrdersClient):
    """
    Async wrapper for OrdersClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def media(self) -> "_AsyncMediaClient":
        """Lazily construct and return the async media sub-resource client."""
        if self._media is None:
            from .media.client import AsyncMediaClient

            _child = AsyncMediaClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._media = _child
        return self._media

    @property
    def items(self) -> "_AsyncItemsClient":
        """Lazily construct and return the async items sub-resource client."""
        if self._items is None:
            from .items.client import AsyncItemsClient

            _child = AsyncItemsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._items = _child
        return self._items

    @property
    def deliverables(self) -> "_AsyncDeliverablesClient":
        """Lazily construct and return the async deliverables sub-resource client."""
        if self._deliverables is None:
            from .deliverables.client import AsyncDeliverablesClient

            _child = AsyncDeliverablesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._deliverables = _child
        return self._deliverables

    @property
    def languages(self) -> "_AsyncLanguagesClient":
        """Lazily construct and return the async languages sub-resource client."""
        if self._languages is None:
            from .languages.client import AsyncLanguagesClient

            _child = AsyncLanguagesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._languages = _child
        return self._languages

    @property
    def with_raw_response(self) -> "AsyncRawOrdersClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawOrdersClient(self)

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        offset: Union[int, None] = SENTINEL,
        status: Union[List[OrderRequestState], None] = SENTINEL,
        start_date: Union[str, None] = SENTINEL,
        end_date: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListOrdersResponse]:  # type: ignore[override]
        """
        Lists Productions orders in the workspace. Supports filtering by status and date range, with pagination.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Maximum number of orders to return per page.

        offset : typing.Optional[int]
            Number of orders to skip for pagination.

        status : typing.Optional[typing.Sequence[OrderRequestState]]
            Filter orders by one or more statuses.

        start_date : typing.Optional[str]
            Filter orders created on or after this date.

        end_date : typing.Optional[str]
            Filter orders created on or before this date.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrdersResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.list(
                page_size=20,
                offset=10,
                status=[
                    "open"
                ],
                start_date="2023-07-20T21:03:51.582Z",
                end_date="2023-07-20T21:03:51.582Z",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "offset": offset,
                        "status": status,
                        "start_date": start_date,
                        "end_date": end_date,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        request: CreateOrderRequest = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreateOrderResponse]:  # type: ignore[override]
        """
        Creates a new Productions order in the workspace. The order starts in the open state and can be configured with items before submission.

        Parameters
        ----------
        request : typing.Optional[CreateOrderRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateOrderResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import CreateOrderRequest

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.create(
                request=CreateOrderRequest(
                    sandbox=False
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            request=request, request_options=request_options
        )

    def get(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[OrderResponse]:  # type: ignore[override]
        """
        Retrieves full details for a Productions order.

        Quote and pricing information may not be available immediately; if you wish to see the quote before submission, you may need to poll the order details until it is ready.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrderResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.get(
                order_id="prodorder_sut9m3vkzvrf8jz8516fglalxe",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(order_id, request_options=request_options)

    def update(
        self,
        order_id: str,
        *,
        request: UpdateOrderRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[UpdateOrderResponse]:  # type: ignore[override]
        """
        Updates an open order.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request : UpdateOrderRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateOrderResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.update(
                order_id="prodorder_wcszied6ivjj9wcm9huhwb0mad",
                request={
                    "name": "name"
                },
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            order_id, request=request, request_options=request_options
        )

    def submit(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[SubmitOrderResponse]:  # type: ignore[override]
        """
        Submits an open order for processing. The order must have at least one item. Once submitted, items can no longer be modified.

        Upon submission, the workspace will be charged for the order. The quote is based on information extracted from the uploaded media, such as its duration. The quote may not be available immediately; if you wish to see the quote before submission, you may need to poll the order details until the quote is ready.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubmitOrderResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.submit(
                order_id="prodorder_9pp4826gmvqv1vo0d4t8ftttni",
            )


        asyncio.run(main())
        """
        return to_async(super().submit)(order_id, request_options=request_options)


class AsyncRawOrdersClient:
    """
    Async raw-response client for AsyncOrdersClient.
    """

    def __init__(self, client: AsyncOrdersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        offset: Union[int, None] = SENTINEL,
        status: Union[List[OrderRequestState], None] = SENTINEL,
        start_date: Union[str, None] = SENTINEL,
        end_date: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListOrdersResponse]:
        data = await AsyncOrdersClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "offset": offset,
                        "status": status,
                        "start_date": start_date,
                        "end_date": end_date,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        request: CreateOrderRequest = None,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateOrderResponse]:
        data = await AsyncOrdersClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[OrderResponse]:
        data = await AsyncOrdersClient.get(
            self._client, order_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        order_id: str,
        *,
        request: UpdateOrderRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateOrderResponse]:
        data = await AsyncOrdersClient.update(
            self._client, order_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def submit(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[SubmitOrderResponse]:
        data = await AsyncOrdersClient.submit(
            self._client, order_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
