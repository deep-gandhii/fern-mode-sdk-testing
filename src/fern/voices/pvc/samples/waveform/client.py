from typing import Any, Optional, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import HttpValidationError, VoiceSampleVisualWaveformResponseModel
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class WaveformClient(BaseService):
    """
    Fern-style resource client for WaveformClient.
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
    def with_raw_response(self) -> "RawWaveformClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawWaveformClient(self)

    @cast_models
    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> VoiceSampleVisualWaveformResponseModel:
        """
        Retrieve the visual waveform of a voice sample.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        sample_id : str
            Sample ID to be used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceSampleVisualWaveformResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.samples.waveform.get(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            sample_id="VW7YKqPnjY4h39yTbx2L",
        )
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(str).validate(sample_id, "sample_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}/samples/{{sample_id}}/waveform",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_path("sample_id", sample_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                VoiceSampleVisualWaveformResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(VoiceSampleVisualWaveformResponseModel, response)
            )
        )


class RawWaveformClient:
    """
    Raw-response client for WaveformClient.

    Each method delegates to the matching :class:`WaveformClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: WaveformClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceSampleVisualWaveformResponseModel]:
        data = WaveformClient.get(
            self._client, voice_id, sample_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncWaveformClient(WaveformClient):
    """
    Async wrapper for WaveformClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawWaveformClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawWaveformClient(self)

    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[VoiceSampleVisualWaveformResponseModel]:  # type: ignore[override]
        """
        Retrieve the visual waveform of a voice sample.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        sample_id : str
            Sample ID to be used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceSampleVisualWaveformResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.samples.waveform.get(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                sample_id="VW7YKqPnjY4h39yTbx2L",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            voice_id, sample_id, request_options=request_options
        )


class AsyncRawWaveformClient:
    """
    Async raw-response client for AsyncWaveformClient.
    """

    def __init__(self, client: AsyncWaveformClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceSampleVisualWaveformResponseModel]:
        data = await AsyncWaveformClient.get(
            self._client, voice_id, sample_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
