from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import HttpValidationError, OrderDeliverablesResponse
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class DeliverablesClient(BaseService):
    """
    Fern-style resource client for DeliverablesClient.
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
    def with_raw_response(self) -> "RawDeliverablesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawDeliverablesClient(self)

    @cast_models
    def list(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> OrderDeliverablesResponse:
        """
        Retrieves the delivered files for a completed order. Returns an empty list if the order is not yet completed.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrderDeliverablesResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.deliverables.list(
            order_id="prodorder_ec8msxt6qz46ok5fhzo2dkuu90",
        )
        """

        Validator(str).validate(order_id, "order_id")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/{{order_id}}/deliverables",
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
                OrderDeliverablesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(OrderDeliverablesResponse, response)
            )
        )


class RawDeliverablesClient:
    """
    Raw-response client for DeliverablesClient.

    Each method delegates to the matching :class:`DeliverablesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: DeliverablesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[OrderDeliverablesResponse]:
        data = DeliverablesClient.list(
            self._client, order_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDeliverablesClient(DeliverablesClient):
    """
    Async wrapper for DeliverablesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawDeliverablesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDeliverablesClient(self)

    def list(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[OrderDeliverablesResponse]:  # type: ignore[override]
        """
        Retrieves the delivered files for a completed order. Returns an empty list if the order is not yet completed.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrderDeliverablesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.deliverables.list(
                order_id="prodorder_ec8msxt6qz46ok5fhzo2dkuu90",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(order_id, request_options=request_options)


class AsyncRawDeliverablesClient:
    """
    Async raw-response client for AsyncDeliverablesClient.
    """

    def __init__(self, client: AsyncDeliverablesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, order_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[OrderDeliverablesResponse]:
        data = await AsyncDeliverablesClient.list(
            self._client, order_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
