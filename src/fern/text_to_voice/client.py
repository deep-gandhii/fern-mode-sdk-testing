from typing import Any, Optional, Dict, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AllowedOutputFormats,
    BodyCreateANewVoiceFromVoicePreviewV1TextToVoicePost,
    HttpValidationError,
    Voice,
    VoiceDesignPreviewResponse,
    VoiceDesignRequest,
    VoiceDesignRequestModel,
    VoiceDesignRequestModelModelId,
    VoiceRemixRequestModel,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .preview.client import (
        PreviewClient as _PreviewClient,
        AsyncPreviewClient as _AsyncPreviewClient,
    )


class TextToVoiceClient(BaseService):
    """
    Fern-style resource client for TextToVoiceClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._preview: Any = None
        self._create_previews_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._design_config: SdkConfig = {}
        self._remix_config: SdkConfig = {}

    @property
    def preview(self) -> "_PreviewClient":
        """Lazily construct and return the preview sub-resource client."""
        if self._preview is None:
            from .preview.client import PreviewClient

            _child = PreviewClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._preview = _child
        return self._preview

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
        if self._preview is not None:
            self._preview.set_base_url(base_url)

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
        if self._preview is not None:
            self._preview.set_config(config)

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
        if self._preview is not None:
            self._preview.set_timeout(timeout)

        return self

    def set_create_previews_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_previews.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_previews_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_design_config(self, config: SdkConfig):
        """
        Sets method-level configuration for design.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._design_config = config
        return self

    def set_remix_config(self, config: SdkConfig):
        """
        Sets method-level configuration for remix.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._remix_config = config
        return self

    @property
    def with_raw_response(self) -> "RawTextToVoiceClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTextToVoiceClient(self)

    @cast_models
    def create_previews(
        self,
        *,
        voice_description: str,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        quality: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        should_enhance: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> VoiceDesignPreviewResponse:
        """
        Create a voice from a text prompt.

        Parameters
        ----------
        voice_description : str
            Description to use for the created voice.

        text : typing.Optional[str]
            Text to generate, text length has to be between 100 and 1000.

        auto_generate_text : typing.Optional[bool]
            Whether to automatically generate a text suitable for the voice description.

        loudness : typing.Optional[float]
            Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.

        quality : typing.Optional[float]
            Higher quality results in better voice output but less variety.

        seed : typing.Optional[int]
            Random number that controls the voice generation. Same seed with same inputs produces same voice.

        guidance_scale : typing.Optional[float]
            Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.

        should_enhance : typing.Optional[bool]
            Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False

        output_format : typing.Optional[AllowedOutputFormats]
            The output format of the generated audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceDesignPreviewResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.text_to_voice.create_previews(
            output_format="mp3_22050_32",
            voice_description="A sassy squeaky mouse",
            text="in adnulla dolor cupidatatlaborislaboris consecteturtempor indoloreirure voluptate Duis dolor Excepteur",
            auto_generate_text=False,
            loudness=0.5,
            quality=0.9,
            seed=580133691,
            guidance_scale=5,
            should_enhance=True,
        )
        """

        Validator(AllowedOutputFormats).is_optional().is_nullable().validate(
            output_format, "output_format"
        )

        resolved_config = self._get_resolved_config(
            self._create_previews_config, request_options
        )

        request_body = VoiceDesignRequest(
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "quality": quality,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "should_enhance": should_enhance,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(VoiceDesignRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-voice/create-previews",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                VoiceDesignPreviewResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(VoiceDesignPreviewResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        voice_name: str,
        voice_description: str,
        generated_voice_id: str,
        labels: Union[Dict[str, str], None] = SENTINEL,
        played_not_selected_voice_ids: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Voice:
        """
        Create a voice from previously generated voice preview. This endpoint should be called after you fetched a generated_voice_id using POST /v1/text-to-voice/design or POST /v1/text-to-voice/:voice_id/remix.

        Parameters
        ----------
        voice_name : str
            Name to use for the created voice.

        voice_description : str
            Description to use for the created voice.

        generated_voice_id : str
            The generated_voice_id to create; obtain it from POST /v1/text-to-voice/design, POST /v1/text-to-voice/:voice_id/remix, or the response headers when generating previews.

        labels : typing.Optional[typing.Dict[str, str]]
            Optional, metadata to add to the created voice. Defaults to None.

        played_not_selected_voice_ids : typing.Optional[typing.Sequence[str]]
            List of voice ids that the user has played but not selected. Used for RLHF.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Voice
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.text_to_voice.create(
            voice_name="Sassy squeaky mouse",
            voice_description="A sassy squeaky mouse",
            generated_voice_id="37HceQefKmEi3bGovXjL",
            labels={},
            played_not_selected_voice_ids=[
                "played_not_selected_voice_ids"
            ],
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateANewVoiceFromVoicePreviewV1TextToVoicePost(
            voice_name=voice_name,
            voice_description=voice_description,
            generated_voice_id=generated_voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "labels": labels,
                        "played_not_selected_voice_ids": played_not_selected_voice_ids,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateANewVoiceFromVoicePreviewV1TextToVoicePost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-voice",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                Voice.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(Voice, response)
            )
        )

    @cast_models
    def design(
        self,
        *,
        voice_description: str,
        model_id: Optional[VoiceDesignRequestModelModelId] = SENTINEL,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        stream_previews: Optional[bool] = SENTINEL,
        should_enhance: Optional[bool] = SENTINEL,
        remixing_session_id: Union[str, None] = SENTINEL,
        remixing_session_iteration_id: Union[str, None] = SENTINEL,
        quality: Union[float, None] = SENTINEL,
        reference_audio_base_64: Union[str, None] = SENTINEL,
        prompt_strength: Union[float, None] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> VoiceDesignPreviewResponse:
        """
        Design a voice via a prompt. This method returns a list of voice previews. Each preview has a generated_voice_id and a sample of the voice as base64 encoded mp3 audio. To create a voice use the generated_voice_id of the preferred preview with the /v1/text-to-voice endpoint.

        Parameters
        ----------
        voice_description : str
            Description to use for the created voice.

        model_id : typing.Optional[VoiceDesignRequestModelModelId]
            Model to use for the voice generation. Possible values: eleven_multilingual_ttv_v2, eleven_ttv_v3.

        text : typing.Optional[str]
            Text to generate, text length has to be between 100 and 1000.

        auto_generate_text : typing.Optional[bool]
            Whether to automatically generate a text suitable for the voice description.

        loudness : typing.Optional[float]
            Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.

        seed : typing.Optional[int]
            Random number that controls the voice generation. Same seed with same inputs produces same voice.

        guidance_scale : typing.Optional[float]
            Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.

        stream_previews : typing.Optional[bool]
            Determines whether the Text to Voice previews should be included in the response. If true, only the generated IDs will be returned which can then be streamed via the /v1/text-to-voice/:generated_voice_id/stream endpoint.

        should_enhance : typing.Optional[bool]
            Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False

        remixing_session_id : typing.Optional[str]
            The remixing session id.

        remixing_session_iteration_id : typing.Optional[str]
            The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created.

        quality : typing.Optional[float]
            Higher quality results in better voice output but less variety.

        reference_audio_base_64 : typing.Optional[str]
            Reference audio to use for the voice generation. The audio should be base64 encoded. Only supported when using the  eleven_ttv_v3 model.

        prompt_strength : typing.Optional[float]
            Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceDesignPreviewResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.text_to_voice.design(
            output_format="mp3_22050_32",
            voice_description="A sassy squeaky mouse",
            model_id="eleven_multilingual_ttv_v2",
            text="animirure aliquip commodoadvoluptate doloreut est voluptate mollitsintcommodo culpa proident tempor sunt",
            auto_generate_text=False,
            loudness=0.5,
            seed=176056479,
            guidance_scale=5,
            stream_previews=True,
            should_enhance=True,
            remixing_session_id="remixing_session_id",
            remixing_session_iteration_id="remixing_session_iteration_id",
            quality=-0.74,
            reference_audio_base_64="reference_audio_base64",
            prompt_strength=0.73,
        )
        """

        Validator(AllowedOutputFormats).is_optional().is_nullable().validate(
            output_format, "output_format"
        )

        resolved_config = self._get_resolved_config(
            self._design_config, request_options
        )

        request_body = VoiceDesignRequestModel(
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "stream_previews": stream_previews,
                        "should_enhance": should_enhance,
                        "remixing_session_id": remixing_session_id,
                        "remixing_session_iteration_id": remixing_session_iteration_id,
                        "quality": quality,
                        "reference_audio_base_64": reference_audio_base_64,
                        "prompt_strength": prompt_strength,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(VoiceDesignRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-voice/design",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                VoiceDesignPreviewResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(VoiceDesignPreviewResponse, response)
            )
        )

    @cast_models
    def remix(
        self,
        voice_id: str,
        *,
        voice_description: str,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        stream_previews: Optional[bool] = SENTINEL,
        remixing_session_id: Union[str, None] = SENTINEL,
        remixing_session_iteration_id: Union[str, None] = SENTINEL,
        prompt_strength: Union[float, None] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> VoiceDesignPreviewResponse:
        """
        Remix an existing voice via a prompt. This method returns a list of voice previews. Each preview has a generated_voice_id and a sample of the voice as base64 encoded mp3 audio. To create a voice use the generated_voice_id of the preferred preview with the /v1/text-to-voice endpoint.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        voice_description : str
            Description of the changes to make to the voice.

        text : typing.Optional[str]
            Text to generate, text length has to be between 100 and 1000.

        auto_generate_text : typing.Optional[bool]
            Whether to automatically generate a text suitable for the voice description.

        loudness : typing.Optional[float]
            Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.

        seed : typing.Optional[int]
            Random number that controls the voice generation. Same seed with same inputs produces same voice.

        guidance_scale : typing.Optional[float]
            Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.

        stream_previews : typing.Optional[bool]
            Determines whether the Text to Voice previews should be included in the response. If true, only the generated IDs will be returned which can then be streamed via the /v1/text-to-voice/:generated_voice_id/stream endpoint.

        remixing_session_id : typing.Optional[str]
            The remixing session id.

        remixing_session_iteration_id : typing.Optional[str]
            The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created.

        prompt_strength : typing.Optional[float]
            Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceDesignPreviewResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.text_to_voice.remix(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            output_format="mp3_22050_32",
            voice_description="Make the voice have a higher pitch.",
            text="sed irure veniamamet velit ex ea inin sunt consectetur nonanim cupidatat amet reprehenderitex dolor nostrud in dolore",
            auto_generate_text=True,
            loudness=0.5,
            seed=1278439489,
            guidance_scale=5,
            stream_previews=True,
            remixing_session_id="remixing_session_id",
            remixing_session_iteration_id="remixing_session_iteration_id",
            prompt_strength=0.01,
        )
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(AllowedOutputFormats).is_optional().is_nullable().validate(
            output_format, "output_format"
        )

        resolved_config = self._get_resolved_config(self._remix_config, request_options)

        request_body = VoiceRemixRequestModel(
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "stream_previews": stream_previews,
                        "remixing_session_id": remixing_session_id,
                        "remixing_session_iteration_id": remixing_session_iteration_id,
                        "prompt_strength": prompt_strength,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(VoiceRemixRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/text-to-voice/{{voice_id}}/remix",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                VoiceDesignPreviewResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(VoiceDesignPreviewResponse, response)
            )
        )


class RawTextToVoiceClient:
    """
    Raw-response client for TextToVoiceClient.

    Each method delegates to the matching :class:`TextToVoiceClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TextToVoiceClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create_previews(
        self,
        *,
        voice_description: str,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        quality: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        should_enhance: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceDesignPreviewResponse]:
        data = TextToVoiceClient.create_previews(
            self._client,
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "quality": quality,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "should_enhance": should_enhance,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        voice_name: str,
        voice_description: str,
        generated_voice_id: str,
        labels: Union[Dict[str, str], None] = SENTINEL,
        played_not_selected_voice_ids: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Voice]:
        data = TextToVoiceClient.create(
            self._client,
            voice_name=voice_name,
            voice_description=voice_description,
            generated_voice_id=generated_voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "labels": labels,
                        "played_not_selected_voice_ids": played_not_selected_voice_ids,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def design(
        self,
        *,
        voice_description: str,
        model_id: Optional[VoiceDesignRequestModelModelId] = SENTINEL,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        stream_previews: Optional[bool] = SENTINEL,
        should_enhance: Optional[bool] = SENTINEL,
        remixing_session_id: Union[str, None] = SENTINEL,
        remixing_session_iteration_id: Union[str, None] = SENTINEL,
        quality: Union[float, None] = SENTINEL,
        reference_audio_base_64: Union[str, None] = SENTINEL,
        prompt_strength: Union[float, None] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceDesignPreviewResponse]:
        data = TextToVoiceClient.design(
            self._client,
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "stream_previews": stream_previews,
                        "should_enhance": should_enhance,
                        "remixing_session_id": remixing_session_id,
                        "remixing_session_iteration_id": remixing_session_iteration_id,
                        "quality": quality,
                        "reference_audio_base_64": reference_audio_base_64,
                        "prompt_strength": prompt_strength,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def remix(
        self,
        voice_id: str,
        *,
        voice_description: str,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        stream_previews: Optional[bool] = SENTINEL,
        remixing_session_id: Union[str, None] = SENTINEL,
        remixing_session_iteration_id: Union[str, None] = SENTINEL,
        prompt_strength: Union[float, None] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceDesignPreviewResponse]:
        data = TextToVoiceClient.remix(
            self._client,
            voice_id,
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "stream_previews": stream_previews,
                        "remixing_session_id": remixing_session_id,
                        "remixing_session_iteration_id": remixing_session_iteration_id,
                        "prompt_strength": prompt_strength,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncTextToVoiceClient(TextToVoiceClient):
    """
    Async wrapper for TextToVoiceClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def preview(self) -> "_AsyncPreviewClient":
        """Lazily construct and return the async preview sub-resource client."""
        if self._preview is None:
            from .preview.client import AsyncPreviewClient

            _child = AsyncPreviewClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._preview = _child
        return self._preview

    @property
    def with_raw_response(self) -> "AsyncRawTextToVoiceClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTextToVoiceClient(self)

    def create_previews(
        self,
        *,
        voice_description: str,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        quality: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        should_enhance: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[VoiceDesignPreviewResponse]:  # type: ignore[override]
        """
        Create a voice from a text prompt.

        Parameters
        ----------
        voice_description : str
            Description to use for the created voice.

        text : typing.Optional[str]
            Text to generate, text length has to be between 100 and 1000.

        auto_generate_text : typing.Optional[bool]
            Whether to automatically generate a text suitable for the voice description.

        loudness : typing.Optional[float]
            Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.

        quality : typing.Optional[float]
            Higher quality results in better voice output but less variety.

        seed : typing.Optional[int]
            Random number that controls the voice generation. Same seed with same inputs produces same voice.

        guidance_scale : typing.Optional[float]
            Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.

        should_enhance : typing.Optional[bool]
            Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False

        output_format : typing.Optional[AllowedOutputFormats]
            The output format of the generated audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceDesignPreviewResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.text_to_voice.create_previews(
                output_format="mp3_22050_32",
                voice_description="A sassy squeaky mouse",
                text="in adnulla dolor cupidatatlaborislaboris consecteturtempor indoloreirure voluptate Duis dolor Excepteur",
                auto_generate_text=False,
                loudness=0.5,
                quality=0.9,
                seed=580133691,
                guidance_scale=5,
                should_enhance=True,
            )


        asyncio.run(main())
        """
        return to_async(super().create_previews)(
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "quality": quality,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "should_enhance": should_enhance,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        voice_name: str,
        voice_description: str,
        generated_voice_id: str,
        labels: Union[Dict[str, str], None] = SENTINEL,
        played_not_selected_voice_ids: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Voice]:  # type: ignore[override]
        """
        Create a voice from previously generated voice preview. This endpoint should be called after you fetched a generated_voice_id using POST /v1/text-to-voice/design or POST /v1/text-to-voice/:voice_id/remix.

        Parameters
        ----------
        voice_name : str
            Name to use for the created voice.

        voice_description : str
            Description to use for the created voice.

        generated_voice_id : str
            The generated_voice_id to create; obtain it from POST /v1/text-to-voice/design, POST /v1/text-to-voice/:voice_id/remix, or the response headers when generating previews.

        labels : typing.Optional[typing.Dict[str, str]]
            Optional, metadata to add to the created voice. Defaults to None.

        played_not_selected_voice_ids : typing.Optional[typing.Sequence[str]]
            List of voice ids that the user has played but not selected. Used for RLHF.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Voice
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.text_to_voice.create(
                voice_name="Sassy squeaky mouse",
                voice_description="A sassy squeaky mouse",
                generated_voice_id="37HceQefKmEi3bGovXjL",
                labels={},
                played_not_selected_voice_ids=[
                    "played_not_selected_voice_ids"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            voice_name=voice_name,
            voice_description=voice_description,
            generated_voice_id=generated_voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "labels": labels,
                        "played_not_selected_voice_ids": played_not_selected_voice_ids,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def design(
        self,
        *,
        voice_description: str,
        model_id: Optional[VoiceDesignRequestModelModelId] = SENTINEL,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        stream_previews: Optional[bool] = SENTINEL,
        should_enhance: Optional[bool] = SENTINEL,
        remixing_session_id: Union[str, None] = SENTINEL,
        remixing_session_iteration_id: Union[str, None] = SENTINEL,
        quality: Union[float, None] = SENTINEL,
        reference_audio_base_64: Union[str, None] = SENTINEL,
        prompt_strength: Union[float, None] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[VoiceDesignPreviewResponse]:  # type: ignore[override]
        """
        Design a voice via a prompt. This method returns a list of voice previews. Each preview has a generated_voice_id and a sample of the voice as base64 encoded mp3 audio. To create a voice use the generated_voice_id of the preferred preview with the /v1/text-to-voice endpoint.

        Parameters
        ----------
        voice_description : str
            Description to use for the created voice.

        model_id : typing.Optional[VoiceDesignRequestModelModelId]
            Model to use for the voice generation. Possible values: eleven_multilingual_ttv_v2, eleven_ttv_v3.

        text : typing.Optional[str]
            Text to generate, text length has to be between 100 and 1000.

        auto_generate_text : typing.Optional[bool]
            Whether to automatically generate a text suitable for the voice description.

        loudness : typing.Optional[float]
            Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.

        seed : typing.Optional[int]
            Random number that controls the voice generation. Same seed with same inputs produces same voice.

        guidance_scale : typing.Optional[float]
            Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.

        stream_previews : typing.Optional[bool]
            Determines whether the Text to Voice previews should be included in the response. If true, only the generated IDs will be returned which can then be streamed via the /v1/text-to-voice/:generated_voice_id/stream endpoint.

        should_enhance : typing.Optional[bool]
            Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False

        remixing_session_id : typing.Optional[str]
            The remixing session id.

        remixing_session_iteration_id : typing.Optional[str]
            The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created.

        quality : typing.Optional[float]
            Higher quality results in better voice output but less variety.

        reference_audio_base_64 : typing.Optional[str]
            Reference audio to use for the voice generation. The audio should be base64 encoded. Only supported when using the  eleven_ttv_v3 model.

        prompt_strength : typing.Optional[float]
            Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceDesignPreviewResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.text_to_voice.design(
                output_format="mp3_22050_32",
                voice_description="A sassy squeaky mouse",
                model_id="eleven_multilingual_ttv_v2",
                text="animirure aliquip commodoadvoluptate doloreut est voluptate mollitsintcommodo culpa proident tempor sunt",
                auto_generate_text=False,
                loudness=0.5,
                seed=176056479,
                guidance_scale=5,
                stream_previews=True,
                should_enhance=True,
                remixing_session_id="remixing_session_id",
                remixing_session_iteration_id="remixing_session_iteration_id",
                quality=-0.74,
                reference_audio_base_64="reference_audio_base64",
                prompt_strength=0.73,
            )


        asyncio.run(main())
        """
        return to_async(super().design)(
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "stream_previews": stream_previews,
                        "should_enhance": should_enhance,
                        "remixing_session_id": remixing_session_id,
                        "remixing_session_iteration_id": remixing_session_iteration_id,
                        "quality": quality,
                        "reference_audio_base_64": reference_audio_base_64,
                        "prompt_strength": prompt_strength,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def remix(
        self,
        voice_id: str,
        *,
        voice_description: str,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        stream_previews: Optional[bool] = SENTINEL,
        remixing_session_id: Union[str, None] = SENTINEL,
        remixing_session_iteration_id: Union[str, None] = SENTINEL,
        prompt_strength: Union[float, None] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[VoiceDesignPreviewResponse]:  # type: ignore[override]
        """
        Remix an existing voice via a prompt. This method returns a list of voice previews. Each preview has a generated_voice_id and a sample of the voice as base64 encoded mp3 audio. To create a voice use the generated_voice_id of the preferred preview with the /v1/text-to-voice endpoint.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        voice_description : str
            Description of the changes to make to the voice.

        text : typing.Optional[str]
            Text to generate, text length has to be between 100 and 1000.

        auto_generate_text : typing.Optional[bool]
            Whether to automatically generate a text suitable for the voice description.

        loudness : typing.Optional[float]
            Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.

        seed : typing.Optional[int]
            Random number that controls the voice generation. Same seed with same inputs produces same voice.

        guidance_scale : typing.Optional[float]
            Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.

        stream_previews : typing.Optional[bool]
            Determines whether the Text to Voice previews should be included in the response. If true, only the generated IDs will be returned which can then be streamed via the /v1/text-to-voice/:generated_voice_id/stream endpoint.

        remixing_session_id : typing.Optional[str]
            The remixing session id.

        remixing_session_iteration_id : typing.Optional[str]
            The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created.

        prompt_strength : typing.Optional[float]
            Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceDesignPreviewResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.text_to_voice.remix(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                output_format="mp3_22050_32",
                voice_description="Make the voice have a higher pitch.",
                text="sed irure veniamamet velit ex ea inin sunt consectetur nonanim cupidatat amet reprehenderitex dolor nostrud in dolore",
                auto_generate_text=True,
                loudness=0.5,
                seed=1278439489,
                guidance_scale=5,
                stream_previews=True,
                remixing_session_id="remixing_session_id",
                remixing_session_iteration_id="remixing_session_iteration_id",
                prompt_strength=0.01,
            )


        asyncio.run(main())
        """
        return to_async(super().remix)(
            voice_id,
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "stream_previews": stream_previews,
                        "remixing_session_id": remixing_session_id,
                        "remixing_session_iteration_id": remixing_session_iteration_id,
                        "prompt_strength": prompt_strength,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawTextToVoiceClient:
    """
    Async raw-response client for AsyncTextToVoiceClient.
    """

    def __init__(self, client: AsyncTextToVoiceClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create_previews(
        self,
        *,
        voice_description: str,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        quality: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        should_enhance: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceDesignPreviewResponse]:
        data = await AsyncTextToVoiceClient.create_previews(
            self._client,
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "quality": quality,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "should_enhance": should_enhance,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        voice_name: str,
        voice_description: str,
        generated_voice_id: str,
        labels: Union[Dict[str, str], None] = SENTINEL,
        played_not_selected_voice_ids: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Voice]:
        data = await AsyncTextToVoiceClient.create(
            self._client,
            voice_name=voice_name,
            voice_description=voice_description,
            generated_voice_id=generated_voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "labels": labels,
                        "played_not_selected_voice_ids": played_not_selected_voice_ids,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def design(
        self,
        *,
        voice_description: str,
        model_id: Optional[VoiceDesignRequestModelModelId] = SENTINEL,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        stream_previews: Optional[bool] = SENTINEL,
        should_enhance: Optional[bool] = SENTINEL,
        remixing_session_id: Union[str, None] = SENTINEL,
        remixing_session_iteration_id: Union[str, None] = SENTINEL,
        quality: Union[float, None] = SENTINEL,
        reference_audio_base_64: Union[str, None] = SENTINEL,
        prompt_strength: Union[float, None] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceDesignPreviewResponse]:
        data = await AsyncTextToVoiceClient.design(
            self._client,
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "stream_previews": stream_previews,
                        "should_enhance": should_enhance,
                        "remixing_session_id": remixing_session_id,
                        "remixing_session_iteration_id": remixing_session_iteration_id,
                        "quality": quality,
                        "reference_audio_base_64": reference_audio_base_64,
                        "prompt_strength": prompt_strength,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def remix(
        self,
        voice_id: str,
        *,
        voice_description: str,
        text: Union[str, None] = SENTINEL,
        auto_generate_text: Optional[bool] = SENTINEL,
        loudness: Optional[float] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        guidance_scale: Optional[float] = SENTINEL,
        stream_previews: Optional[bool] = SENTINEL,
        remixing_session_id: Union[str, None] = SENTINEL,
        remixing_session_iteration_id: Union[str, None] = SENTINEL,
        prompt_strength: Union[float, None] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceDesignPreviewResponse]:
        data = await AsyncTextToVoiceClient.remix(
            self._client,
            voice_id,
            voice_description=voice_description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "auto_generate_text": auto_generate_text,
                        "loudness": loudness,
                        "seed": seed,
                        "guidance_scale": guidance_scale,
                        "stream_previews": stream_previews,
                        "remixing_session_id": remixing_session_id,
                        "remixing_session_iteration_id": remixing_session_iteration_id,
                        "prompt_strength": prompt_strength,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
