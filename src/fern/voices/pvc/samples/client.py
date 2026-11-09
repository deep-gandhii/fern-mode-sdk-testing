from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    AddVoiceResponseModel,
    BodyAddSamplesToPvcVoiceV1VoicesPvcVoiceIdSamplesPost,
    BodyUpdatePvcVoiceSampleV1VoicesPvcVoiceIdSamplesSampleIdPost,
    DeleteVoiceSampleResponseModel,
    HttpValidationError,
    VoiceSample,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .audio.client import (
        AudioClient as _AudioClient,
        AsyncAudioClient as _AsyncAudioClient,
    )
    from .speakers.client import (
        SpeakersClient as _SpeakersClient,
        AsyncSpeakersClient as _AsyncSpeakersClient,
    )
    from .waveform.client import (
        WaveformClient as _WaveformClient,
        AsyncWaveformClient as _AsyncWaveformClient,
    )


class SamplesClient(BaseService):
    """
    Fern-style resource client for SamplesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._audio: Any = None
        self._speakers: Any = None
        self._waveform: Any = None
        self._create_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    @property
    def audio(self) -> "_AudioClient":
        """Lazily construct and return the audio sub-resource client."""
        if self._audio is None:
            from .audio.client import AudioClient

            _child = AudioClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audio = _child
        return self._audio

    @property
    def speakers(self) -> "_SpeakersClient":
        """Lazily construct and return the speakers sub-resource client."""
        if self._speakers is None:
            from .speakers.client import SpeakersClient

            _child = SpeakersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speakers = _child
        return self._speakers

    @property
    def waveform(self) -> "_WaveformClient":
        """Lazily construct and return the waveform sub-resource client."""
        if self._waveform is None:
            from .waveform.client import WaveformClient

            _child = WaveformClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._waveform = _child
        return self._waveform

    def set_base_url(self, base_url: Union[ElevenLabsEnvironment, str]):
        """
        Sets the base URL for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's base URL and then cached, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error.

        :param base_url: The base URL to be set, as a string or an ElevenLabsEnvironment enum member.
        :return: The resource client.
        """
        super().set_base_url(base_url)
        if self._audio is not None:
            self._audio.set_base_url(base_url)
        if self._speakers is not None:
            self._speakers.set_base_url(base_url)
        if self._waveform is not None:
            self._waveform.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for this resource client and every sub-resource client
        already built.

        A child is constructed holding a reference to this client's config and is then cached,
        and both this setter and `set_retry` REBIND `_service_config` rather than mutating it --
        so an already-materialised child kept the config it was born with. The parent wins:
        last writer overwrites, the same rule `set_base_url` and `set_timeout` follow, which keeps
        a client and its children in exact agreement. Narrower scopes are untouched, because
        method-level config (`set_<method>_config`) and per-call `request_options` live in their
        own attributes and are never overwritten by this.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The resource client.
        """
        super().set_config(config)
        if self._audio is not None:
            self._audio.set_config(config)
        if self._speakers is not None:
            self._speakers.set_config(config)
        if self._waveform is not None:
            self._waveform.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's timeout and its request handler is
        built from it, so the inherited setter -- which only rebinds the receiver and rebuilds the
        receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The resource client.
        """
        super().set_timeout(timeout)
        if self._audio is not None:
            self._audio.set_timeout(timeout)
        if self._speakers is not None:
            self._speakers.set_timeout(timeout)
        if self._waveform is not None:
            self._waveform.set_timeout(timeout)

        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

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
    def with_raw_response(self) -> "RawSamplesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSamplesClient(self)

    @cast_models
    def create(
        self,
        voice_id: str,
        *,
        files: List[bytes],
        remove_background_noise: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> List[VoiceSample]:
        """
        Add audio samples to a PVC voice

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        files : typing.Sequence[core.File]
            Audio files used to create the voice.

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[VoiceSample]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.samples.create(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            files=[
                "files"
            ],
            remove_background_noise=True,
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyAddSamplesToPvcVoiceV1VoicesPvcVoiceIdSamplesPost(
            files=files,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyAddSamplesToPvcVoiceV1VoicesPvcVoiceIdSamplesPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}/samples",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            [
                VoiceSample.model_validate(item)
                for item in (response if isinstance(response, list) else [])
            ]
            if should_validate_response(resolved_config)
            else construct_lenient(
                List[VoiceSample], (response if isinstance(response, list) else [])
            )
        )

    @cast_models
    def update(
        self,
        voice_id: str,
        sample_id: str,
        *,
        remove_background_noise: Optional[bool] = SENTINEL,
        selected_speaker_ids: Union[List[str], None] = SENTINEL,
        trim_start_time: Union[int, None] = SENTINEL,
        trim_end_time: Union[int, None] = SENTINEL,
        file_name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddVoiceResponseModel:
        """
        Update a PVC voice sample - apply noise removal, select speaker, change trim times or file name.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        sample_id : str
            Sample ID to be used

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        selected_speaker_ids : typing.Optional[typing.Sequence[str]]
            Speaker IDs to be used for PVC training. Make sure you send all the speaker IDs you want to use for PVC training in one request because the last request will override the previous ones.

        trim_start_time : typing.Optional[int]
            The start time of the audio to be used for PVC training. Time should be in milliseconds

        trim_end_time : typing.Optional[int]
            The end time of the audio to be used for PVC training. Time should be in milliseconds

        file_name : typing.Optional[str]
            The name of the audio file to be used for PVC training.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddVoiceResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.samples.update(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            sample_id="VW7YKqPnjY4h39yTbx2L",
            remove_background_noise=True,
            selected_speaker_ids=[
                "selected_speaker_ids"
            ],
            trim_start_time=2,
            trim_end_time=8,
            file_name="file_name",
        )
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(str).validate(sample_id, "sample_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdatePvcVoiceSampleV1VoicesPvcVoiceIdSamplesSampleIdPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise,
                        "selected_speaker_ids": selected_speaker_ids,
                        "trim_start_time": trim_start_time,
                        "trim_end_time": trim_end_time,
                        "file_name": file_name,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyUpdatePvcVoiceSampleV1VoicesPvcVoiceIdSamplesSampleIdPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}/samples/{{sample_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_path("sample_id", sample_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddVoiceResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddVoiceResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> DeleteVoiceSampleResponseModel:
        """
        Delete a sample from a PVC voice.

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
        DeleteVoiceSampleResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.samples.delete(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            sample_id="VW7YKqPnjY4h39yTbx2L",
        )
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(str).validate(sample_id, "sample_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}/samples/{{sample_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_path("sample_id", sample_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteVoiceSampleResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteVoiceSampleResponseModel, response)
            )
        )


class RawSamplesClient:
    """
    Raw-response client for SamplesClient.

    Each method delegates to the matching :class:`SamplesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SamplesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        voice_id: str,
        *,
        files: List[bytes],
        remove_background_noise: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[List[VoiceSample]]:
        data = SamplesClient.create(
            self._client,
            voice_id,
            files=files,
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

    def update(
        self,
        voice_id: str,
        sample_id: str,
        *,
        remove_background_noise: Optional[bool] = SENTINEL,
        selected_speaker_ids: Union[List[str], None] = SENTINEL,
        trim_start_time: Union[int, None] = SENTINEL,
        trim_end_time: Union[int, None] = SENTINEL,
        file_name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceResponseModel]:
        data = SamplesClient.update(
            self._client,
            voice_id,
            sample_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise,
                        "selected_speaker_ids": selected_speaker_ids,
                        "trim_start_time": trim_start_time,
                        "trim_end_time": trim_end_time,
                        "file_name": file_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteVoiceSampleResponseModel]:
        data = SamplesClient.delete(
            self._client, voice_id, sample_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSamplesClient(SamplesClient):
    """
    Async wrapper for SamplesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def audio(self) -> "_AsyncAudioClient":
        """Lazily construct and return the async audio sub-resource client."""
        if self._audio is None:
            from .audio.client import AsyncAudioClient

            _child = AsyncAudioClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audio = _child
        return self._audio

    @property
    def speakers(self) -> "_AsyncSpeakersClient":
        """Lazily construct and return the async speakers sub-resource client."""
        if self._speakers is None:
            from .speakers.client import AsyncSpeakersClient

            _child = AsyncSpeakersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speakers = _child
        return self._speakers

    @property
    def waveform(self) -> "_AsyncWaveformClient":
        """Lazily construct and return the async waveform sub-resource client."""
        if self._waveform is None:
            from .waveform.client import AsyncWaveformClient

            _child = AsyncWaveformClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._waveform = _child
        return self._waveform

    @property
    def with_raw_response(self) -> "AsyncRawSamplesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSamplesClient(self)

    def create(
        self,
        voice_id: str,
        *,
        files: List[bytes],
        remove_background_noise: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[List[VoiceSample]]:  # type: ignore[override]
        """
        Add audio samples to a PVC voice

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        files : typing.Sequence[core.File]
            Audio files used to create the voice.

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[VoiceSample]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.samples.create(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                files=[
                    "files"
                ],
                remove_background_noise=True,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            voice_id,
            files=files,
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

    def update(
        self,
        voice_id: str,
        sample_id: str,
        *,
        remove_background_noise: Optional[bool] = SENTINEL,
        selected_speaker_ids: Union[List[str], None] = SENTINEL,
        trim_start_time: Union[int, None] = SENTINEL,
        trim_end_time: Union[int, None] = SENTINEL,
        file_name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddVoiceResponseModel]:  # type: ignore[override]
        """
        Update a PVC voice sample - apply noise removal, select speaker, change trim times or file name.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        sample_id : str
            Sample ID to be used

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        selected_speaker_ids : typing.Optional[typing.Sequence[str]]
            Speaker IDs to be used for PVC training. Make sure you send all the speaker IDs you want to use for PVC training in one request because the last request will override the previous ones.

        trim_start_time : typing.Optional[int]
            The start time of the audio to be used for PVC training. Time should be in milliseconds

        trim_end_time : typing.Optional[int]
            The end time of the audio to be used for PVC training. Time should be in milliseconds

        file_name : typing.Optional[str]
            The name of the audio file to be used for PVC training.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddVoiceResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.samples.update(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                sample_id="VW7YKqPnjY4h39yTbx2L",
                remove_background_noise=True,
                selected_speaker_ids=[
                    "selected_speaker_ids"
                ],
                trim_start_time=2,
                trim_end_time=8,
                file_name="file_name",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            voice_id,
            sample_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise,
                        "selected_speaker_ids": selected_speaker_ids,
                        "trim_start_time": trim_start_time,
                        "trim_end_time": trim_end_time,
                        "file_name": file_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DeleteVoiceSampleResponseModel]:  # type: ignore[override]
        """
        Delete a sample from a PVC voice.

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
        DeleteVoiceSampleResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.samples.delete(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                sample_id="VW7YKqPnjY4h39yTbx2L",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            voice_id, sample_id, request_options=request_options
        )


class AsyncRawSamplesClient:
    """
    Async raw-response client for AsyncSamplesClient.
    """

    def __init__(self, client: AsyncSamplesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        voice_id: str,
        *,
        files: List[bytes],
        remove_background_noise: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[List[VoiceSample]]:
        data = await AsyncSamplesClient.create(
            self._client,
            voice_id,
            files=files,
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

    async def update(
        self,
        voice_id: str,
        sample_id: str,
        *,
        remove_background_noise: Optional[bool] = SENTINEL,
        selected_speaker_ids: Union[List[str], None] = SENTINEL,
        trim_start_time: Union[int, None] = SENTINEL,
        trim_end_time: Union[int, None] = SENTINEL,
        file_name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceResponseModel]:
        data = await AsyncSamplesClient.update(
            self._client,
            voice_id,
            sample_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise,
                        "selected_speaker_ids": selected_speaker_ids,
                        "trim_start_time": trim_start_time,
                        "trim_end_time": trim_end_time,
                        "file_name": file_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteVoiceSampleResponseModel]:
        data = await AsyncSamplesClient.delete(
            self._client, voice_id, sample_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
