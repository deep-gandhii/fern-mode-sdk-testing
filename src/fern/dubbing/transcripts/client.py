from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import DubbingTranscriptsResponseModel, GetFormatType, HttpValidationError
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class TranscriptsClient(BaseService):
    """
    Fern-style resource client for TranscriptsClient.
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
    def with_raw_response(self) -> "RawTranscriptsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTranscriptsClient(self)

    @cast_models
    def get(
        self,
        dubbing_id: str,
        language_code: str,
        format_type: GetFormatType,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingTranscriptsResponseModel:
        """
        Fetch the transcript for one of the languages in a dub.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language_code : str
            ISO-693 language code to retrieve the transcript for. Use 'source' to fetch the transcript of the original media.

        format_type : GetFormatType
            Format to return transcript in. For subtitles use either 'srt' or 'webvtt', and for a full transcript use 'json'. The 'json' format is not yet supported for Dubbing Studio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingTranscriptsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import GetFormatType

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.transcripts.get(
            dubbing_id="dubbing_id",
            language_code="source",
            format_type="srt",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")
        Validator(str).validate(language_code, "language_code")
        Validator(GetFormatType).validate(format_type, "format_type")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/{{dubbing_id}}/transcripts/{{language_code}}/format/{{format_type}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .add_path("language_code", language_code)
            .add_path("format_type", format_type)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingTranscriptsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingTranscriptsResponseModel, response)
            )
        )


class RawTranscriptsClient:
    """
    Raw-response client for TranscriptsClient.

    Each method delegates to the matching :class:`TranscriptsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TranscriptsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        dubbing_id: str,
        language_code: str,
        format_type: GetFormatType,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingTranscriptsResponseModel]:
        data = TranscriptsClient.get(
            self._client,
            dubbing_id,
            language_code,
            format_type,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncTranscriptsClient(TranscriptsClient):
    """
    Async wrapper for TranscriptsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawTranscriptsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTranscriptsClient(self)

    def get(
        self,
        dubbing_id: str,
        language_code: str,
        format_type: GetFormatType,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingTranscriptsResponseModel]:  # type: ignore[override]
        """
        Fetch the transcript for one of the languages in a dub.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language_code : str
            ISO-693 language code to retrieve the transcript for. Use 'source' to fetch the transcript of the original media.

        format_type : GetFormatType
            Format to return transcript in. For subtitles use either 'srt' or 'webvtt', and for a full transcript use 'json'. The 'json' format is not yet supported for Dubbing Studio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingTranscriptsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import GetFormatType

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.transcripts.get(
                dubbing_id="dubbing_id",
                language_code="source",
                format_type="srt",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            dubbing_id, language_code, format_type, request_options=request_options
        )


class AsyncRawTranscriptsClient:
    """
    Async raw-response client for AsyncTranscriptsClient.
    """

    def __init__(self, client: AsyncTranscriptsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        dubbing_id: str,
        language_code: str,
        format_type: GetFormatType,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingTranscriptsResponseModel]:
        data = await AsyncTranscriptsClient.get(
            self._client,
            dubbing_id,
            language_code,
            format_type,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
