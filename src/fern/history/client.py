from typing import Any, Optional, Generator, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    DeleteHistoryItemResponse,
    DownloadBadRequestResponse,
    DownloadHistoryRequest,
    GetSpeechHistoryResponse,
    HttpValidationError,
    ListSortDirection,
    Source,
    SpeechHistoryItemResponse,
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


class HistoryClient(BaseService):
    """
    Fern-style resource client for HistoryClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._get_audio_config: SdkConfig = {}
        self._download_config: SdkConfig = {}

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    def set_get_audio_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_audio.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_audio_config = config
        return self

    def set_download_config(self, config: SdkConfig):
        """
        Sets method-level configuration for download.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._download_config = config
        return self

    @property
    def with_raw_response(self) -> "RawHistoryClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawHistoryClient(self)

    @cast_models
    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        start_after_history_item_id: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        date_before_unix: Union[int, None] = SENTINEL,
        date_after_unix: Union[int, None] = SENTINEL,
        sort_direction: Union[ListSortDirection, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        source: Union[Source, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetSpeechHistoryResponse:
        """
        Returns a list of your generated audio (e.g. text to speech, speech to speech, Studio, dubbing). Music and SFX generations are not included and cannot currently be retrieved via the API.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many history items to return at maximum. Can not exceed 1000, defaults to 100.

        start_after_history_item_id : typing.Optional[str]
            After which ID to start fetching, use this parameter to paginate across a large collection of history items. In case this parameter is not provided history items will be fetched starting from the most recently created one ordered descending by their creation date.

        voice_id : typing.Optional[str]
            ID of the voice to be filtered for. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        model_id : typing.Optional[str]
            Search term used for filtering history items. If provided, source becomes required.

        date_before_unix : typing.Optional[int]
            Unix timestamp to filter history items before this date (exclusive).

        date_after_unix : typing.Optional[int]
            Unix timestamp to filter history items after this date (inclusive).

        sort_direction : typing.Optional[ListSortDirection]
            Sort direction for the results.

        search : typing.Optional[str]
            search term used for filtering

        source : typing.Optional[Source]
            Source of the generated history item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSpeechHistoryResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import ListSortDirection, Source

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.history.list(
            page_size=100,
            start_after_history_item_id="start_after_history_item_id",
            voice_id="voice_id",
            model_id="model_id",
            date_before_unix=8,
            date_after_unix=2,
            sort_direction="asc",
            search="search",
            source="TTS",
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(
            start_after_history_item_id, "start_after_history_item_id"
        )
        Validator(str).is_optional().is_nullable().validate(voice_id, "voice_id")
        Validator(str).is_optional().is_nullable().validate(model_id, "model_id")
        Validator(int).is_optional().is_nullable().validate(
            date_before_unix, "date_before_unix"
        )
        Validator(int).is_optional().is_nullable().validate(
            date_after_unix, "date_after_unix"
        )
        Validator(ListSortDirection).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(Source).is_optional().is_nullable().validate(source, "source")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/history",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("page_size", page_size, nullable=True)
            .add_query(
                "start_after_history_item_id",
                start_after_history_item_id,
                nullable=True,
            )
            .add_query("voice_id", voice_id, nullable=True)
            .add_query("model_id", model_id, nullable=True)
            .add_query("date_before_unix", date_before_unix, nullable=True)
            .add_query("date_after_unix", date_after_unix, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query("source", source, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetSpeechHistoryResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetSpeechHistoryResponse, response)
            )
        )

    @cast_models
    def get(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> SpeechHistoryItemResponse:
        """
        Retrieves a history item.

        Parameters
        ----------
        history_item_id : str
            ID of the history item to be used. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeechHistoryItemResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.history.get(
            history_item_id="VW7YKqPnjY4h39yTbx2L",
        )
        """

        Validator(str).validate(history_item_id, "history_item_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/history/{{history_item_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("history_item_id", history_item_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SpeechHistoryItemResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SpeechHistoryItemResponse, response)
            )
        )

    @cast_models
    def delete(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DeleteHistoryItemResponse:
        """
        Delete a history item by its ID

        Parameters
        ----------
        history_item_id : str
            ID of the history item to be used. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteHistoryItemResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.history.delete(
            history_item_id="VW7YKqPnjY4h39yTbx2L",
        )
        """

        Validator(str).validate(history_item_id, "history_item_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/history/{{history_item_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("history_item_id", history_item_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteHistoryItemResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteHistoryItemResponse, response)
            )
        )

    @cast_models
    def get_audio(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Generator[bytes, None, None]:
        """
        Returns the audio of an history item.

        Parameters
        ----------
        history_item_id : str
            ID of the history item to be used. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            The audio file of the history item.

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.history.get_audio(
            history_item_id="VW7YKqPnjY4h39yTbx2L",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(str).validate(history_item_id, "history_item_id")

        resolved_config = self._get_resolved_config(
            self._get_audio_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/history/{{history_item_id}}/audio",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("history_item_id", history_item_id)
            .serialize()
            .set_method("GET")
            .set_binary_download()
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def download(
        self,
        *,
        history_item_ids: List[str],
        output_format: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Download one or more history items. If one history item ID is provided, we will return a single audio file. If more than one history item IDs are provided, we will provide the history items packed into a .zip file.

        Parameters
        ----------
        history_item_ids : typing.Sequence[str]
            A list of history items to download, you can get IDs of history items and other metadata using the GET https://api.elevenlabs.io/v1/history endpoint.

        output_format : typing.Optional[str]
            Output format to transcode the audio file, can be wav or default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            The requested audio file, or a zip file containing multiple audio files when multiple history items are requested.

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.history.download(
            history_item_ids=[
                "history_item_ids"
            ],
            output_format="output_format",
        )
        for chunk in response:
            print(chunk)
        """

        resolved_config = self._get_resolved_config(
            self._download_config, request_options
        )

        request_body = DownloadHistoryRequest(
            history_item_ids=history_item_ids,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"output_format": output_format}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(DownloadHistoryRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/history/download",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response


class RawHistoryClient:
    """
    Raw-response client for HistoryClient.

    Each method delegates to the matching :class:`HistoryClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: HistoryClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        start_after_history_item_id: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        date_before_unix: Union[int, None] = SENTINEL,
        date_after_unix: Union[int, None] = SENTINEL,
        sort_direction: Union[ListSortDirection, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        source: Union[Source, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSpeechHistoryResponse]:
        data = HistoryClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "start_after_history_item_id": start_after_history_item_id,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "date_before_unix": date_before_unix,
                        "date_after_unix": date_after_unix,
                        "sort_direction": sort_direction,
                        "search": search,
                        "source": source,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[SpeechHistoryItemResponse]:
        data = HistoryClient.get(
            self._client, history_item_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteHistoryItemResponse]:
        data = HistoryClient.delete(
            self._client, history_item_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_audio(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = HistoryClient.get_audio(
            _call_client, history_item_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def download(
        self,
        *,
        history_item_ids: List[str],
        output_format: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = HistoryClient.download(
            _call_client,
            history_item_ids=history_item_ids,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"output_format": output_format}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )


class AsyncHistoryClient(HistoryClient):
    """
    Async wrapper for HistoryClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawHistoryClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawHistoryClient(self)

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        start_after_history_item_id: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        date_before_unix: Union[int, None] = SENTINEL,
        date_after_unix: Union[int, None] = SENTINEL,
        sort_direction: Union[ListSortDirection, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        source: Union[Source, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetSpeechHistoryResponse]:  # type: ignore[override]
        """
        Returns a list of your generated audio (e.g. text to speech, speech to speech, Studio, dubbing). Music and SFX generations are not included and cannot currently be retrieved via the API.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many history items to return at maximum. Can not exceed 1000, defaults to 100.

        start_after_history_item_id : typing.Optional[str]
            After which ID to start fetching, use this parameter to paginate across a large collection of history items. In case this parameter is not provided history items will be fetched starting from the most recently created one ordered descending by their creation date.

        voice_id : typing.Optional[str]
            ID of the voice to be filtered for. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        model_id : typing.Optional[str]
            Search term used for filtering history items. If provided, source becomes required.

        date_before_unix : typing.Optional[int]
            Unix timestamp to filter history items before this date (exclusive).

        date_after_unix : typing.Optional[int]
            Unix timestamp to filter history items after this date (inclusive).

        sort_direction : typing.Optional[ListSortDirection]
            Sort direction for the results.

        search : typing.Optional[str]
            search term used for filtering

        source : typing.Optional[Source]
            Source of the generated history item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSpeechHistoryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import ListSortDirection, Source

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.history.list(
                page_size=100,
                start_after_history_item_id="start_after_history_item_id",
                voice_id="voice_id",
                model_id="model_id",
                date_before_unix=8,
                date_after_unix=2,
                sort_direction="asc",
                search="search",
                source="TTS",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "start_after_history_item_id": start_after_history_item_id,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "date_before_unix": date_before_unix,
                        "date_after_unix": date_after_unix,
                        "sort_direction": sort_direction,
                        "search": search,
                        "source": source,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[SpeechHistoryItemResponse]:  # type: ignore[override]
        """
        Retrieves a history item.

        Parameters
        ----------
        history_item_id : str
            ID of the history item to be used. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeechHistoryItemResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.history.get(
                history_item_id="VW7YKqPnjY4h39yTbx2L",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(history_item_id, request_options=request_options)

    def delete(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DeleteHistoryItemResponse]:  # type: ignore[override]
        """
        Delete a history item by its ID

        Parameters
        ----------
        history_item_id : str
            ID of the history item to be used. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteHistoryItemResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.history.delete(
                history_item_id="VW7YKqPnjY4h39yTbx2L",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            history_item_id, request_options=request_options
        )

    def get_audio(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Returns the audio of an history item.

        Parameters
        ----------
        history_item_id : str
            ID of the history item to be used. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The audio file of the history item.

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.history.get_audio(
                history_item_id="VW7YKqPnjY4h39yTbx2L",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().get_audio(
            history_item_id, request_options=request_options
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

    def download(
        self,
        *,
        history_item_ids: List[str],
        output_format: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Download one or more history items. If one history item ID is provided, we will return a single audio file. If more than one history item IDs are provided, we will provide the history items packed into a .zip file.

        Parameters
        ----------
        history_item_ids : typing.Sequence[str]
            A list of history items to download, you can get IDs of history items and other metadata using the GET https://api.elevenlabs.io/v1/history endpoint.

        output_format : typing.Optional[str]
            Output format to transcode the audio file, can be wav or default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The requested audio file, or a zip file containing multiple audio files when multiple history items are requested.

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.history.download(
                history_item_ids=[
                    "history_item_ids"
                ],
                output_format="output_format",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().download(
            history_item_ids=history_item_ids,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"output_format": output_format}.items()
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


class AsyncRawHistoryClient:
    """
    Async raw-response client for AsyncHistoryClient.
    """

    def __init__(self, client: AsyncHistoryClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        start_after_history_item_id: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        date_before_unix: Union[int, None] = SENTINEL,
        date_after_unix: Union[int, None] = SENTINEL,
        sort_direction: Union[ListSortDirection, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        source: Union[Source, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSpeechHistoryResponse]:
        data = await AsyncHistoryClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "start_after_history_item_id": start_after_history_item_id,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "date_before_unix": date_before_unix,
                        "date_after_unix": date_after_unix,
                        "sort_direction": sort_direction,
                        "search": search,
                        "source": source,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[SpeechHistoryItemResponse]:
        data = await AsyncHistoryClient.get(
            self._client, history_item_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteHistoryItemResponse]:
        data = await AsyncHistoryClient.delete(
            self._client, history_item_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_audio(
        self, history_item_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncHistoryClient.get_audio(
            _call_client, history_item_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def download(
        self,
        *,
        history_item_ids: List[str],
        output_format: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncHistoryClient.download(
            _call_client,
            history_item_ids=history_item_ids,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"output_format": output_format}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )
