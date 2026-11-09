from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types.transcripts_get_response import TranscriptsGetResponse_adapter
from ...types import HttpValidationError, TranscriptsGetResponse
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
        self._delete_config: SdkConfig = {}

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
        self, transcription_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> TranscriptsGetResponse:
        """
        Retrieve a previously generated transcript by its ID.

        Parameters
        ----------
        transcription_id : str
            The unique ID of the transcript to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptsGetResponse
            The transcript data

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.speech_to_text.transcripts.get(
            transcription_id="transcription_id",
        )
        """

        Validator(str).validate(transcription_id, "transcription_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-to-text/transcripts/{{transcription_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("transcription_id", transcription_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                TranscriptsGetResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(TranscriptsGetResponse, response)
            )
        )

    @cast_models
    def delete(
        self, transcription_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Any:
        """
        Delete a previously generated transcript by its ID.

        Parameters
        ----------
        transcription_id : str
            The unique ID of the transcript to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Delete completed successfully.

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.speech_to_text.transcripts.delete(
            transcription_id="transcription_id",
        )
        """

        Validator(str).validate(transcription_id, "transcription_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-to-text/transcripts/{{transcription_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("transcription_id", transcription_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


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
        self, transcription_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[TranscriptsGetResponse]:
        data = TranscriptsClient.get(
            self._client, transcription_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, transcription_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = TranscriptsClient.delete(
            self._client, transcription_id, request_options=request_options
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
        self, transcription_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[TranscriptsGetResponse]:  # type: ignore[override]
        """
        Retrieve a previously generated transcript by its ID.

        Parameters
        ----------
        transcription_id : str
            The unique ID of the transcript to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptsGetResponse
            The transcript data

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.speech_to_text.transcripts.get(
                transcription_id="transcription_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(transcription_id, request_options=request_options)

    def delete(
        self, transcription_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete a previously generated transcript by its ID.

        Parameters
        ----------
        transcription_id : str
            The unique ID of the transcript to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Delete completed successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.speech_to_text.transcripts.delete(
                transcription_id="transcription_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            transcription_id, request_options=request_options
        )


class AsyncRawTranscriptsClient:
    """
    Async raw-response client for AsyncTranscriptsClient.
    """

    def __init__(self, client: AsyncTranscriptsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, transcription_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[TranscriptsGetResponse]:
        data = await AsyncTranscriptsClient.get(
            self._client, transcription_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, transcription_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = await AsyncTranscriptsClient.delete(
            self._client, transcription_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
