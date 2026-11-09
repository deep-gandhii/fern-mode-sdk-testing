from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    HttpValidationError,
    SegmentDeleteResponse,
    SegmentUpdatePayload,
    SegmentUpdateResponse,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class SegmentClient(BaseService):
    """
    Fern-style resource client for SegmentClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSegmentClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSegmentClient(self)

    @cast_models
    def update(
        self,
        dubbing_id: str,
        segment_id: str,
        language: str,
        *,
        start_time: Union[float, None] = SENTINEL,
        end_time: Union[float, None] = SENTINEL,
        text: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> SegmentUpdateResponse:
        """
        Modifies a single segment with new text and/or start/end times. Will update the values for only a specific language of a segment. Does not automatically regenerate the dub.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segment_id : str
            ID of the segment

        language : str
            ID of the language.

        start_time : typing.Optional[float]

        end_time : typing.Optional[float]

        text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentUpdateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.segment.update(
            dubbing_id="dubbing_id",
            segment_id="segment_id",
            language="language",
            start_time=3.17,
            end_time=2.48,
            text="text",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")
        Validator(str).validate(segment_id, "segment_id")
        Validator(str).validate(language, "language")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = SegmentUpdatePayload(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "text": text,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(SegmentUpdatePayload).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/segment/{{segment_id}}/{{language}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .add_path("segment_id", segment_id)
            .add_path("language", language)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SegmentUpdateResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SegmentUpdateResponse, response)
            )
        )

    @cast_models
    def delete(
        self,
        dubbing_id: str,
        segment_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SegmentDeleteResponse:
        """
        Deletes a single segment from the dubbing.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segment_id : str
            ID of the segment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentDeleteResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.segment.delete(
            dubbing_id="dubbing_id",
            segment_id="segment_id",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")
        Validator(str).validate(segment_id, "segment_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/segment/{{segment_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .add_path("segment_id", segment_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SegmentDeleteResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SegmentDeleteResponse, response)
            )
        )


class RawSegmentClient:
    """
    Raw-response client for SegmentClient.

    Each method delegates to the matching :class:`SegmentClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SegmentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def update(
        self,
        dubbing_id: str,
        segment_id: str,
        language: str,
        *,
        start_time: Union[float, None] = SENTINEL,
        end_time: Union[float, None] = SENTINEL,
        text: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentUpdateResponse]:
        data = SegmentClient.update(
            self._client,
            dubbing_id,
            segment_id,
            language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "text": text,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        dubbing_id: str,
        segment_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentDeleteResponse]:
        data = SegmentClient.delete(
            self._client, dubbing_id, segment_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSegmentClient(SegmentClient):
    """
    Async wrapper for SegmentClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSegmentClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSegmentClient(self)

    def update(
        self,
        dubbing_id: str,
        segment_id: str,
        language: str,
        *,
        start_time: Union[float, None] = SENTINEL,
        end_time: Union[float, None] = SENTINEL,
        text: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SegmentUpdateResponse]:  # type: ignore[override]
        """
        Modifies a single segment with new text and/or start/end times. Will update the values for only a specific language of a segment. Does not automatically regenerate the dub.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segment_id : str
            ID of the segment

        language : str
            ID of the language.

        start_time : typing.Optional[float]

        end_time : typing.Optional[float]

        text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentUpdateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.segment.update(
                dubbing_id="dubbing_id",
                segment_id="segment_id",
                language="language",
                start_time=3.17,
                end_time=2.48,
                text="text",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            dubbing_id,
            segment_id,
            language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "text": text,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self,
        dubbing_id: str,
        segment_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SegmentDeleteResponse]:  # type: ignore[override]
        """
        Deletes a single segment from the dubbing.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segment_id : str
            ID of the segment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentDeleteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.segment.delete(
                dubbing_id="dubbing_id",
                segment_id="segment_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            dubbing_id, segment_id, request_options=request_options
        )


class AsyncRawSegmentClient:
    """
    Async raw-response client for AsyncSegmentClient.
    """

    def __init__(self, client: AsyncSegmentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def update(
        self,
        dubbing_id: str,
        segment_id: str,
        language: str,
        *,
        start_time: Union[float, None] = SENTINEL,
        end_time: Union[float, None] = SENTINEL,
        text: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentUpdateResponse]:
        data = await AsyncSegmentClient.update(
            self._client,
            dubbing_id,
            segment_id,
            language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "text": text,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        dubbing_id: str,
        segment_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentDeleteResponse]:
        data = await AsyncSegmentClient.delete(
            self._client, dubbing_id, segment_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
