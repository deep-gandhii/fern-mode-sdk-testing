from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyDubsAllOrSomeSegmentsAndLanguagesV1DubbingResourceDubbingIdDubPost,
    BodyMoveSegmentsBetweenSpeakersV1DubbingResourceDubbingIdMigrateSegmentsPost,
    BodyRenderAudioOrVideoForTheGivenLanguageV1DubbingResourceDubbingIdRenderLanguagePost,
    BodyTranscribesSegmentsV1DubbingResourceDubbingIdTranscribePost,
    BodyTranslatesAllOrSomeSegmentsAndLanguagesV1DubbingResourceDubbingIdTranslatePost,
    DubbingRenderResponseModel,
    DubbingResource,
    HttpValidationError,
    RenderType,
    SegmentDubResponse,
    SegmentMigrationResponse,
    SegmentTranscriptionResponse,
    SegmentTranslationResponse,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .language.client import (
        LanguageClient as _LanguageClient,
        AsyncLanguageClient as _AsyncLanguageClient,
    )
    from .speaker.client import (
        SpeakerClient as _SpeakerClient,
        AsyncSpeakerClient as _AsyncSpeakerClient,
    )
    from .segment.client import (
        SegmentClient as _SegmentClient,
        AsyncSegmentClient as _AsyncSegmentClient,
    )


class ResourceClient(BaseService):
    """
    Fern-style resource client for ResourceClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._language: Any = None
        self._speaker: Any = None
        self._segment: Any = None
        self._get_config: SdkConfig = {}
        self._migrate_segments_config: SdkConfig = {}
        self._transcribe_config: SdkConfig = {}
        self._translate_config: SdkConfig = {}
        self._dub_config: SdkConfig = {}
        self._render_config: SdkConfig = {}

    @property
    def language(self) -> "_LanguageClient":
        """Lazily construct and return the language sub-resource client."""
        if self._language is None:
            from .language.client import LanguageClient

            _child = LanguageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._language = _child
        return self._language

    @property
    def speaker(self) -> "_SpeakerClient":
        """Lazily construct and return the speaker sub-resource client."""
        if self._speaker is None:
            from .speaker.client import SpeakerClient

            _child = SpeakerClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speaker = _child
        return self._speaker

    @property
    def segment(self) -> "_SegmentClient":
        """Lazily construct and return the segment sub-resource client."""
        if self._segment is None:
            from .segment.client import SegmentClient

            _child = SegmentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._segment = _child
        return self._segment

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
        if self._language is not None:
            self._language.set_base_url(base_url)
        if self._speaker is not None:
            self._speaker.set_base_url(base_url)
        if self._segment is not None:
            self._segment.set_base_url(base_url)

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
        if self._language is not None:
            self._language.set_config(config)
        if self._speaker is not None:
            self._speaker.set_config(config)
        if self._segment is not None:
            self._segment.set_config(config)

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
        if self._language is not None:
            self._language.set_timeout(timeout)
        if self._speaker is not None:
            self._speaker.set_timeout(timeout)
        if self._segment is not None:
            self._segment.set_timeout(timeout)

        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_migrate_segments_config(self, config: SdkConfig):
        """
        Sets method-level configuration for migrate_segments.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._migrate_segments_config = config
        return self

    def set_transcribe_config(self, config: SdkConfig):
        """
        Sets method-level configuration for transcribe.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._transcribe_config = config
        return self

    def set_translate_config(self, config: SdkConfig):
        """
        Sets method-level configuration for translate.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._translate_config = config
        return self

    def set_dub_config(self, config: SdkConfig):
        """
        Sets method-level configuration for dub.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._dub_config = config
        return self

    def set_render_config(self, config: SdkConfig):
        """
        Sets method-level configuration for render.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._render_config = config
        return self

    @property
    def with_raw_response(self) -> "RawResourceClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawResourceClient(self)

    @cast_models
    def get(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DubbingResource:
        """
        Given a dubbing ID generated from the '/v1/dubbing' endpoint with studio enabled, returns the dubbing resource.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingResource
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.get(
            dubbing_id="dubbing_id",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingResource.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingResource, response)
            )
        )

    @cast_models
    def migrate_segments(
        self,
        dubbing_id: str,
        *,
        segment_ids: List[str],
        speaker_id: str,
        request_options: Optional[RequestOptions] = None,
    ) -> SegmentMigrationResponse:
        """
        Change the attribution of one or more segments to a different speaker.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segment_ids : typing.Sequence[str]

        speaker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentMigrationResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.migrate_segments(
            dubbing_id="dubbing_id",
            segment_ids=[
                "segment_ids"
            ],
            speaker_id="speaker_id",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(
            self._migrate_segments_config, request_options
        )

        request_body = BodyMoveSegmentsBetweenSpeakersV1DubbingResourceDubbingIdMigrateSegmentsPost(
            segment_ids=segment_ids, speaker_id=speaker_id
        )
        Validator(
            BodyMoveSegmentsBetweenSpeakersV1DubbingResourceDubbingIdMigrateSegmentsPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/migrate-segments",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SegmentMigrationResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SegmentMigrationResponse, response)
            )
        )

    @cast_models
    def transcribe(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> SegmentTranscriptionResponse:
        """
        Regenerate the transcriptions for the specified segments. Does not automatically regenerate translations or dubs.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segments : typing.Sequence[str]
            Transcribe this specific list of segments.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentTranscriptionResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.transcribe(
            dubbing_id="dubbing_id",
            segments=[
                "segments"
            ],
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(
            self._transcribe_config, request_options
        )

        request_body = BodyTranscribesSegmentsV1DubbingResourceDubbingIdTranscribePost(
            segments=segments
        )
        Validator(
            BodyTranscribesSegmentsV1DubbingResourceDubbingIdTranscribePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/transcribe",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SegmentTranscriptionResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SegmentTranscriptionResponse, response)
            )
        )

    @cast_models
    def translate(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> SegmentTranslationResponse:
        """
        Regenerate the translations for either the entire resource or the specified segments/languages. Will automatically transcribe missing transcriptions. Will not automatically regenerate the dubs.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segments : typing.Sequence[str]
            Translate only this list of segments.

        languages : typing.Optional[typing.Sequence[str]]
            Translate only these languages for each segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentTranslationResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.translate(
            dubbing_id="dubbing_id",
            segments=[
                "segments"
            ],
            languages=[
                "languages"
            ],
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(
            self._translate_config, request_options
        )

        request_body = BodyTranslatesAllOrSomeSegmentsAndLanguagesV1DubbingResourceDubbingIdTranslatePost(
            segments=segments,
            **dict[str, Any](
                {k: v for k, v in {"languages": languages}.items() if v is not SENTINEL}
            ),
        )
        Validator(
            BodyTranslatesAllOrSomeSegmentsAndLanguagesV1DubbingResourceDubbingIdTranslatePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/translate",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SegmentTranslationResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SegmentTranslationResponse, response)
            )
        )

    @cast_models
    def dub(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> SegmentDubResponse:
        """
        Regenerate the dubs for either the entire resource or the specified segments/languages. Will automatically transcribe and translate any missing transcriptions and translations.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segments : typing.Sequence[str]
            Dub only this list of segments.

        languages : typing.Optional[typing.Sequence[str]]
            Dub only these languages for each segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentDubResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.dub(
            dubbing_id="dubbing_id",
            segments=[
                "segments"
            ],
            languages=[
                "languages"
            ],
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(self._dub_config, request_options)

        request_body = (
            BodyDubsAllOrSomeSegmentsAndLanguagesV1DubbingResourceDubbingIdDubPost(
                segments=segments,
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {"languages": languages}.items()
                        if v is not SENTINEL
                    }
                ),
            )
        )
        Validator(
            BodyDubsAllOrSomeSegmentsAndLanguagesV1DubbingResourceDubbingIdDubPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/dub",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SegmentDubResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SegmentDubResponse, response)
            )
        )

    @cast_models
    def render(
        self,
        dubbing_id: str,
        language: str,
        *,
        render_type: RenderType,
        normalize_volume: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingRenderResponseModel:
        """
        Regenerate the output media for a language using the latest Studio state. Please ensure all segments have been dubbed before rendering, otherwise they will be omitted. Renders are generated asynchronously, and to check the status of all renders please use the 'Get Dubbing Resource' endpoint.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language : str
            The target language code to render, eg. 'es'. To render the source track use 'original'.

        render_type : RenderType

        normalize_volume : typing.Optional[bool]
            Whether to normalize the volume of the rendered audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingRenderResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.render(
            dubbing_id="dubbing_id",
            language="language",
            render_type="mp4",
            normalize_volume=False,
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")
        Validator(str).validate(language, "language")

        resolved_config = self._get_resolved_config(
            self._render_config, request_options
        )

        request_body = BodyRenderAudioOrVideoForTheGivenLanguageV1DubbingResourceDubbingIdRenderLanguagePost(
            render_type=render_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"normalize_volume": normalize_volume}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(
            BodyRenderAudioOrVideoForTheGivenLanguageV1DubbingResourceDubbingIdRenderLanguagePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/render/{{language}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .add_path("language", language)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingRenderResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingRenderResponseModel, response)
            )
        )


class RawResourceClient:
    """
    Raw-response client for ResourceClient.

    Each method delegates to the matching :class:`ResourceClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ResourceClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DubbingResource]:
        data = ResourceClient.get(
            self._client, dubbing_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def migrate_segments(
        self,
        dubbing_id: str,
        *,
        segment_ids: List[str],
        speaker_id: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentMigrationResponse]:
        data = ResourceClient.migrate_segments(
            self._client,
            dubbing_id,
            segment_ids=segment_ids,
            speaker_id=speaker_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def transcribe(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentTranscriptionResponse]:
        data = ResourceClient.transcribe(
            self._client, dubbing_id, segments=segments, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def translate(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentTranslationResponse]:
        data = ResourceClient.translate(
            self._client,
            dubbing_id,
            segments=segments,
            **dict[str, Any](
                {k: v for k, v in {"languages": languages}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def dub(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentDubResponse]:
        data = ResourceClient.dub(
            self._client,
            dubbing_id,
            segments=segments,
            **dict[str, Any](
                {k: v for k, v in {"languages": languages}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def render(
        self,
        dubbing_id: str,
        language: str,
        *,
        render_type: RenderType,
        normalize_volume: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingRenderResponseModel]:
        data = ResourceClient.render(
            self._client,
            dubbing_id,
            language,
            render_type=render_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"normalize_volume": normalize_volume}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncResourceClient(ResourceClient):
    """
    Async wrapper for ResourceClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def language(self) -> "_AsyncLanguageClient":
        """Lazily construct and return the async language sub-resource client."""
        if self._language is None:
            from .language.client import AsyncLanguageClient

            _child = AsyncLanguageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._language = _child
        return self._language

    @property
    def speaker(self) -> "_AsyncSpeakerClient":
        """Lazily construct and return the async speaker sub-resource client."""
        if self._speaker is None:
            from .speaker.client import AsyncSpeakerClient

            _child = AsyncSpeakerClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speaker = _child
        return self._speaker

    @property
    def segment(self) -> "_AsyncSegmentClient":
        """Lazily construct and return the async segment sub-resource client."""
        if self._segment is None:
            from .segment.client import AsyncSegmentClient

            _child = AsyncSegmentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._segment = _child
        return self._segment

    @property
    def with_raw_response(self) -> "AsyncRawResourceClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawResourceClient(self)

    def get(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DubbingResource]:  # type: ignore[override]
        """
        Given a dubbing ID generated from the '/v1/dubbing' endpoint with studio enabled, returns the dubbing resource.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingResource
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.get(
                dubbing_id="dubbing_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(dubbing_id, request_options=request_options)

    def migrate_segments(
        self,
        dubbing_id: str,
        *,
        segment_ids: List[str],
        speaker_id: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SegmentMigrationResponse]:  # type: ignore[override]
        """
        Change the attribution of one or more segments to a different speaker.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segment_ids : typing.Sequence[str]

        speaker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentMigrationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.migrate_segments(
                dubbing_id="dubbing_id",
                segment_ids=[
                    "segment_ids"
                ],
                speaker_id="speaker_id",
            )


        asyncio.run(main())
        """
        return to_async(super().migrate_segments)(
            dubbing_id,
            segment_ids=segment_ids,
            speaker_id=speaker_id,
            request_options=request_options,
        )

    def transcribe(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SegmentTranscriptionResponse]:  # type: ignore[override]
        """
        Regenerate the transcriptions for the specified segments. Does not automatically regenerate translations or dubs.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segments : typing.Sequence[str]
            Transcribe this specific list of segments.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentTranscriptionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.transcribe(
                dubbing_id="dubbing_id",
                segments=[
                    "segments"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().transcribe)(
            dubbing_id, segments=segments, request_options=request_options
        )

    def translate(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SegmentTranslationResponse]:  # type: ignore[override]
        """
        Regenerate the translations for either the entire resource or the specified segments/languages. Will automatically transcribe missing transcriptions. Will not automatically regenerate the dubs.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segments : typing.Sequence[str]
            Translate only this list of segments.

        languages : typing.Optional[typing.Sequence[str]]
            Translate only these languages for each segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentTranslationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.translate(
                dubbing_id="dubbing_id",
                segments=[
                    "segments"
                ],
                languages=[
                    "languages"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().translate)(
            dubbing_id,
            segments=segments,
            **dict[str, Any](
                {k: v for k, v in {"languages": languages}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def dub(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SegmentDubResponse]:  # type: ignore[override]
        """
        Regenerate the dubs for either the entire resource or the specified segments/languages. Will automatically transcribe and translate any missing transcriptions and translations.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        segments : typing.Sequence[str]
            Dub only this list of segments.

        languages : typing.Optional[typing.Sequence[str]]
            Dub only these languages for each segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentDubResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.dub(
                dubbing_id="dubbing_id",
                segments=[
                    "segments"
                ],
                languages=[
                    "languages"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().dub)(
            dubbing_id,
            segments=segments,
            **dict[str, Any](
                {k: v for k, v in {"languages": languages}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def render(
        self,
        dubbing_id: str,
        language: str,
        *,
        render_type: RenderType,
        normalize_volume: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingRenderResponseModel]:  # type: ignore[override]
        """
        Regenerate the output media for a language using the latest Studio state. Please ensure all segments have been dubbed before rendering, otherwise they will be omitted. Renders are generated asynchronously, and to check the status of all renders please use the 'Get Dubbing Resource' endpoint.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language : str
            The target language code to render, eg. 'es'. To render the source track use 'original'.

        render_type : RenderType

        normalize_volume : typing.Optional[bool]
            Whether to normalize the volume of the rendered audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingRenderResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.render(
                dubbing_id="dubbing_id",
                language="language",
                render_type="mp4",
                normalize_volume=False,
            )


        asyncio.run(main())
        """
        return to_async(super().render)(
            dubbing_id,
            language,
            render_type=render_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"normalize_volume": normalize_volume}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawResourceClient:
    """
    Async raw-response client for AsyncResourceClient.
    """

    def __init__(self, client: AsyncResourceClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DubbingResource]:
        data = await AsyncResourceClient.get(
            self._client, dubbing_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def migrate_segments(
        self,
        dubbing_id: str,
        *,
        segment_ids: List[str],
        speaker_id: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentMigrationResponse]:
        data = await AsyncResourceClient.migrate_segments(
            self._client,
            dubbing_id,
            segment_ids=segment_ids,
            speaker_id=speaker_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def transcribe(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentTranscriptionResponse]:
        data = await AsyncResourceClient.transcribe(
            self._client, dubbing_id, segments=segments, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def translate(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentTranslationResponse]:
        data = await AsyncResourceClient.translate(
            self._client,
            dubbing_id,
            segments=segments,
            **dict[str, Any](
                {k: v for k, v in {"languages": languages}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def dub(
        self,
        dubbing_id: str,
        *,
        segments: List[str],
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SegmentDubResponse]:
        data = await AsyncResourceClient.dub(
            self._client,
            dubbing_id,
            segments=segments,
            **dict[str, Any](
                {k: v for k, v in {"languages": languages}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def render(
        self,
        dubbing_id: str,
        language: str,
        *,
        render_type: RenderType,
        normalize_volume: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingRenderResponseModel]:
        data = await AsyncResourceClient.render(
            self._client,
            dubbing_id,
            language,
            render_type=render_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"normalize_volume": normalize_volume}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
