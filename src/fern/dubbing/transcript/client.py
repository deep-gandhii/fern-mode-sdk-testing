from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types.transcript_get_transcript_for_dub_response import (
    TranscriptGetTranscriptForDubResponse_adapter,
)
from ...types import (
    GetTranscriptForDubFormatType,
    HttpValidationError,
    TranscriptGetTranscriptForDubResponse,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.transport.api_error import ApiError
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class TranscriptClient(BaseService):
    """
    Fern-style resource client for TranscriptClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_transcript_for_dub_config: SdkConfig = {}

    def set_get_transcript_for_dub_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_transcript_for_dub.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_transcript_for_dub_config = config
        return self

    @property
    def with_raw_response(self) -> "RawTranscriptClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTranscriptClient(self)

    @cast_models
    def get_transcript_for_dub(
        self,
        dubbing_id: str,
        language_code: str,
        *,
        format_type: Union[GetTranscriptForDubFormatType, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Union[TranscriptGetTranscriptForDubResponse, str]:
        """
        Returns transcript for the dub as an SRT or WEBVTT file.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language_code : str
            ISO-693 language code to retrieve the transcript for. Use 'source' to fetch the transcript of the original media.

        format_type : typing.Optional[GetTranscriptForDubFormatType]
            Format to return transcript in. For subtitles use either 'srt' or 'webvtt', and for a full transcript use 'json'. The 'json' format is not yet supported for Dubbing Studio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Union[TranscriptGetTranscriptForDubResponse, str]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import GetTranscriptForDubFormatType

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.transcript.get_transcript_for_dub(
            dubbing_id="dubbing_id",
            language_code="source",
            format_type="srt",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")
        Validator(str).validate(language_code, "language_code")
        Validator(GetTranscriptForDubFormatType).is_optional().is_nullable().validate(
            format_type, "format_type"
        )

        resolved_config = self._get_resolved_config(
            self._get_transcript_for_dub_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/{{dubbing_id}}/transcript/{{language_code}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .add_path("language_code", language_code)
            .add_query("format_type", format_type, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if status in {200} and response in (b"", ""):
            return None
        if content == "application/json":
            return (
                None
                if response in (b"", "")
                else (
                    TranscriptGetTranscriptForDubResponse_adapter.validate_python(
                        response
                    )
                    if should_validate_response(resolved_config)
                    else construct_lenient(
                        TranscriptGetTranscriptForDubResponse, response
                    )
                )
            )
        if content == "text/plain":
            return response
        raise ApiError("Error on deserializing the response.", status, response)


class RawTranscriptClient:
    """
    Raw-response client for TranscriptClient.

    Each method delegates to the matching :class:`TranscriptClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TranscriptClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get_transcript_for_dub(
        self,
        dubbing_id: str,
        language_code: str,
        *,
        format_type: Union[GetTranscriptForDubFormatType, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Union[TranscriptGetTranscriptForDubResponse, str]]:
        data = TranscriptClient.get_transcript_for_dub(
            self._client,
            dubbing_id,
            language_code,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"format_type": format_type}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncTranscriptClient(TranscriptClient):
    """
    Async wrapper for TranscriptClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawTranscriptClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTranscriptClient(self)

    def get_transcript_for_dub(
        self,
        dubbing_id: str,
        language_code: str,
        *,
        format_type: Union[GetTranscriptForDubFormatType, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Union[TranscriptGetTranscriptForDubResponse, str]]:  # type: ignore[override]
        """
        Returns transcript for the dub as an SRT or WEBVTT file.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language_code : str
            ISO-693 language code to retrieve the transcript for. Use 'source' to fetch the transcript of the original media.

        format_type : typing.Optional[GetTranscriptForDubFormatType]
            Format to return transcript in. For subtitles use either 'srt' or 'webvtt', and for a full transcript use 'json'. The 'json' format is not yet supported for Dubbing Studio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Union[TranscriptGetTranscriptForDubResponse, str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import GetTranscriptForDubFormatType

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.transcript.get_transcript_for_dub(
                dubbing_id="dubbing_id",
                language_code="source",
                format_type="srt",
            )


        asyncio.run(main())
        """
        return to_async(super().get_transcript_for_dub)(
            dubbing_id,
            language_code,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"format_type": format_type}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawTranscriptClient:
    """
    Async raw-response client for AsyncTranscriptClient.
    """

    def __init__(self, client: AsyncTranscriptClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get_transcript_for_dub(
        self,
        dubbing_id: str,
        language_code: str,
        *,
        format_type: Union[GetTranscriptForDubFormatType, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Union[TranscriptGetTranscriptForDubResponse, str]]:
        data = await AsyncTranscriptClient.get_transcript_for_dub(
            self._client,
            dubbing_id,
            language_code,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"format_type": format_type}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
