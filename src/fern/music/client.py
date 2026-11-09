from typing import Any, Optional, Generator, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AllowedOutputFormats,
    BodyComposeMusicV1MusicPost,
    BodyComposeMusicV1MusicPostCompositionPlan,
    BodyComposeMusicV1MusicPostModelId,
    BodyComposeMusicWithADetailedResponseV1MusicDetailedPost,
    BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan,
    BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId,
    BodyStemSeparationV1MusicStemSeparationPost,
    BodyStemSeparationV1MusicStemSeparationPostStemVariationId,
    BodyStreamComposedMusicV1MusicStreamPost,
    BodyStreamComposedMusicV1MusicStreamPostCompositionPlan,
    BodyStreamComposedMusicV1MusicStreamPostModelId,
    BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPost,
    BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostCompositionPlan,
    BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostModelId,
    BodyUploadMusicV1MusicUploadPost,
    BodyUploadMusicV1MusicUploadPostExtractCompositionPlan,
    BodyVideoToMusicV1MusicVideoToMusicPost,
    BodyVideoToMusicV1MusicVideoToMusicPostModelId,
    ComposeDetailedOutputFormat,
    ComposeDetailedStreamOutputFormat,
    ComposeOutputFormat,
    HttpValidationError,
    MusicComposeDetailedResponse,
    MusicUploadResponse,
    OutputFormatOfTheGeneratedAudio8,
)
from ..net.transport.serializer import Serializer
from ..net.transport.response import deserialize_sse_event
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .composition_plan.client import (
        CompositionPlanClient as _CompositionPlanClient,
        AsyncCompositionPlanClient as _AsyncCompositionPlanClient,
    )
    from .finetunes.client import (
        FinetunesClient as _FinetunesClient,
        AsyncFinetunesClient as _AsyncFinetunesClient,
    )


class MusicClient(BaseService):
    """
    Fern-style resource client for MusicClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._composition_plan: Any = None
        self._finetunes: Any = None
        self._video_to_music_config: SdkConfig = {}
        self._compose_config: SdkConfig = {}
        self._compose_detailed_config: SdkConfig = {}
        self._compose_detailed_stream_config: SdkConfig = {}
        self._stream_config: SdkConfig = {}
        self._upload_config: SdkConfig = {}
        self._separate_stems_config: SdkConfig = {}

    @property
    def composition_plan(self) -> "_CompositionPlanClient":
        """Lazily construct and return the composition_plan sub-resource client."""
        if self._composition_plan is None:
            from .composition_plan.client import CompositionPlanClient

            _child = CompositionPlanClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._composition_plan = _child
        return self._composition_plan

    @property
    def finetunes(self) -> "_FinetunesClient":
        """Lazily construct and return the finetunes sub-resource client."""
        if self._finetunes is None:
            from .finetunes.client import FinetunesClient

            _child = FinetunesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._finetunes = _child
        return self._finetunes

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
        if self._composition_plan is not None:
            self._composition_plan.set_base_url(base_url)
        if self._finetunes is not None:
            self._finetunes.set_base_url(base_url)

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
        if self._composition_plan is not None:
            self._composition_plan.set_config(config)
        if self._finetunes is not None:
            self._finetunes.set_config(config)

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
        if self._composition_plan is not None:
            self._composition_plan.set_timeout(timeout)
        if self._finetunes is not None:
            self._finetunes.set_timeout(timeout)

        return self

    def set_video_to_music_config(self, config: SdkConfig):
        """
        Sets method-level configuration for video_to_music.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._video_to_music_config = config
        return self

    def set_compose_config(self, config: SdkConfig):
        """
        Sets method-level configuration for compose.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._compose_config = config
        return self

    def set_compose_detailed_config(self, config: SdkConfig):
        """
        Sets method-level configuration for compose_detailed.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._compose_detailed_config = config
        return self

    def set_compose_detailed_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for compose_detailed_stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._compose_detailed_stream_config = config
        return self

    def set_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._stream_config = config
        return self

    def set_upload_config(self, config: SdkConfig):
        """
        Sets method-level configuration for upload.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._upload_config = config
        return self

    def set_separate_stems_config(self, config: SdkConfig):
        """
        Sets method-level configuration for separate_stems.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._separate_stems_config = config
        return self

    @property
    def with_raw_response(self) -> "RawMusicClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawMusicClient(self)

    @cast_models
    def video_to_music(
        self,
        *,
        videos: List[bytes],
        description: Union[str, None] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        model_id: Optional[BodyVideoToMusicV1MusicVideoToMusicPostModelId] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Generate background music from one or more video files. Videos are combined in order. Optional description and style tags influence the generated music.

        Parameters
        ----------
        videos : typing.Sequence[core.File]
            One or more video files sent via FormData array (multipart/form-data). They will be combined into one codec in order.
                        A maximum of 10 videos is allowed, where the total size of the combined video is limited to 200MB.
                        In total, the video can be up to 600 seconds long. Note that combining multiple videos may increase the request duration significantly. If possible, combine the videos beforehand.

        description : typing.Optional[str]
            Optional text description of the music you want. A maximum of 1000 characters is allowed.

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of style tags (e.g. ['upbeat', 'cinematic']). A maximum of 10 tags is allowed.

        model_id : typing.Optional[BodyVideoToMusicV1MusicVideoToMusicPostModelId]
            The model to use for the generation.

        sign_with_c_2_pa : typing.Optional[bool]
            Whether to sign the generated song with C2PA. Applicable only for mp3 files.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Generated audio file matching the video. Content-Type and file extension depend on the output_format parameter (default mp3).

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.music.video_to_music(
            output_format="mp3_22050_32",
            videos=[
                "videos"
            ],
            description="description",
            tags=[
                "tags"
            ],
            model_id="music_v1",
            sign_with_c_2_pa=False,
        )
        for chunk in response:
            print(chunk)
        """

        Validator(AllowedOutputFormats).is_optional().is_nullable().validate(
            output_format, "output_format"
        )

        resolved_config = self._get_resolved_config(
            self._video_to_music_config, request_options
        )

        request_body = BodyVideoToMusicV1MusicVideoToMusicPost(
            videos=videos,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "description": description,
                        "tags": tags,
                        "model_id": model_id,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyVideoToMusicV1MusicVideoToMusicPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/video-to-music",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body, "multipart/form-data")
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def compose(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyComposeMusicV1MusicPostCompositionPlan, None
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[BodyComposeMusicV1MusicPostModelId] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        respect_sections_durations: Optional[bool] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[ComposeOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Compose a song from a prompt or a composition plan.

        Parameters
        ----------
        prompt : typing.Optional[str]
            A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.

        composition_plan : typing.Optional[BodyComposeMusicV1MusicPostCompositionPlan]
            A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.

        music_length_ms : typing.Optional[int]
            The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        model_id : typing.Optional[BodyComposeMusicV1MusicPostModelId]
            The model to use for the generation.

        seed : typing.Optional[int]
            Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.

        force_instrumental : typing.Optional[bool]
            If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.

        finetune_id : typing.Optional[str]
            The ID of the finetune to use for the generation

        respect_sections_durations : typing.Optional[bool]
            Controls how strictly section durations in the `composition_plan` are enforced. Only used with `composition_plan` and only applies to `music_v1`; for `music_v2` section durations are always enforced and this is ignored. When false for `music_v1`, the model may adjust individual section durations for better quality and latency, while preserving the total song duration from the plan.

        store_for_inpainting : typing.Optional[bool]
            Whether to store the generated song for inpainting.

        sign_with_c_2_pa : typing.Optional[bool]
            Whether to sign the generated song with C2PA. Applicable only for mp3 files.

        output_format : typing.Optional[ComposeOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            The generated audio file in the format specified

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import ComposeOutputFormat

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.music.compose(
            output_format="auto",
            prompt="prompt",
            composition_plan={
                "positive_global_styles": [
                    "positive_global_styles"
                ],
                "negative_global_styles": [
                    "negative_global_styles"
                ],
                "sections": [
                    {
                        "section_name": "section_name",
                        "positive_local_styles": [
                            "positive_local_styles"
                        ],
                        "negative_local_styles": [
                            "negative_local_styles"
                        ],
                        "duration_ms": 9189,
                        "lines": [
                            "lines"
                        ],
                        "source_from": {
                            "song_id": "song_id",
                            "range": {
                                "start_ms": 9,
                                "end_ms": 4
                            },
                            "negative_ranges": [
                                {
                                    "start_ms": 9,
                                    "end_ms": 4
                                }
                            ]
                        }
                    }
                ]
            },
            music_length_ms=36319,
            model_id="music_v1",
            seed=1974260297,
            force_instrumental=False,
            finetune_id="finetune_id",
            respect_sections_durations=True,
            store_for_inpainting=True,
            sign_with_c_2_pa=True,
        )
        for chunk in response:
            print(chunk)
        """

        Validator(ComposeOutputFormat).is_optional().is_nullable().validate(
            output_format, "output_format"
        )

        resolved_config = self._get_resolved_config(
            self._compose_config, request_options
        )

        request_body = BodyComposeMusicV1MusicPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "respect_sections_durations": respect_sections_durations,
                        "store_for_inpainting": store_for_inpainting,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(BodyComposeMusicV1MusicPost).is_optional().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def compose_detailed(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan,
            None,
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        respect_sections_durations: Optional[bool] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[ComposeDetailedOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Compose a song from a prompt or a composition plan.

        Parameters
        ----------
        prompt : typing.Optional[str]
            A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.

        composition_plan : typing.Optional[BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan]
            A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.

        music_length_ms : typing.Optional[int]
            The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        model_id : typing.Optional[BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId]
            The model to use for the generation.

        seed : typing.Optional[int]
            Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.

        force_instrumental : typing.Optional[bool]
            If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.

        finetune_id : typing.Optional[str]
            The ID of the finetune to use for the generation

        respect_sections_durations : typing.Optional[bool]
            Controls how strictly section durations in the `composition_plan` are enforced. Only used with `composition_plan` and only applies to `music_v1`; for `music_v2` section durations are always enforced and this is ignored. When false for `music_v1`, the model may adjust individual section durations for better quality and latency, while preserving the total song duration from the plan.

        store_for_inpainting : typing.Optional[bool]
            Whether to store the generated song for inpainting.

        with_timestamps : typing.Optional[bool]
            Whether to return the timestamps of the words in the generated song.

        sign_with_c_2_pa : typing.Optional[bool]
            Whether to sign the generated song with C2PA. Applicable only for mp3 files.

        output_format : typing.Optional[ComposeDetailedOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Multipart/mixed response with JSON metadata and binary audio file

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import ComposeDetailedOutputFormat

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.music.compose_detailed(
            output_format="auto",
            prompt="A prompt for music generation",
            music_length_ms=10000,
        )
        for chunk in response:
            print(chunk)
        """

        Validator(ComposeDetailedOutputFormat).is_optional().is_nullable().validate(
            output_format, "output_format"
        )

        resolved_config = self._get_resolved_config(
            self._compose_detailed_config, request_options
        )

        request_body = BodyComposeMusicWithADetailedResponseV1MusicDetailedPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "respect_sections_durations": respect_sections_durations,
                        "store_for_inpainting": store_for_inpainting,
                        "with_timestamps": with_timestamps,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/detailed",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def compose_detailed_stream(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostCompositionPlan,
            None,
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostModelId
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        output_format: Union[ComposeDetailedStreamOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[str, None, None]:
        """
        Stream a song and its detailed metadata using Server-Sent Events (SSE).

        Parameters
        ----------
        prompt : typing.Optional[str]
            A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.

        composition_plan : typing.Optional[BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostCompositionPlan]
            A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.

        music_length_ms : typing.Optional[int]
            The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        model_id : typing.Optional[BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostModelId]
            The model to use for the generation.

        seed : typing.Optional[int]
            Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.

        force_instrumental : typing.Optional[bool]
            If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.

        finetune_id : typing.Optional[str]
            The ID of the finetune to use for the generation

        store_for_inpainting : typing.Optional[bool]
            Whether to store the generated song for inpainting.

        with_timestamps : typing.Optional[bool]
            Whether to return the timestamps of the words in the generated song.

        output_format : typing.Optional[ComposeDetailedStreamOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[str]
            Server-Sent Events for composition plan, song metadata, audio chunks with optional word timestamps, and completion.

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import ComposeDetailedStreamOutputFormat

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.music.compose_detailed_stream(
            output_format="auto",
            prompt="prompt",
            composition_plan={
                "positive_global_styles": [
                    "positive_global_styles"
                ],
                "negative_global_styles": [
                    "negative_global_styles"
                ],
                "sections": [
                    {
                        "section_name": "section_name",
                        "positive_local_styles": [
                            "positive_local_styles"
                        ],
                        "negative_local_styles": [
                            "negative_local_styles"
                        ],
                        "duration_ms": 9189,
                        "lines": [
                            "lines"
                        ],
                        "source_from": {
                            "song_id": "song_id",
                            "range": {
                                "start_ms": 9,
                                "end_ms": 4
                            },
                            "negative_ranges": [
                                {
                                    "start_ms": 9,
                                    "end_ms": 4
                                }
                            ]
                        }
                    }
                ]
            },
            music_length_ms=189956,
            model_id="music_v1",
            seed=1073974809,
            force_instrumental=False,
            finetune_id="finetune_id",
            store_for_inpainting=False,
            with_timestamps=True,
        )
        for chunk in response:
            print(chunk)
        """

        Validator(
            ComposeDetailedStreamOutputFormat
        ).is_optional().is_nullable().validate(output_format, "output_format")

        resolved_config = self._get_resolved_config(
            self._compose_detailed_stream_config, request_options
        )

        request_body = (
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPost(
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "prompt": prompt,
                            "composition_plan": composition_plan,
                            "music_length_ms": music_length_ms,
                            "model_id": model_id,
                            "seed": seed,
                            "force_instrumental": force_instrumental,
                            "finetune_id": finetune_id,
                            "store_for_inpainting": store_for_inpainting,
                            "with_timestamps": with_timestamps,
                        }.items()
                        if v is not SENTINEL
                    }
                )
            )
        )
        Validator(
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/detailed/stream",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_header("Accept", "text/event-stream")
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        for response, status, content in self.stream_request(serialized_request):
            yield response

    @cast_models
    def stream(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyStreamComposedMusicV1MusicStreamPostCompositionPlan, None
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[BodyStreamComposedMusicV1MusicStreamPostModelId] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio8, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Stream a composed song from a prompt or a composition plan.

        Parameters
        ----------
        prompt : typing.Optional[str]
            A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.

        composition_plan : typing.Optional[BodyStreamComposedMusicV1MusicStreamPostCompositionPlan]
            A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.

        music_length_ms : typing.Optional[int]
            The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        model_id : typing.Optional[BodyStreamComposedMusicV1MusicStreamPostModelId]
            The model to use for the generation.

        seed : typing.Optional[int]
            Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.

        force_instrumental : typing.Optional[bool]
            If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.

        finetune_id : typing.Optional[str]
            The ID of the finetune to use for the generation

        store_for_inpainting : typing.Optional[bool]
            Whether to store the generated song for inpainting.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio8]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Streaming audio data in the format specified

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio8

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.music.stream(
            output_format="auto",
            prompt="prompt",
            composition_plan={
                "positive_global_styles": [
                    "positive_global_styles"
                ],
                "negative_global_styles": [
                    "negative_global_styles"
                ],
                "sections": [
                    {
                        "section_name": "section_name",
                        "positive_local_styles": [
                            "positive_local_styles"
                        ],
                        "negative_local_styles": [
                            "negative_local_styles"
                        ],
                        "duration_ms": 9189,
                        "lines": [
                            "lines"
                        ],
                        "source_from": {
                            "song_id": "song_id",
                            "range": {
                                "start_ms": 9,
                                "end_ms": 4
                            },
                            "negative_ranges": [
                                {
                                    "start_ms": 9,
                                    "end_ms": 4
                                }
                            ]
                        }
                    }
                ]
            },
            music_length_ms=523967,
            model_id="music_v1",
            seed=1183754256,
            force_instrumental=False,
            finetune_id="finetune_id",
            store_for_inpainting=True,
        )
        for chunk in response:
            print(chunk)
        """

        Validator(
            OutputFormatOfTheGeneratedAudio8
        ).is_optional().is_nullable().validate(output_format, "output_format")

        resolved_config = self._get_resolved_config(
            self._stream_config, request_options
        )

        request_body = BodyStreamComposedMusicV1MusicStreamPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "store_for_inpainting": store_for_inpainting,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(BodyStreamComposedMusicV1MusicStreamPost).is_optional().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/stream",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def upload(
        self,
        *,
        file: bytes,
        extract_composition_plan: Optional[
            BodyUploadMusicV1MusicUploadPostExtractCompositionPlan
        ] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> MusicUploadResponse:
        """
        Upload a music file to be later used for inpainting. Price for uploading is the same as the one for song generation. All uploaded content gets inspected for copyright infringement. If copyrighted content is detected, half of the request cost is still charged.

        Parameters
        ----------
        file : core.File
            The audio file to upload.

        extract_composition_plan : typing.Optional[BodyUploadMusicV1MusicUploadPostExtractCompositionPlan]
            Whether to generate and return the composition plan for the uploaded song. Pass a model id (`music_v1` or `music_v2`) to control which composition plan format is returned. Passing `true`/`false` is deprecated; `true` defaults to the `music_v1` plan format. Enabling this will increase the latency.

        with_timestamps : typing.Optional[bool]
            Whether to transcribe the uploaded song and return word-level timestamps. If True, the response will include words_timestamps but will increase the latency.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicUploadResponse
            Successfully uploaded music file with optional composition plan

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.music.upload(
            file="file",
            extract_composition_plan=True,
            with_timestamps=False,
        )
        """

        resolved_config = self._get_resolved_config(
            self._upload_config, request_options
        )

        request_body = BodyUploadMusicV1MusicUploadPost(
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extract_composition_plan": extract_composition_plan,
                        "with_timestamps": with_timestamps,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyUploadMusicV1MusicUploadPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/upload",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                MusicUploadResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MusicUploadResponse, response)
            )
        )

    @cast_models
    def separate_stems(
        self,
        *,
        file: bytes,
        stem_variation_id: Optional[
            BodyStemSeparationV1MusicStemSeparationPostStemVariationId
        ] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Separate an audio file into individual stems. This endpoint might have high latency, depending on the length of the audio file.

        Parameters
        ----------
        file : core.File
            The audio file to separate into stems.

        stem_variation_id : typing.Optional[BodyStemSeparationV1MusicStemSeparationPostStemVariationId]
            The id of the stem variation to use.

        sign_with_c_2_pa : typing.Optional[bool]
            Whether to sign the generated song with C2PA. Applicable only for mp3 files.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            ZIP archive containing separated audio stems. Each stem is provided as a separate audio file in the requested output format.

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.music.separate_stems(
            output_format="mp3_22050_32",
            file="file",
            stem_variation_id="two_stems_v1",
            sign_with_c_2_pa=True,
        )
        for chunk in response:
            print(chunk)
        """

        Validator(AllowedOutputFormats).is_optional().is_nullable().validate(
            output_format, "output_format"
        )

        resolved_config = self._get_resolved_config(
            self._separate_stems_config, request_options
        )

        request_body = BodyStemSeparationV1MusicStemSeparationPost(
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "stem_variation_id": stem_variation_id,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyStemSeparationV1MusicStemSeparationPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/stem-separation",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("output_format", output_format, nullable=True)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body, "multipart/form-data")
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response


class RawMusicClient:
    """
    Raw-response client for MusicClient.

    Each method delegates to the matching :class:`MusicClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: MusicClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def video_to_music(
        self,
        *,
        videos: List[bytes],
        description: Union[str, None] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        model_id: Optional[BodyVideoToMusicV1MusicVideoToMusicPostModelId] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = MusicClient.video_to_music(
            _call_client,
            videos=videos,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "description": description,
                        "tags": tags,
                        "model_id": model_id,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def compose(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyComposeMusicV1MusicPostCompositionPlan, None
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[BodyComposeMusicV1MusicPostModelId] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        respect_sections_durations: Optional[bool] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[ComposeOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = MusicClient.compose(
            _call_client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "respect_sections_durations": respect_sections_durations,
                        "store_for_inpainting": store_for_inpainting,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def compose_detailed(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan,
            None,
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        respect_sections_durations: Optional[bool] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[ComposeDetailedOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = MusicClient.compose_detailed(
            _call_client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "respect_sections_durations": respect_sections_durations,
                        "store_for_inpainting": store_for_inpainting,
                        "with_timestamps": with_timestamps,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def compose_detailed_stream(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostCompositionPlan,
            None,
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostModelId
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        output_format: Union[ComposeDetailedStreamOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[str, None, None]]:
        _call_client = self._client._for_one_call()
        data = MusicClient.compose_detailed_stream(
            _call_client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "store_for_inpainting": store_for_inpainting,
                        "with_timestamps": with_timestamps,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def stream(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyStreamComposedMusicV1MusicStreamPostCompositionPlan, None
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[BodyStreamComposedMusicV1MusicStreamPostModelId] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio8, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = MusicClient.stream(
            _call_client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "store_for_inpainting": store_for_inpainting,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def upload(
        self,
        *,
        file: bytes,
        extract_composition_plan: Optional[
            BodyUploadMusicV1MusicUploadPostExtractCompositionPlan
        ] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MusicUploadResponse]:
        data = MusicClient.upload(
            self._client,
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extract_composition_plan": extract_composition_plan,
                        "with_timestamps": with_timestamps,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def separate_stems(
        self,
        *,
        file: bytes,
        stem_variation_id: Optional[
            BodyStemSeparationV1MusicStemSeparationPostStemVariationId
        ] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = MusicClient.separate_stems(
            _call_client,
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "stem_variation_id": stem_variation_id,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )


class AsyncMusicClient(MusicClient):
    """
    Async wrapper for MusicClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def composition_plan(self) -> "_AsyncCompositionPlanClient":
        """Lazily construct and return the async composition_plan sub-resource client."""
        if self._composition_plan is None:
            from .composition_plan.client import AsyncCompositionPlanClient

            _child = AsyncCompositionPlanClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._composition_plan = _child
        return self._composition_plan

    @property
    def finetunes(self) -> "_AsyncFinetunesClient":
        """Lazily construct and return the async finetunes sub-resource client."""
        if self._finetunes is None:
            from .finetunes.client import AsyncFinetunesClient

            _child = AsyncFinetunesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._finetunes = _child
        return self._finetunes

    @property
    def with_raw_response(self) -> "AsyncRawMusicClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawMusicClient(self)

    def video_to_music(
        self,
        *,
        videos: List[bytes],
        description: Union[str, None] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        model_id: Optional[BodyVideoToMusicV1MusicVideoToMusicPostModelId] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Generate background music from one or more video files. Videos are combined in order. Optional description and style tags influence the generated music.

        Parameters
        ----------
        videos : typing.Sequence[core.File]
            One or more video files sent via FormData array (multipart/form-data). They will be combined into one codec in order.
                        A maximum of 10 videos is allowed, where the total size of the combined video is limited to 200MB.
                        In total, the video can be up to 600 seconds long. Note that combining multiple videos may increase the request duration significantly. If possible, combine the videos beforehand.

        description : typing.Optional[str]
            Optional text description of the music you want. A maximum of 1000 characters is allowed.

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of style tags (e.g. ['upbeat', 'cinematic']). A maximum of 10 tags is allowed.

        model_id : typing.Optional[BodyVideoToMusicV1MusicVideoToMusicPostModelId]
            The model to use for the generation.

        sign_with_c_2_pa : typing.Optional[bool]
            Whether to sign the generated song with C2PA. Applicable only for mp3 files.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Generated audio file matching the video. Content-Type and file extension depend on the output_format parameter (default mp3).

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.music.video_to_music(
                output_format="mp3_22050_32",
                videos=[
                    "videos"
                ],
                description="description",
                tags=[
                    "tags"
                ],
                model_id="music_v1",
                sign_with_c_2_pa=False,
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().video_to_music(
            videos=videos,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "description": description,
                        "tags": tags,
                        "model_id": model_id,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
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

    def compose(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyComposeMusicV1MusicPostCompositionPlan, None
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[BodyComposeMusicV1MusicPostModelId] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        respect_sections_durations: Optional[bool] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[ComposeOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Compose a song from a prompt or a composition plan.

        Parameters
        ----------
        prompt : typing.Optional[str]
            A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.

        composition_plan : typing.Optional[BodyComposeMusicV1MusicPostCompositionPlan]
            A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.

        music_length_ms : typing.Optional[int]
            The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        model_id : typing.Optional[BodyComposeMusicV1MusicPostModelId]
            The model to use for the generation.

        seed : typing.Optional[int]
            Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.

        force_instrumental : typing.Optional[bool]
            If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.

        finetune_id : typing.Optional[str]
            The ID of the finetune to use for the generation

        respect_sections_durations : typing.Optional[bool]
            Controls how strictly section durations in the `composition_plan` are enforced. Only used with `composition_plan` and only applies to `music_v1`; for `music_v2` section durations are always enforced and this is ignored. When false for `music_v1`, the model may adjust individual section durations for better quality and latency, while preserving the total song duration from the plan.

        store_for_inpainting : typing.Optional[bool]
            Whether to store the generated song for inpainting.

        sign_with_c_2_pa : typing.Optional[bool]
            Whether to sign the generated song with C2PA. Applicable only for mp3 files.

        output_format : typing.Optional[ComposeOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The generated audio file in the format specified

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import ComposeOutputFormat

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.music.compose(
                output_format="auto",
                prompt="prompt",
                composition_plan={
                    "positive_global_styles": [
                        "positive_global_styles"
                    ],
                    "negative_global_styles": [
                        "negative_global_styles"
                    ],
                    "sections": [
                        {
                            "section_name": "section_name",
                            "positive_local_styles": [
                                "positive_local_styles"
                            ],
                            "negative_local_styles": [
                                "negative_local_styles"
                            ],
                            "duration_ms": 9189,
                            "lines": [
                                "lines"
                            ],
                            "source_from": {
                                "song_id": "song_id",
                                "range": {
                                    "start_ms": 9,
                                    "end_ms": 4
                                },
                                "negative_ranges": [
                                    {
                                        "start_ms": 9,
                                        "end_ms": 4
                                    }
                                ]
                            }
                        }
                    ]
                },
                music_length_ms=36319,
                model_id="music_v1",
                seed=1974260297,
                force_instrumental=False,
                finetune_id="finetune_id",
                respect_sections_durations=True,
                store_for_inpainting=True,
                sign_with_c_2_pa=True,
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().compose(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "respect_sections_durations": respect_sections_durations,
                        "store_for_inpainting": store_for_inpainting,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
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

    def compose_detailed(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan,
            None,
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        respect_sections_durations: Optional[bool] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[ComposeDetailedOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Compose a song from a prompt or a composition plan.

        Parameters
        ----------
        prompt : typing.Optional[str]
            A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.

        composition_plan : typing.Optional[BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan]
            A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.

        music_length_ms : typing.Optional[int]
            The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        model_id : typing.Optional[BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId]
            The model to use for the generation.

        seed : typing.Optional[int]
            Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.

        force_instrumental : typing.Optional[bool]
            If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.

        finetune_id : typing.Optional[str]
            The ID of the finetune to use for the generation

        respect_sections_durations : typing.Optional[bool]
            Controls how strictly section durations in the `composition_plan` are enforced. Only used with `composition_plan` and only applies to `music_v1`; for `music_v2` section durations are always enforced and this is ignored. When false for `music_v1`, the model may adjust individual section durations for better quality and latency, while preserving the total song duration from the plan.

        store_for_inpainting : typing.Optional[bool]
            Whether to store the generated song for inpainting.

        with_timestamps : typing.Optional[bool]
            Whether to return the timestamps of the words in the generated song.

        sign_with_c_2_pa : typing.Optional[bool]
            Whether to sign the generated song with C2PA. Applicable only for mp3 files.

        output_format : typing.Optional[ComposeDetailedOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Multipart/mixed response with JSON metadata and binary audio file

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import ComposeDetailedOutputFormat

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.music.compose_detailed(
                output_format="auto",
                prompt="A prompt for music generation",
                music_length_ms=10000,
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().compose_detailed(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "respect_sections_durations": respect_sections_durations,
                        "store_for_inpainting": store_for_inpainting,
                        "with_timestamps": with_timestamps,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
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

    def compose_detailed_stream(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostCompositionPlan,
            None,
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostModelId
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        output_format: Union[ComposeDetailedStreamOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[str, None]:  # type: ignore[override]
        """
        Stream a song and its detailed metadata using Server-Sent Events (SSE).

        Parameters
        ----------
        prompt : typing.Optional[str]
            A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.

        composition_plan : typing.Optional[BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostCompositionPlan]
            A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.

        music_length_ms : typing.Optional[int]
            The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        model_id : typing.Optional[BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostModelId]
            The model to use for the generation.

        seed : typing.Optional[int]
            Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.

        force_instrumental : typing.Optional[bool]
            If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.

        finetune_id : typing.Optional[str]
            The ID of the finetune to use for the generation

        store_for_inpainting : typing.Optional[bool]
            Whether to store the generated song for inpainting.

        with_timestamps : typing.Optional[bool]
            Whether to return the timestamps of the words in the generated song.

        output_format : typing.Optional[ComposeDetailedStreamOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[str]
            Server-Sent Events for composition plan, song metadata, audio chunks with optional word timestamps, and completion.

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import ComposeDetailedStreamOutputFormat

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.music.compose_detailed_stream(
                output_format="auto",
                prompt="prompt",
                composition_plan={
                    "positive_global_styles": [
                        "positive_global_styles"
                    ],
                    "negative_global_styles": [
                        "negative_global_styles"
                    ],
                    "sections": [
                        {
                            "section_name": "section_name",
                            "positive_local_styles": [
                                "positive_local_styles"
                            ],
                            "negative_local_styles": [
                                "negative_local_styles"
                            ],
                            "duration_ms": 9189,
                            "lines": [
                                "lines"
                            ],
                            "source_from": {
                                "song_id": "song_id",
                                "range": {
                                    "start_ms": 9,
                                    "end_ms": 4
                                },
                                "negative_ranges": [
                                    {
                                        "start_ms": 9,
                                        "end_ms": 4
                                    }
                                ]
                            }
                        }
                    ]
                },
                music_length_ms=189956,
                model_id="music_v1",
                seed=1073974809,
                force_instrumental=False,
                finetune_id="finetune_id",
                store_for_inpainting=False,
                with_timestamps=True,
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().compose_detailed_stream(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "store_for_inpainting": store_for_inpainting,
                        "with_timestamps": with_timestamps,
                        "output_format": output_format,
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

    def stream(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyStreamComposedMusicV1MusicStreamPostCompositionPlan, None
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[BodyStreamComposedMusicV1MusicStreamPostModelId] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio8, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Stream a composed song from a prompt or a composition plan.

        Parameters
        ----------
        prompt : typing.Optional[str]
            A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.

        composition_plan : typing.Optional[BodyStreamComposedMusicV1MusicStreamPostCompositionPlan]
            A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.

        music_length_ms : typing.Optional[int]
            The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        model_id : typing.Optional[BodyStreamComposedMusicV1MusicStreamPostModelId]
            The model to use for the generation.

        seed : typing.Optional[int]
            Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.

        force_instrumental : typing.Optional[bool]
            If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.

        finetune_id : typing.Optional[str]
            The ID of the finetune to use for the generation

        store_for_inpainting : typing.Optional[bool]
            Whether to store the generated song for inpainting.

        output_format : typing.Optional[OutputFormatOfTheGeneratedAudio8]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Streaming audio data in the format specified

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import OutputFormatOfTheGeneratedAudio8

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.music.stream(
                output_format="auto",
                prompt="prompt",
                composition_plan={
                    "positive_global_styles": [
                        "positive_global_styles"
                    ],
                    "negative_global_styles": [
                        "negative_global_styles"
                    ],
                    "sections": [
                        {
                            "section_name": "section_name",
                            "positive_local_styles": [
                                "positive_local_styles"
                            ],
                            "negative_local_styles": [
                                "negative_local_styles"
                            ],
                            "duration_ms": 9189,
                            "lines": [
                                "lines"
                            ],
                            "source_from": {
                                "song_id": "song_id",
                                "range": {
                                    "start_ms": 9,
                                    "end_ms": 4
                                },
                                "negative_ranges": [
                                    {
                                        "start_ms": 9,
                                        "end_ms": 4
                                    }
                                ]
                            }
                        }
                    ]
                },
                music_length_ms=523967,
                model_id="music_v1",
                seed=1183754256,
                force_instrumental=False,
                finetune_id="finetune_id",
                store_for_inpainting=True,
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "store_for_inpainting": store_for_inpainting,
                        "output_format": output_format,
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

    def upload(
        self,
        *,
        file: bytes,
        extract_composition_plan: Optional[
            BodyUploadMusicV1MusicUploadPostExtractCompositionPlan
        ] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[MusicUploadResponse]:  # type: ignore[override]
        """
        Upload a music file to be later used for inpainting. Price for uploading is the same as the one for song generation. All uploaded content gets inspected for copyright infringement. If copyrighted content is detected, half of the request cost is still charged.

        Parameters
        ----------
        file : core.File
            The audio file to upload.

        extract_composition_plan : typing.Optional[BodyUploadMusicV1MusicUploadPostExtractCompositionPlan]
            Whether to generate and return the composition plan for the uploaded song. Pass a model id (`music_v1` or `music_v2`) to control which composition plan format is returned. Passing `true`/`false` is deprecated; `true` defaults to the `music_v1` plan format. Enabling this will increase the latency.

        with_timestamps : typing.Optional[bool]
            Whether to transcribe the uploaded song and return word-level timestamps. If True, the response will include words_timestamps but will increase the latency.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicUploadResponse
            Successfully uploaded music file with optional composition plan

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.music.upload(
                file="file",
                extract_composition_plan=True,
                with_timestamps=False,
            )


        asyncio.run(main())
        """
        return to_async(super().upload)(
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extract_composition_plan": extract_composition_plan,
                        "with_timestamps": with_timestamps,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def separate_stems(
        self,
        *,
        file: bytes,
        stem_variation_id: Optional[
            BodyStemSeparationV1MusicStemSeparationPostStemVariationId
        ] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Separate an audio file into individual stems. This endpoint might have high latency, depending on the length of the audio file.

        Parameters
        ----------
        file : core.File
            The audio file to separate into stems.

        stem_variation_id : typing.Optional[BodyStemSeparationV1MusicStemSeparationPostStemVariationId]
            The id of the stem variation to use.

        sign_with_c_2_pa : typing.Optional[bool]
            Whether to sign the generated song with C2PA. Applicable only for mp3 files.

        output_format : typing.Optional[AllowedOutputFormats]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            ZIP archive containing separated audio stems. Each stem is provided as a separate audio file in the requested output format.

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import AllowedOutputFormats

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.music.separate_stems(
                output_format="mp3_22050_32",
                file="file",
                stem_variation_id="two_stems_v1",
                sign_with_c_2_pa=True,
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().separate_stems(
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "stem_variation_id": stem_variation_id,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
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


class AsyncRawMusicClient:
    """
    Async raw-response client for AsyncMusicClient.
    """

    def __init__(self, client: AsyncMusicClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def video_to_music(
        self,
        *,
        videos: List[bytes],
        description: Union[str, None] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        model_id: Optional[BodyVideoToMusicV1MusicVideoToMusicPostModelId] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncMusicClient.video_to_music(
            _call_client,
            videos=videos,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "description": description,
                        "tags": tags,
                        "model_id": model_id,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def compose(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyComposeMusicV1MusicPostCompositionPlan, None
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[BodyComposeMusicV1MusicPostModelId] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        respect_sections_durations: Optional[bool] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[ComposeOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncMusicClient.compose(
            _call_client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "respect_sections_durations": respect_sections_durations,
                        "store_for_inpainting": store_for_inpainting,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def compose_detailed(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan,
            None,
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[
            BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        respect_sections_durations: Optional[bool] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[ComposeDetailedOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncMusicClient.compose_detailed(
            _call_client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "respect_sections_durations": respect_sections_durations,
                        "store_for_inpainting": store_for_inpainting,
                        "with_timestamps": with_timestamps,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def compose_detailed_stream(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostCompositionPlan,
            None,
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[
            BodyStreamComposedMusicWithADetailedResponseV1MusicDetailedStreamPostModelId
        ] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        output_format: Union[ComposeDetailedStreamOutputFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[str, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncMusicClient.compose_detailed_stream(
            _call_client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "store_for_inpainting": store_for_inpainting,
                        "with_timestamps": with_timestamps,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def stream(
        self,
        *,
        prompt: Union[str, None] = SENTINEL,
        composition_plan: Union[
            BodyStreamComposedMusicV1MusicStreamPostCompositionPlan, None
        ] = SENTINEL,
        music_length_ms: Union[int, None] = SENTINEL,
        model_id: Optional[BodyStreamComposedMusicV1MusicStreamPostModelId] = SENTINEL,
        seed: Union[int, None] = SENTINEL,
        force_instrumental: Optional[bool] = SENTINEL,
        finetune_id: Union[str, None] = SENTINEL,
        store_for_inpainting: Optional[bool] = SENTINEL,
        output_format: Union[OutputFormatOfTheGeneratedAudio8, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncMusicClient.stream(
            _call_client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt": prompt,
                        "composition_plan": composition_plan,
                        "music_length_ms": music_length_ms,
                        "model_id": model_id,
                        "seed": seed,
                        "force_instrumental": force_instrumental,
                        "finetune_id": finetune_id,
                        "store_for_inpainting": store_for_inpainting,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    async def upload(
        self,
        *,
        file: bytes,
        extract_composition_plan: Optional[
            BodyUploadMusicV1MusicUploadPostExtractCompositionPlan
        ] = SENTINEL,
        with_timestamps: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MusicUploadResponse]:
        data = await AsyncMusicClient.upload(
            self._client,
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extract_composition_plan": extract_composition_plan,
                        "with_timestamps": with_timestamps,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def separate_stems(
        self,
        *,
        file: bytes,
        stem_variation_id: Optional[
            BodyStemSeparationV1MusicStemSeparationPostStemVariationId
        ] = SENTINEL,
        sign_with_c_2_pa: Optional[bool] = SENTINEL,
        output_format: Union[AllowedOutputFormats, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncMusicClient.separate_stems(
            _call_client,
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "stem_variation_id": stem_variation_id,
                        "sign_with_c_2_pa": sign_with_c_2_pa,
                        "output_format": output_format,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )
