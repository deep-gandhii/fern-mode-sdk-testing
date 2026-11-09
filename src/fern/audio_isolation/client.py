from typing import Any, Optional, Generator, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AudioIsolationRequest,
    AudioIsolationRequestFileFormat,
    AudioIsolationStreamRequest,
    AudioIsolationStreamRequestFileFormat,
    GetAudioIsolationHistoryResponseModel,
    HttpValidationError,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading


class AudioIsolationClient(BaseService):
    """
    Fern-style resource client for AudioIsolationClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._convert_config: SdkConfig = {}
        self._list_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._stream_config: SdkConfig = {}

    def set_convert_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_config = config
        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    def set_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._stream_config = config
        return self

    @property
    def with_raw_response(self) -> "RawAudioIsolationClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAudioIsolationClient(self)

    @cast_models
    def convert(
        self,
        *,
        audio: bytes,
        file_format: Union[AudioIsolationRequestFileFormat, None] = SENTINEL,
        preview_b_64: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Removes background noise from audio.

        Parameters
        ----------
        audio : core.File
            The audio file from which vocals/speech will be isolated from.

        file_format : typing.Optional[AudioIsolationRequestFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        preview_b_64 : typing.Optional[str]
            Optional preview image base64 for tracking this generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.audio_isolation.convert(
            audio="audio",
            file_format="pcm_s16le_16",
            preview_b_64="preview_b64",
        )
        for chunk in response:
            print(chunk)
        """

        resolved_config = self._get_resolved_config(
            self._convert_config, request_options
        )

        request_body = AudioIsolationRequest(
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file_format": file_format,
                        "preview_b_64": preview_b_64,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(AudioIsolationRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/audio-isolation",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body, "multipart/form-data")
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        page: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetAudioIsolationHistoryResponseModel:
        """
        Returns a list of all your audio isolation generations.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many history items to return at maximum. Defaults to 100.

        page : typing.Optional[int]
            Page number for search pagination (1-based). Only used when search is provided.

        search : typing.Optional[str]
            Optional search term used for filtering audio isolation history (title/text).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioIsolationHistoryResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.audio_isolation.list(
            page_size=100,
            page=1,
            search="search",
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(int).is_optional().is_nullable().validate(page, "page")
        Validator(str).is_optional().is_nullable().validate(search, "search")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/audio-isolation/history",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("page_size", page_size, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("search", search, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetAudioIsolationHistoryResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAudioIsolationHistoryResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a specific audio isolation history item and the associated media files.

        Parameters
        ----------
        history_item_id : str
            Identifier of the audio isolation history item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.audio_isolation.delete(
            history_item_id="history_item_id",
        )
        """

        Validator(str).validate(history_item_id, "history_item_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/audio-isolation/history/{{history_item_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("history_item_id", history_item_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def stream(
        self,
        *,
        audio: bytes,
        file_format: Union[AudioIsolationStreamRequestFileFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Removes background noise from audio.

        Parameters
        ----------
        audio : core.File
            The audio file from which vocals/speech will be isolated from.

        file_format : typing.Optional[AudioIsolationStreamRequestFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.audio_isolation.stream(
            audio="audio",
            file_format="pcm_s16le_16",
        )
        for chunk in response:
            print(chunk)
        """

        resolved_config = self._get_resolved_config(
            self._stream_config, request_options
        )

        request_body = AudioIsolationStreamRequest(
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"file_format": file_format}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(AudioIsolationStreamRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/audio-isolation/stream",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body, "multipart/form-data")
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response


class RawAudioIsolationClient:
    """
    Raw-response client for AudioIsolationClient.

    Each method delegates to the matching :class:`AudioIsolationClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AudioIsolationClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        *,
        audio: bytes,
        file_format: Union[AudioIsolationRequestFileFormat, None] = SENTINEL,
        preview_b_64: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = AudioIsolationClient.convert(
            _call_client,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file_format": file_format,
                        "preview_b_64": preview_b_64,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        page: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAudioIsolationHistoryResponseModel]:
        data = AudioIsolationClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "page": page,
                        "search": search,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        AudioIsolationClient.delete(
            self._client, history_item_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)

    def stream(
        self,
        *,
        audio: bytes,
        file_format: Union[AudioIsolationStreamRequestFileFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = AudioIsolationClient.stream(
            _call_client,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"file_format": file_format}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )


class AsyncAudioIsolationClient(AudioIsolationClient):
    """
    Async wrapper for AudioIsolationClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAudioIsolationClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAudioIsolationClient(self)

    def convert(
        self,
        *,
        audio: bytes,
        file_format: Union[AudioIsolationRequestFileFormat, None] = SENTINEL,
        preview_b_64: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Removes background noise from audio.

        Parameters
        ----------
        audio : core.File
            The audio file from which vocals/speech will be isolated from.

        file_format : typing.Optional[AudioIsolationRequestFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        preview_b_64 : typing.Optional[str]
            Optional preview image base64 for tracking this generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.audio_isolation.convert(
                audio="audio",
                file_format="pcm_s16le_16",
                preview_b_64="preview_b64",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().convert(
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file_format": file_format,
                        "preview_b_64": preview_b_64,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

        async def async_generator():
            exhausted = object()
            closing = threading.Event()

            def pull():
                try:
                    return next(sync_generator, exhausted)
                finally:
                    if closing.is_set():
                        sync_generator.close()

            try:
                while True:
                    item = await asyncio.to_thread(pull)
                    if item is exhausted:
                        return
                    yield item
            finally:
                closing.set()
                try:
                    sync_generator.close()
                except ValueError as error:
                    if "already executing" not in str(error):
                        raise

        return async_generator()

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        page: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetAudioIsolationHistoryResponseModel]:  # type: ignore[override]
        """
        Returns a list of all your audio isolation generations.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many history items to return at maximum. Defaults to 100.

        page : typing.Optional[int]
            Page number for search pagination (1-based). Only used when search is provided.

        search : typing.Optional[str]
            Optional search term used for filtering audio isolation history (title/text).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioIsolationHistoryResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.audio_isolation.list(
                page_size=100,
                page=1,
                search="search",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "page": page,
                        "search": search,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Deletes a specific audio isolation history item and the associated media files.

        Parameters
        ----------
        history_item_id : str
            Identifier of the audio isolation history item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.audio_isolation.delete(
                history_item_id="history_item_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            history_item_id, request_options=request_options
        )

    def stream(
        self,
        *,
        audio: bytes,
        file_format: Union[AudioIsolationStreamRequestFileFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Removes background noise from audio.

        Parameters
        ----------
        audio : core.File
            The audio file from which vocals/speech will be isolated from.

        file_format : typing.Optional[AudioIsolationStreamRequestFileFormat]
            The format of input audio. Options are 'pcm_s16le_16' or 'other' For `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample rate, single channel (mono), and little-endian byte order. Latency will be lower than with passing an encoded waveform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.audio_isolation.stream(
                audio="audio",
                file_format="pcm_s16le_16",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream(
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"file_format": file_format}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

        async def async_generator():
            exhausted = object()
            closing = threading.Event()

            def pull():
                try:
                    return next(sync_generator, exhausted)
                finally:
                    if closing.is_set():
                        sync_generator.close()

            try:
                while True:
                    item = await asyncio.to_thread(pull)
                    if item is exhausted:
                        return
                    yield item
            finally:
                closing.set()
                try:
                    sync_generator.close()
                except ValueError as error:
                    if "already executing" not in str(error):
                        raise

        return async_generator()


class AsyncRawAudioIsolationClient:
    """
    Async raw-response client for AsyncAudioIsolationClient.
    """

    def __init__(self, client: AsyncAudioIsolationClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def convert(
        self,
        *,
        audio: bytes,
        file_format: Union[AudioIsolationRequestFileFormat, None] = SENTINEL,
        preview_b_64: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncAudioIsolationClient.convert(
            _call_client,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file_format": file_format,
                        "preview_b_64": preview_b_64,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    async def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        page: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAudioIsolationHistoryResponseModel]:
        data = await AsyncAudioIsolationClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "page": page,
                        "search": search,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        await AsyncAudioIsolationClient.delete(
            self._client, history_item_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)

    def stream(
        self,
        *,
        audio: bytes,
        file_format: Union[AudioIsolationStreamRequestFileFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncAudioIsolationClient.stream(
            _call_client,
            audio=audio,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"file_format": file_format}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )
