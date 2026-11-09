from typing import Any, Optional, Dict, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.sentinel import SENTINEL
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import HttpValidationError, SegmentCreatePayload, SegmentCreateResponse
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
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
        self._create_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
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
    def create(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        start_time: float,
        end_time: float,
        text: Union[str, None] = SENTINEL,
        translations: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> SegmentCreateResponse:
        """
        Creates a new segment in dubbing resource with a start and end time for the speaker in every available language. Does not automatically generate transcripts/translations/audio.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        speaker_id : str
            ID of the speaker.

        start_time : float

        end_time : float

        text : typing.Optional[str]

        translations : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentCreateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.speaker.segment.create(
            dubbing_id="dubbing_id",
            speaker_id="speaker_id",
            start_time=5.47,
            end_time=6.44,
            text="text",
            translations={},
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")
        Validator(str).validate(speaker_id, "speaker_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = SegmentCreatePayload(
            start_time=start_time,
            end_time=end_time,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"text": text, "translations": translations}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(SegmentCreatePayload).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/speaker/{{speaker_id}}/segment",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .add_path("speaker_id", speaker_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SegmentCreateResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SegmentCreateResponse, response)
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

    def create(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        start_time: float,
        end_time: float,
        text: Union[str, None] = SENTINEL,
        translations: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentCreateResponse]:
        data = SegmentClient.create(
            self._client,
            dubbing_id,
            speaker_id,
            start_time=start_time,
            end_time=end_time,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"text": text, "translations": translations}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
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

    def create(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        start_time: float,
        end_time: float,
        text: Union[str, None] = SENTINEL,
        translations: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SegmentCreateResponse]:  # type: ignore[override]
        """
        Creates a new segment in dubbing resource with a start and end time for the speaker in every available language. Does not automatically generate transcripts/translations/audio.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        speaker_id : str
            ID of the speaker.

        start_time : float

        end_time : float

        text : typing.Optional[str]

        translations : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentCreateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.speaker.segment.create(
                dubbing_id="dubbing_id",
                speaker_id="speaker_id",
                start_time=5.47,
                end_time=6.44,
                text="text",
                translations={},
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            dubbing_id,
            speaker_id,
            start_time=start_time,
            end_time=end_time,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"text": text, "translations": translations}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawSegmentClient:
    """
    Async raw-response client for AsyncSegmentClient.
    """

    def __init__(self, client: AsyncSegmentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        start_time: float,
        end_time: float,
        text: Union[str, None] = SENTINEL,
        translations: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentCreateResponse]:
        data = await AsyncSegmentClient.create(
            self._client,
            dubbing_id,
            speaker_id,
            start_time=start_time,
            end_time=end_time,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"text": text, "translations": translations}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
