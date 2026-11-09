from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyRegisterMediaV1ProductionsOrdersOrderIdMediaPost,
    HttpValidationError,
    OrderMediaResponse,
    RegisterMediaResponse,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class MediaClient(BaseService):
    """
    Fern-style resource client for MediaClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._register_config: SdkConfig = {}
        self._get_config: SdkConfig = {}

    def set_register_config(self, config: SdkConfig):
        """
        Sets method-level configuration for register.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._register_config = config
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
    def with_raw_response(self) -> "RawMediaClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawMediaClient(self)

    @cast_models
    def register(
        self,
        order_id: str,
        *,
        declared_language: str,
        media: Union[bytes, None] = SENTINEL,
        media_url: Union[str, None] = SENTINEL,
        media_url_filename: Union[str, None] = SENTINEL,
        media_url_content_type: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> RegisterMediaResponse:
        """
        Registers a media file with an order, either by uploading it directly or by providing a URL to fetch it from. Exactly one of `media` or `media_url` must be provided. The registered media can then be referenced when adding order items.

        Parameters
        ----------
        order_id : str
            The ID of the order to which this media will be attached.

        declared_language : str
            The language code of the media content (e.g. 'en', 'es-ES'). Must be a supported source language for some order item kind.

        media : typing.Optional[core.File]
            The media file to upload. Mutually exclusive with media_url.

        media_url : typing.Optional[str]
            A URL to fetch the media file from. Mutually exclusive with media.

        media_url_filename : typing.Optional[str]
            The filename for URL-sourced media (e.g. 'example.mp4'). Required when using media_url.

        media_url_content_type : typing.Optional[str]
            The MIME type for URL-sourced media (e.g. 'video/mp4'). Required when using media_url.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterMediaResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.media.register(
            order_id="prodorder_zdbf7s14r4s3f0geyi5gs9qkth",
            declared_language="declared_language",
            media="media",
            media_url="media_url",
            media_url_filename="media_url_filename",
            media_url_content_type="media_url_content_type",
        )
        """

        Validator(str).validate(order_id, "order_id")

        resolved_config = self._get_resolved_config(
            self._register_config, request_options
        )

        request_body = BodyRegisterMediaV1ProductionsOrdersOrderIdMediaPost(
            declared_language=declared_language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "media": media,
                        "media_url": media_url,
                        "media_url_filename": media_url_filename,
                        "media_url_content_type": media_url_content_type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyRegisterMediaV1ProductionsOrdersOrderIdMediaPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/{{order_id}}/media",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("order_id", order_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                RegisterMediaResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(RegisterMediaResponse, response)
            )
        )

    @cast_models
    def get(
        self,
        order_id: str,
        media_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> OrderMediaResponse:
        """
        Retrieves metadata and a time-limited download URL for a previously uploaded media file.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        media_id : str
            The ID of the media file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrderMediaResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.productions.orders.media.get(
            order_id="prodorder_tmqom91h48s233jlxex5qa0l3g",
            media_id="prodmedia_vjobie73pds4sgw7eq4ho3nitc",
        )
        """

        Validator(str).validate(order_id, "order_id")
        Validator(str).validate(media_id, "media_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/productions/orders/{{order_id}}/media/{{media_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("order_id", order_id)
            .add_path("media_id", media_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                OrderMediaResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(OrderMediaResponse, response)
            )
        )


class RawMediaClient:
    """
    Raw-response client for MediaClient.

    Each method delegates to the matching :class:`MediaClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: MediaClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def register(
        self,
        order_id: str,
        *,
        declared_language: str,
        media: Union[bytes, None] = SENTINEL,
        media_url: Union[str, None] = SENTINEL,
        media_url_filename: Union[str, None] = SENTINEL,
        media_url_content_type: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[RegisterMediaResponse]:
        data = MediaClient.register(
            self._client,
            order_id,
            declared_language=declared_language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "media": media,
                        "media_url": media_url,
                        "media_url_filename": media_url_filename,
                        "media_url_content_type": media_url_content_type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        order_id: str,
        media_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[OrderMediaResponse]:
        data = MediaClient.get(
            self._client, order_id, media_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncMediaClient(MediaClient):
    """
    Async wrapper for MediaClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawMediaClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawMediaClient(self)

    def register(
        self,
        order_id: str,
        *,
        declared_language: str,
        media: Union[bytes, None] = SENTINEL,
        media_url: Union[str, None] = SENTINEL,
        media_url_filename: Union[str, None] = SENTINEL,
        media_url_content_type: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[RegisterMediaResponse]:  # type: ignore[override]
        """
        Registers a media file with an order, either by uploading it directly or by providing a URL to fetch it from. Exactly one of `media` or `media_url` must be provided. The registered media can then be referenced when adding order items.

        Parameters
        ----------
        order_id : str
            The ID of the order to which this media will be attached.

        declared_language : str
            The language code of the media content (e.g. 'en', 'es-ES'). Must be a supported source language for some order item kind.

        media : typing.Optional[core.File]
            The media file to upload. Mutually exclusive with media_url.

        media_url : typing.Optional[str]
            A URL to fetch the media file from. Mutually exclusive with media.

        media_url_filename : typing.Optional[str]
            The filename for URL-sourced media (e.g. 'example.mp4'). Required when using media_url.

        media_url_content_type : typing.Optional[str]
            The MIME type for URL-sourced media (e.g. 'video/mp4'). Required when using media_url.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterMediaResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.media.register(
                order_id="prodorder_zdbf7s14r4s3f0geyi5gs9qkth",
                declared_language="declared_language",
                media="media",
                media_url="media_url",
                media_url_filename="media_url_filename",
                media_url_content_type="media_url_content_type",
            )


        asyncio.run(main())
        """
        return to_async(super().register)(
            order_id,
            declared_language=declared_language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "media": media,
                        "media_url": media_url,
                        "media_url_filename": media_url_filename,
                        "media_url_content_type": media_url_content_type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        order_id: str,
        media_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[OrderMediaResponse]:  # type: ignore[override]
        """
        Retrieves metadata and a time-limited download URL for a previously uploaded media file.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        media_id : str
            The ID of the media file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrderMediaResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.productions.orders.media.get(
                order_id="prodorder_tmqom91h48s233jlxex5qa0l3g",
                media_id="prodmedia_vjobie73pds4sgw7eq4ho3nitc",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            order_id, media_id, request_options=request_options
        )


class AsyncRawMediaClient:
    """
    Async raw-response client for AsyncMediaClient.
    """

    def __init__(self, client: AsyncMediaClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def register(
        self,
        order_id: str,
        *,
        declared_language: str,
        media: Union[bytes, None] = SENTINEL,
        media_url: Union[str, None] = SENTINEL,
        media_url_filename: Union[str, None] = SENTINEL,
        media_url_content_type: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[RegisterMediaResponse]:
        data = await AsyncMediaClient.register(
            self._client,
            order_id,
            declared_language=declared_language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "media": media,
                        "media_url": media_url,
                        "media_url_filename": media_url_filename,
                        "media_url_content_type": media_url_content_type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        order_id: str,
        media_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[OrderMediaResponse]:
        data = await AsyncMediaClient.get(
            self._client, order_id, media_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
