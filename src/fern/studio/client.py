from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    BodyCreatePodcastV1StudioPodcastsPost,
    BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization,
    BodyCreatePodcastV1StudioPodcastsPostDurationScale,
    BodyCreatePodcastV1StudioPodcastsPostMode,
    BodyCreatePodcastV1StudioPodcastsPostSource,
    HttpValidationError,
    PodcastProjectResponseModel,
    QualityPresetType,
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
    from .projects.client import (
        ProjectsClient as _ProjectsClient,
        AsyncProjectsClient as _AsyncProjectsClient,
    )


class StudioClient(BaseService):
    """
    Fern-style resource client for StudioClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._projects: Any = None
        self._create_podcast_config: SdkConfig = {}

    @property
    def projects(self) -> "_ProjectsClient":
        """Lazily construct and return the projects sub-resource client."""
        if self._projects is None:
            from .projects.client import ProjectsClient

            _child = ProjectsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._projects = _child
        return self._projects

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
        if self._projects is not None:
            self._projects.set_base_url(base_url)

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
        if self._projects is not None:
            self._projects.set_config(config)

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
        if self._projects is not None:
            self._projects.set_timeout(timeout)

        return self

    def set_create_podcast_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_podcast.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_podcast_config = config
        return self

    @property
    def with_raw_response(self) -> "RawStudioClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawStudioClient(self)

    @cast_models
    def create_podcast(
        self,
        *,
        model_id: str,
        mode: BodyCreatePodcastV1StudioPodcastsPostMode,
        source: BodyCreatePodcastV1StudioPodcastsPostSource,
        quality_preset: Optional[QualityPresetType] = SENTINEL,
        duration_scale: Optional[
            BodyCreatePodcastV1StudioPodcastsPostDurationScale
        ] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        intro: Union[str, None] = SENTINEL,
        outro: Union[str, None] = SENTINEL,
        instructions_prompt: Union[str, None] = SENTINEL,
        highlights: Union[List[str], None] = SENTINEL,
        callback_url: Union[str, None] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization, None
        ] = SENTINEL,
        safety_identifier: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> PodcastProjectResponseModel:
        """
        Create and auto-convert a podcast project. Currently, the LLM cost is covered by us but you will still be charged for the audio generation. In the future, you will be charged for both the LLM and audio generation costs.

        Parameters
        ----------
        model_id : str
            The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models.

        mode : BodyCreatePodcastV1StudioPodcastsPostMode
            The type of podcast to generate. Can be 'conversation', an interaction between two voices, or 'bulletin', a monologue.

        source : BodyCreatePodcastV1StudioPodcastsPostSource
            The source content for the Podcast.

        quality_preset : typing.Optional[QualityPresetType]

        duration_scale : typing.Optional[BodyCreatePodcastV1StudioPodcastsPostDurationScale]
            Duration of the generated podcast. Must be one of:
            short - produces podcasts shorter than 3 minutes.
            default - produces podcasts roughly between 3-7 minutes.
            long - produces podcasts longer than 7 minutes.

        language : typing.Optional[str]
            An optional language of the Studio project. Two-letter language code (ISO 639-1).

        intro : typing.Optional[str]
            The intro text that will always be added to the beginning of the podcast.

        outro : typing.Optional[str]
            The outro text that will always be added to the end of the podcast.

        instructions_prompt : typing.Optional[str]
            Additional instructions prompt for the podcast generation used to adjust the podcast's style and tone.

        highlights : typing.Optional[typing.Sequence[str]]
            A brief summary or highlights of the Studio project's content, providing key points or themes. This should be between 10 and 70 characters.

        callback_url : typing.Optional[str]
            A url that will be called by our service when the Studio project is converted. Request will contain a json blob containing the status of the conversion
                Messages:
                1. When project was converted successfully:
                {
                  type: "project_conversion_status",
                  event_timestamp: 1234567890,
                  data: {
                    request_id: "1234567890",
                    project_id: "21m00Tcm4TlvDq8ikWAM",
                    conversion_status: "success",
                    project_snapshot_id: "22m00Tcm4TlvDq8ikMAT",
                    error_details: None,
                  }
                }
                2. When project conversion failed:
                {
                  type: "project_conversion_status",
                  event_timestamp: 1234567890,
                  data: {
                    request_id: "1234567890",
                    project_id: "21m00Tcm4TlvDq8ikWAM",
                    conversion_status: "error",
                    project_snapshot_id: None,
                    error_details: "Error details if conversion failed"
                  }
                }

                3. When chapter was converted successfully:
                {
                  type: "chapter_conversion_status",
                  event_timestamp: 1234567890,
                  data: {
                    request_id: "1234567890",
                    project_id: "21m00Tcm4TlvDq8ikWAM",
                    chapter_id: "22m00Tcm4TlvDq8ikMAT",
                    conversion_status: "success",
                    chapter_snapshot_id: "23m00Tcm4TlvDq8ikMAV",
                    error_details: None,
                  }
                }
                4. When chapter conversion failed:
                {
                  type: "chapter_conversion_status",
                  event_timestamp: 1234567890,
                  data: {
                    request_id: "1234567890",
                    project_id: "21m00Tcm4TlvDq8ikWAM",
                    chapter_id: "22m00Tcm4TlvDq8ikMAT",
                    conversion_status: "error",
                    chapter_snapshot_id: None,
                    error_details: "Error details if conversion failed"
                  }
                }

        apply_text_normalization : typing.Optional[BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization]
            This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
                When set to 'auto', the system will automatically decide whether to apply text normalization
                (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
                with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.

        safety_identifier : typing.Optional[str]
            Used for moderation. Your workspace must be allowlisted to use this feature.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastProjectResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.create_podcast(
            safety_identifier="safety-identifier",
            model_id="eleven_multilingual_v2",
            mode={
                "type": "conversation",
                "conversation": {
                    "host_voice_id": "host_voice_id",
                    "guest_voice_id": "guest_voice_id"
                }
            },
            source={
                "type": "text",
                "text": "text"
            },
            quality_preset="standard",
            duration_scale="short",
            language="ip",
            intro="intro",
            outro="outro",
            instructions_prompt="instructions_prompt",
            highlights=[
                "highlights"
            ],
            callback_url="callback_url",
            apply_text_normalization="auto",
        )
        """

        Validator(str).is_optional().is_nullable().validate(
            safety_identifier, "safety_identifier"
        )

        resolved_config = self._get_resolved_config(
            self._create_podcast_config, request_options
        )

        request_body = BodyCreatePodcastV1StudioPodcastsPost(
            model_id=model_id,
            mode=mode,
            source=source,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "quality_preset": quality_preset,
                        "duration_scale": duration_scale,
                        "language": language,
                        "intro": intro,
                        "outro": outro,
                        "instructions_prompt": instructions_prompt,
                        "highlights": highlights,
                        "callback_url": callback_url,
                        "apply_text_normalization": apply_text_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreatePodcastV1StudioPodcastsPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/podcasts",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_header("safety-identifier", safety_identifier)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                PodcastProjectResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(PodcastProjectResponseModel, response)
            )
        )


class RawStudioClient:
    """
    Raw-response client for StudioClient.

    Each method delegates to the matching :class:`StudioClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: StudioClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create_podcast(
        self,
        *,
        model_id: str,
        mode: BodyCreatePodcastV1StudioPodcastsPostMode,
        source: BodyCreatePodcastV1StudioPodcastsPostSource,
        quality_preset: Optional[QualityPresetType] = SENTINEL,
        duration_scale: Optional[
            BodyCreatePodcastV1StudioPodcastsPostDurationScale
        ] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        intro: Union[str, None] = SENTINEL,
        outro: Union[str, None] = SENTINEL,
        instructions_prompt: Union[str, None] = SENTINEL,
        highlights: Union[List[str], None] = SENTINEL,
        callback_url: Union[str, None] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization, None
        ] = SENTINEL,
        safety_identifier: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PodcastProjectResponseModel]:
        data = StudioClient.create_podcast(
            self._client,
            model_id=model_id,
            mode=mode,
            source=source,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "quality_preset": quality_preset,
                        "duration_scale": duration_scale,
                        "language": language,
                        "intro": intro,
                        "outro": outro,
                        "instructions_prompt": instructions_prompt,
                        "highlights": highlights,
                        "callback_url": callback_url,
                        "apply_text_normalization": apply_text_normalization,
                        "safety_identifier": safety_identifier,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncStudioClient(StudioClient):
    """
    Async wrapper for StudioClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def projects(self) -> "_AsyncProjectsClient":
        """Lazily construct and return the async projects sub-resource client."""
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            _child = AsyncProjectsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._projects = _child
        return self._projects

    @property
    def with_raw_response(self) -> "AsyncRawStudioClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawStudioClient(self)

    def create_podcast(
        self,
        *,
        model_id: str,
        mode: BodyCreatePodcastV1StudioPodcastsPostMode,
        source: BodyCreatePodcastV1StudioPodcastsPostSource,
        quality_preset: Optional[QualityPresetType] = SENTINEL,
        duration_scale: Optional[
            BodyCreatePodcastV1StudioPodcastsPostDurationScale
        ] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        intro: Union[str, None] = SENTINEL,
        outro: Union[str, None] = SENTINEL,
        instructions_prompt: Union[str, None] = SENTINEL,
        highlights: Union[List[str], None] = SENTINEL,
        callback_url: Union[str, None] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization, None
        ] = SENTINEL,
        safety_identifier: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PodcastProjectResponseModel]:  # type: ignore[override]
        """
        Create and auto-convert a podcast project. Currently, the LLM cost is covered by us but you will still be charged for the audio generation. In the future, you will be charged for both the LLM and audio generation costs.

        Parameters
        ----------
        model_id : str
            The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models.

        mode : BodyCreatePodcastV1StudioPodcastsPostMode
            The type of podcast to generate. Can be 'conversation', an interaction between two voices, or 'bulletin', a monologue.

        source : BodyCreatePodcastV1StudioPodcastsPostSource
            The source content for the Podcast.

        quality_preset : typing.Optional[QualityPresetType]

        duration_scale : typing.Optional[BodyCreatePodcastV1StudioPodcastsPostDurationScale]
            Duration of the generated podcast. Must be one of:
            short - produces podcasts shorter than 3 minutes.
            default - produces podcasts roughly between 3-7 minutes.
            long - produces podcasts longer than 7 minutes.

        language : typing.Optional[str]
            An optional language of the Studio project. Two-letter language code (ISO 639-1).

        intro : typing.Optional[str]
            The intro text that will always be added to the beginning of the podcast.

        outro : typing.Optional[str]
            The outro text that will always be added to the end of the podcast.

        instructions_prompt : typing.Optional[str]
            Additional instructions prompt for the podcast generation used to adjust the podcast's style and tone.

        highlights : typing.Optional[typing.Sequence[str]]
            A brief summary or highlights of the Studio project's content, providing key points or themes. This should be between 10 and 70 characters.

        callback_url : typing.Optional[str]
            A url that will be called by our service when the Studio project is converted. Request will contain a json blob containing the status of the conversion
                Messages:
                1. When project was converted successfully:
                {
                  type: "project_conversion_status",
                  event_timestamp: 1234567890,
                  data: {
                    request_id: "1234567890",
                    project_id: "21m00Tcm4TlvDq8ikWAM",
                    conversion_status: "success",
                    project_snapshot_id: "22m00Tcm4TlvDq8ikMAT",
                    error_details: None,
                  }
                }
                2. When project conversion failed:
                {
                  type: "project_conversion_status",
                  event_timestamp: 1234567890,
                  data: {
                    request_id: "1234567890",
                    project_id: "21m00Tcm4TlvDq8ikWAM",
                    conversion_status: "error",
                    project_snapshot_id: None,
                    error_details: "Error details if conversion failed"
                  }
                }

                3. When chapter was converted successfully:
                {
                  type: "chapter_conversion_status",
                  event_timestamp: 1234567890,
                  data: {
                    request_id: "1234567890",
                    project_id: "21m00Tcm4TlvDq8ikWAM",
                    chapter_id: "22m00Tcm4TlvDq8ikMAT",
                    conversion_status: "success",
                    chapter_snapshot_id: "23m00Tcm4TlvDq8ikMAV",
                    error_details: None,
                  }
                }
                4. When chapter conversion failed:
                {
                  type: "chapter_conversion_status",
                  event_timestamp: 1234567890,
                  data: {
                    request_id: "1234567890",
                    project_id: "21m00Tcm4TlvDq8ikWAM",
                    chapter_id: "22m00Tcm4TlvDq8ikMAT",
                    conversion_status: "error",
                    chapter_snapshot_id: None,
                    error_details: "Error details if conversion failed"
                  }
                }

        apply_text_normalization : typing.Optional[BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization]
            This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
                When set to 'auto', the system will automatically decide whether to apply text normalization
                (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
                with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.

        safety_identifier : typing.Optional[str]
            Used for moderation. Your workspace must be allowlisted to use this feature.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastProjectResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.create_podcast(
                safety_identifier="safety-identifier",
                model_id="eleven_multilingual_v2",
                mode={
                    "type": "conversation",
                    "conversation": {
                        "host_voice_id": "host_voice_id",
                        "guest_voice_id": "guest_voice_id"
                    }
                },
                source={
                    "type": "text",
                    "text": "text"
                },
                quality_preset="standard",
                duration_scale="short",
                language="ip",
                intro="intro",
                outro="outro",
                instructions_prompt="instructions_prompt",
                highlights=[
                    "highlights"
                ],
                callback_url="callback_url",
                apply_text_normalization="auto",
            )


        asyncio.run(main())
        """
        return to_async(super().create_podcast)(
            model_id=model_id,
            mode=mode,
            source=source,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "quality_preset": quality_preset,
                        "duration_scale": duration_scale,
                        "language": language,
                        "intro": intro,
                        "outro": outro,
                        "instructions_prompt": instructions_prompt,
                        "highlights": highlights,
                        "callback_url": callback_url,
                        "apply_text_normalization": apply_text_normalization,
                        "safety_identifier": safety_identifier,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawStudioClient:
    """
    Async raw-response client for AsyncStudioClient.
    """

    def __init__(self, client: AsyncStudioClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create_podcast(
        self,
        *,
        model_id: str,
        mode: BodyCreatePodcastV1StudioPodcastsPostMode,
        source: BodyCreatePodcastV1StudioPodcastsPostSource,
        quality_preset: Optional[QualityPresetType] = SENTINEL,
        duration_scale: Optional[
            BodyCreatePodcastV1StudioPodcastsPostDurationScale
        ] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        intro: Union[str, None] = SENTINEL,
        outro: Union[str, None] = SENTINEL,
        instructions_prompt: Union[str, None] = SENTINEL,
        highlights: Union[List[str], None] = SENTINEL,
        callback_url: Union[str, None] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization, None
        ] = SENTINEL,
        safety_identifier: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PodcastProjectResponseModel]:
        data = await AsyncStudioClient.create_podcast(
            self._client,
            model_id=model_id,
            mode=mode,
            source=source,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "quality_preset": quality_preset,
                        "duration_scale": duration_scale,
                        "language": language,
                        "intro": intro,
                        "outro": outro,
                        "instructions_prompt": instructions_prompt,
                        "highlights": highlights,
                        "callback_url": callback_url,
                        "apply_text_normalization": apply_text_normalization,
                        "safety_identifier": safety_identifier,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
