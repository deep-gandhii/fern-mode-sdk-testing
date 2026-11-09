from typing import Any, Optional, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.sentinel import SENTINEL
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import HttpValidationError, VoiceSamplePreviewResponseModel
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class AudioClient(BaseService):
    """
    Fern-style resource client for AudioClient.
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
    def with_raw_response(self) -> "RawAudioClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAudioClient(self)

    @cast_models
    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        remove_background_noise: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> VoiceSamplePreviewResponseModel:
        """
        Retrieve the first 30 seconds of voice sample audio with or without noise removal.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        sample_id : str
            Sample ID to be used

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceSamplePreviewResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.samples.audio.get(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            sample_id="VW7YKqPnjY4h39yTbx2L",
            remove_background_noise=True,
        )
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(str).validate(sample_id, "sample_id")
        Validator(bool).is_optional().is_nullable().validate(
            remove_background_noise, "remove_background_noise"
        )

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}/samples/{{sample_id}}/audio",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_path("sample_id", sample_id)
            .add_query(
                "remove_background_noise", remove_background_noise, nullable=True
            )
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                VoiceSamplePreviewResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(VoiceSamplePreviewResponseModel, response)
            )
        )


class RawAudioClient:
    """
    Raw-response client for AudioClient.

    Each method delegates to the matching :class:`AudioClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AudioClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        remove_background_noise: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceSamplePreviewResponseModel]:
        data = AudioClient.get(
            self._client,
            voice_id,
            sample_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncAudioClient(AudioClient):
    """
    Async wrapper for AudioClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAudioClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAudioClient(self)

    def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        remove_background_noise: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[VoiceSamplePreviewResponseModel]:  # type: ignore[override]
        """
        Retrieve the first 30 seconds of voice sample audio with or without noise removal.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        sample_id : str
            Sample ID to be used

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceSamplePreviewResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.samples.audio.get(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                sample_id="VW7YKqPnjY4h39yTbx2L",
                remove_background_noise=True,
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            voice_id,
            sample_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawAudioClient:
    """
    Async raw-response client for AsyncAudioClient.
    """

    def __init__(self, client: AsyncAudioClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        voice_id: str,
        sample_id: str,
        *,
        remove_background_noise: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceSamplePreviewResponseModel]:
        data = await AsyncAudioClient.get(
            self._client,
            voice_id,
            sample_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
