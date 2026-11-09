from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    CreationSources,
    DeleteDubbingResponseModel,
    DoDubbingResponse,
    DubbingMetadataPageResponseModel,
    DubbingMetadataResponse,
    DubbingModels,
    DubbingStatuses,
    DubRequest,
    DubRequestMode,
    HttpValidationError,
    ListDubbingStatus,
    ListFilterByCreator,
    ListOrderBy,
    ListOrderDirection,
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
    from .audio.client import (
        AudioClient as _AudioClient,
        AsyncAudioClient as _AsyncAudioClient,
    )
    from .project.client import (
        ProjectClient as _ProjectClient,
        AsyncProjectClient as _AsyncProjectClient,
    )
    from .resource.client import (
        ResourceClient as _ResourceClient,
        AsyncResourceClient as _AsyncResourceClient,
    )
    from .transcript.client import (
        TranscriptClient as _TranscriptClient,
        AsyncTranscriptClient as _AsyncTranscriptClient,
    )
    from .transcripts.client import (
        TranscriptsClient as _TranscriptsClient,
        AsyncTranscriptsClient as _AsyncTranscriptsClient,
    )


class DubbingClient(BaseService):
    """
    Fern-style resource client for DubbingClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._audio: Any = None
        self._project: Any = None
        self._resource: Any = None
        self._transcript: Any = None
        self._transcripts: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
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
    def project(self) -> "_ProjectClient":
        """Lazily construct and return the project sub-resource client."""
        if self._project is None:
            from .project.client import ProjectClient

            _child = ProjectClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._project = _child
        return self._project

    @property
    def resource(self) -> "_ResourceClient":
        """Lazily construct and return the resource sub-resource client."""
        if self._resource is None:
            from .resource.client import ResourceClient

            _child = ResourceClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._resource = _child
        return self._resource

    @property
    def transcript(self) -> "_TranscriptClient":
        """Lazily construct and return the transcript sub-resource client."""
        if self._transcript is None:
            from .transcript.client import TranscriptClient

            _child = TranscriptClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._transcript = _child
        return self._transcript

    @property
    def transcripts(self) -> "_TranscriptsClient":
        """Lazily construct and return the transcripts sub-resource client."""
        if self._transcripts is None:
            from .transcripts.client import TranscriptsClient

            _child = TranscriptsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._transcripts = _child
        return self._transcripts

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
        if self._project is not None:
            self._project.set_base_url(base_url)
        if self._resource is not None:
            self._resource.set_base_url(base_url)
        if self._transcript is not None:
            self._transcript.set_base_url(base_url)
        if self._transcripts is not None:
            self._transcripts.set_base_url(base_url)

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
        if self._project is not None:
            self._project.set_config(config)
        if self._resource is not None:
            self._resource.set_config(config)
        if self._transcript is not None:
            self._transcript.set_config(config)
        if self._transcripts is not None:
            self._transcripts.set_config(config)

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
        if self._project is not None:
            self._project.set_timeout(timeout)
        if self._resource is not None:
            self._resource.set_timeout(timeout)
        if self._transcript is not None:
            self._transcript.set_timeout(timeout)
        if self._transcripts is not None:
            self._transcripts.set_timeout(timeout)

        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
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

    @property
    def with_raw_response(self) -> "RawDubbingClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawDubbingClient(self)

    @cast_models
    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        dubbing_status: Union[ListDubbingStatus, None] = SENTINEL,
        dubbing_statuses: Union[List[DubbingStatuses], None] = SENTINEL,
        dubbing_models: Union[List[DubbingModels], None] = SENTINEL,
        target_language_codes: Union[List[str], None] = SENTINEL,
        creation_sources: Union[List[CreationSources], None] = SENTINEL,
        filter_by_creator: Union[ListFilterByCreator, None] = SENTINEL,
        order_by: Union[ListOrderBy, None] = SENTINEL,
        order_direction: Union[ListOrderDirection, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingMetadataPageResponseModel:
        """
        List the dubs you have access to.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many dubs to return at maximum. Can not exceed 200, defaults to 100.

        dubbing_status : typing.Optional[ListDubbingStatus]
            What state the dub is currently in.

        dubbing_statuses : typing.Optional[typing.Sequence[DubbingStatuses]]
            Filter by dubbing status.

        dubbing_models : typing.Optional[typing.Sequence[DubbingModels]]
            Filter by dubbing model generation.

        target_language_codes : typing.Optional[typing.Sequence[str]]
            Filter by target language code.

        creation_sources : typing.Optional[typing.Sequence[CreationSources]]
            Filter by dubbing creation source.

        filter_by_creator : typing.Optional[ListFilterByCreator]
            Filters who created the resources being listed, whether it was the user running the request or someone else that shared the resource with them.

        order_by : typing.Optional[ListOrderBy]
            The field to use for ordering results from this query.

        order_direction : typing.Optional[ListOrderDirection]
            The order direction to use for results from this query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingMetadataPageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import ListDubbingStatus, ListFilterByCreator, ListOrderBy, ListOrderDirection

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.list(
            cursor="cursor",
            page_size=100,
            dubbing_status="dubbing",
            dubbing_statuses=[
                "queued"
            ],
            dubbing_models=[
                "dubbing_v1"
            ],
            target_language_codes=[
                "target_language_codes"
            ],
            creation_sources=[
                "flow_node"
            ],
            filter_by_creator="personal",
            order_by="created_at",
            order_direction="DESCENDING",
        )
        """

        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(ListDubbingStatus).is_optional().is_nullable().validate(
            dubbing_status, "dubbing_status"
        )
        Validator(DubbingStatuses).is_array().is_optional().is_nullable().validate(
            dubbing_statuses, "dubbing_statuses"
        )
        Validator(DubbingModels).is_array().is_optional().is_nullable().validate(
            dubbing_models, "dubbing_models"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            target_language_codes, "target_language_codes"
        )
        Validator(CreationSources).is_array().is_optional().is_nullable().validate(
            creation_sources, "creation_sources"
        )
        Validator(ListFilterByCreator).is_optional().is_nullable().validate(
            filter_by_creator, "filter_by_creator"
        )
        Validator(ListOrderBy).is_optional().is_nullable().validate(
            order_by, "order_by"
        )
        Validator(ListOrderDirection).is_optional().is_nullable().validate(
            order_direction, "order_direction"
        )

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("dubbing_status", dubbing_status, nullable=True)
            .add_query("dubbing_statuses", dubbing_statuses, nullable=True)
            .add_query("dubbing_models", dubbing_models, nullable=True)
            .add_query("target_language_codes", target_language_codes, nullable=True)
            .add_query("creation_sources", creation_sources, nullable=True)
            .add_query("filter_by_creator", filter_by_creator, nullable=True)
            .add_query("order_by", order_by, nullable=True)
            .add_query("order_direction", order_direction, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingMetadataPageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingMetadataPageResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        file: Union[bytes, None] = SENTINEL,
        csv_file: Union[bytes, None] = SENTINEL,
        foreground_audio_file: Union[bytes, None] = SENTINEL,
        background_audio_file: Union[bytes, None] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        source_lang: Optional[str] = SENTINEL,
        target_lang: Union[str, None] = SENTINEL,
        target_accent: Union[str, None] = SENTINEL,
        num_speakers: Optional[int] = SENTINEL,
        watermark: Optional[bool] = SENTINEL,
        start_time: Union[int, None] = SENTINEL,
        end_time: Union[int, None] = SENTINEL,
        highest_resolution: Optional[bool] = SENTINEL,
        drop_background_audio: Optional[bool] = SENTINEL,
        use_profanity_filter: Union[bool, None] = SENTINEL,
        dubbing_studio: Optional[bool] = SENTINEL,
        disable_voice_cloning: Optional[bool] = SENTINEL,
        mode: Optional[DubRequestMode] = SENTINEL,
        csv_fps: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DoDubbingResponse:
        """
        Dubs a provided audio or video file into given language.

        Parameters
        ----------
        file : typing.Optional[core.File]
            A list of file paths to audio recordings intended for voice cloning

        csv_file : typing.Optional[core.File]
            CSV file containing transcription/translation metadata

        foreground_audio_file : typing.Optional[core.File]
            For use only with csv input

        background_audio_file : typing.Optional[core.File]
            For use only with csv input

        name : typing.Optional[str]
            Name of the dubbing project.

        source_url : typing.Optional[str]
            URL of the source video/audio file.

        source_lang : typing.Optional[str]
            Source language. Expects a valid iso639-1 or iso639-3 language code.

        target_lang : typing.Optional[str]
            The Target language to dub the content into. Expects a valid iso639-1 or iso639-3 language code.

        target_accent : typing.Optional[str]
            [Experimental] An accent to apply when selecting voices from the library and to use to inform translation of the dialect to prefer.

        num_speakers : typing.Optional[int]
            Number of speakers to use for the dubbing. Set to 0 to automatically detect the number of speakers

        watermark : typing.Optional[bool]
            Whether to apply watermark to the output video.

        start_time : typing.Optional[int]
            Start time of the source video/audio file.

        end_time : typing.Optional[int]
            End time of the source video/audio file.

        highest_resolution : typing.Optional[bool]
            Whether to use the highest resolution available.

        drop_background_audio : typing.Optional[bool]
            An advanced setting. Whether to drop background audio from the final dub. This can improve dub quality where it's known that audio shouldn't have a background track such as for speeches or monologues.

        use_profanity_filter : typing.Optional[bool]
            [BETA] Whether transcripts should have profanities censored with the words '[censored]'

        dubbing_studio : typing.Optional[bool]
            Whether to prepare dub for edits in dubbing studio or edits as a dubbing resource.

        disable_voice_cloning : typing.Optional[bool]
            Instead of using a voice clone in dubbing, use a similar voice from the ElevenLabs Voice Library. Voices used from the library will contribute towards a workspace's custom voices limit, and if there aren't enough available slots the dub will fail. Using this feature requires the caller to have the 'add_voice_from_voice_library' permission on their workspace to access new voices.

        mode : typing.Optional[DubRequestMode]
            The mode in which to run this Dubbing job. Defaults to automatic, use manual if specifically providing a CSV transcript to use. Note that manual mode is experimental and production use is strongly discouraged.

        csv_fps : typing.Optional[float]
            Frames per second to use when parsing a CSV file for dubbing. If not provided, FPS will be inferred from timecodes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DoDubbingResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.create(
            file="file",
            csv_file="csv_file",
            foreground_audio_file="foreground_audio_file",
            background_audio_file="background_audio_file",
            name="name",
            source_url="source_url",
            source_lang="auto",
            target_lang="target_lang",
            target_accent="target_accent",
            num_speakers=9,
            watermark=True,
            start_time=3,
            end_time=8,
            highest_resolution=False,
            drop_background_audio=False,
            use_profanity_filter=True,
            dubbing_studio=False,
            disable_voice_cloning=True,
            mode="automatic",
            csv_fps=3.1,
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = DubRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "csv_file": csv_file,
                        "foreground_audio_file": foreground_audio_file,
                        "background_audio_file": background_audio_file,
                        "name": name,
                        "source_url": source_url,
                        "source_lang": source_lang,
                        "target_lang": target_lang,
                        "target_accent": target_accent,
                        "num_speakers": num_speakers,
                        "watermark": watermark,
                        "start_time": start_time,
                        "end_time": end_time,
                        "highest_resolution": highest_resolution,
                        "drop_background_audio": drop_background_audio,
                        "use_profanity_filter": use_profanity_filter,
                        "dubbing_studio": dubbing_studio,
                        "disable_voice_cloning": disable_voice_cloning,
                        "mode": mode,
                        "csv_fps": csv_fps,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(DubRequest).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing",
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
                DoDubbingResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DoDubbingResponse, response)
            )
        )

    @cast_models
    def get(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DubbingMetadataResponse:
        """
        Returns metadata about a dubbing project, including whether it's still in progress or not

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingMetadataResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.get(
            dubbing_id="dubbing_id",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/{{dubbing_id}}",
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
                DubbingMetadataResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingMetadataResponse, response)
            )
        )

    @cast_models
    def delete(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DeleteDubbingResponseModel:
        """
        Deletes a dubbing project.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDubbingResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.delete(
            dubbing_id="dubbing_id",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/{{dubbing_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteDubbingResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteDubbingResponseModel, response)
            )
        )


class RawDubbingClient:
    """
    Raw-response client for DubbingClient.

    Each method delegates to the matching :class:`DubbingClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: DubbingClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        dubbing_status: Union[ListDubbingStatus, None] = SENTINEL,
        dubbing_statuses: Union[List[DubbingStatuses], None] = SENTINEL,
        dubbing_models: Union[List[DubbingModels], None] = SENTINEL,
        target_language_codes: Union[List[str], None] = SENTINEL,
        creation_sources: Union[List[CreationSources], None] = SENTINEL,
        filter_by_creator: Union[ListFilterByCreator, None] = SENTINEL,
        order_by: Union[ListOrderBy, None] = SENTINEL,
        order_direction: Union[ListOrderDirection, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingMetadataPageResponseModel]:
        data = DubbingClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "dubbing_status": dubbing_status,
                        "dubbing_statuses": dubbing_statuses,
                        "dubbing_models": dubbing_models,
                        "target_language_codes": target_language_codes,
                        "creation_sources": creation_sources,
                        "filter_by_creator": filter_by_creator,
                        "order_by": order_by,
                        "order_direction": order_direction,
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
        file: Union[bytes, None] = SENTINEL,
        csv_file: Union[bytes, None] = SENTINEL,
        foreground_audio_file: Union[bytes, None] = SENTINEL,
        background_audio_file: Union[bytes, None] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        source_lang: Optional[str] = SENTINEL,
        target_lang: Union[str, None] = SENTINEL,
        target_accent: Union[str, None] = SENTINEL,
        num_speakers: Optional[int] = SENTINEL,
        watermark: Optional[bool] = SENTINEL,
        start_time: Union[int, None] = SENTINEL,
        end_time: Union[int, None] = SENTINEL,
        highest_resolution: Optional[bool] = SENTINEL,
        drop_background_audio: Optional[bool] = SENTINEL,
        use_profanity_filter: Union[bool, None] = SENTINEL,
        dubbing_studio: Optional[bool] = SENTINEL,
        disable_voice_cloning: Optional[bool] = SENTINEL,
        mode: Optional[DubRequestMode] = SENTINEL,
        csv_fps: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DoDubbingResponse]:
        data = DubbingClient.create(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "csv_file": csv_file,
                        "foreground_audio_file": foreground_audio_file,
                        "background_audio_file": background_audio_file,
                        "name": name,
                        "source_url": source_url,
                        "source_lang": source_lang,
                        "target_lang": target_lang,
                        "target_accent": target_accent,
                        "num_speakers": num_speakers,
                        "watermark": watermark,
                        "start_time": start_time,
                        "end_time": end_time,
                        "highest_resolution": highest_resolution,
                        "drop_background_audio": drop_background_audio,
                        "use_profanity_filter": use_profanity_filter,
                        "dubbing_studio": dubbing_studio,
                        "disable_voice_cloning": disable_voice_cloning,
                        "mode": mode,
                        "csv_fps": csv_fps,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DubbingMetadataResponse]:
        data = DubbingClient.get(
            self._client, dubbing_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteDubbingResponseModel]:
        data = DubbingClient.delete(
            self._client, dubbing_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDubbingClient(DubbingClient):
    """
    Async wrapper for DubbingClient. Mirrors the sync client's endpoints (awaitable) and, for a
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
    def project(self) -> "_AsyncProjectClient":
        """Lazily construct and return the async project sub-resource client."""
        if self._project is None:
            from .project.client import AsyncProjectClient

            _child = AsyncProjectClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._project = _child
        return self._project

    @property
    def resource(self) -> "_AsyncResourceClient":
        """Lazily construct and return the async resource sub-resource client."""
        if self._resource is None:
            from .resource.client import AsyncResourceClient

            _child = AsyncResourceClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._resource = _child
        return self._resource

    @property
    def transcript(self) -> "_AsyncTranscriptClient":
        """Lazily construct and return the async transcript sub-resource client."""
        if self._transcript is None:
            from .transcript.client import AsyncTranscriptClient

            _child = AsyncTranscriptClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._transcript = _child
        return self._transcript

    @property
    def transcripts(self) -> "_AsyncTranscriptsClient":
        """Lazily construct and return the async transcripts sub-resource client."""
        if self._transcripts is None:
            from .transcripts.client import AsyncTranscriptsClient

            _child = AsyncTranscriptsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._transcripts = _child
        return self._transcripts

    @property
    def with_raw_response(self) -> "AsyncRawDubbingClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDubbingClient(self)

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        dubbing_status: Union[ListDubbingStatus, None] = SENTINEL,
        dubbing_statuses: Union[List[DubbingStatuses], None] = SENTINEL,
        dubbing_models: Union[List[DubbingModels], None] = SENTINEL,
        target_language_codes: Union[List[str], None] = SENTINEL,
        creation_sources: Union[List[CreationSources], None] = SENTINEL,
        filter_by_creator: Union[ListFilterByCreator, None] = SENTINEL,
        order_by: Union[ListOrderBy, None] = SENTINEL,
        order_direction: Union[ListOrderDirection, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingMetadataPageResponseModel]:  # type: ignore[override]
        """
        List the dubs you have access to.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many dubs to return at maximum. Can not exceed 200, defaults to 100.

        dubbing_status : typing.Optional[ListDubbingStatus]
            What state the dub is currently in.

        dubbing_statuses : typing.Optional[typing.Sequence[DubbingStatuses]]
            Filter by dubbing status.

        dubbing_models : typing.Optional[typing.Sequence[DubbingModels]]
            Filter by dubbing model generation.

        target_language_codes : typing.Optional[typing.Sequence[str]]
            Filter by target language code.

        creation_sources : typing.Optional[typing.Sequence[CreationSources]]
            Filter by dubbing creation source.

        filter_by_creator : typing.Optional[ListFilterByCreator]
            Filters who created the resources being listed, whether it was the user running the request or someone else that shared the resource with them.

        order_by : typing.Optional[ListOrderBy]
            The field to use for ordering results from this query.

        order_direction : typing.Optional[ListOrderDirection]
            The order direction to use for results from this query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingMetadataPageResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import ListDubbingStatus, ListFilterByCreator, ListOrderBy, ListOrderDirection

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.list(
                cursor="cursor",
                page_size=100,
                dubbing_status="dubbing",
                dubbing_statuses=[
                    "queued"
                ],
                dubbing_models=[
                    "dubbing_v1"
                ],
                target_language_codes=[
                    "target_language_codes"
                ],
                creation_sources=[
                    "flow_node"
                ],
                filter_by_creator="personal",
                order_by="created_at",
                order_direction="DESCENDING",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "dubbing_status": dubbing_status,
                        "dubbing_statuses": dubbing_statuses,
                        "dubbing_models": dubbing_models,
                        "target_language_codes": target_language_codes,
                        "creation_sources": creation_sources,
                        "filter_by_creator": filter_by_creator,
                        "order_by": order_by,
                        "order_direction": order_direction,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        file: Union[bytes, None] = SENTINEL,
        csv_file: Union[bytes, None] = SENTINEL,
        foreground_audio_file: Union[bytes, None] = SENTINEL,
        background_audio_file: Union[bytes, None] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        source_lang: Optional[str] = SENTINEL,
        target_lang: Union[str, None] = SENTINEL,
        target_accent: Union[str, None] = SENTINEL,
        num_speakers: Optional[int] = SENTINEL,
        watermark: Optional[bool] = SENTINEL,
        start_time: Union[int, None] = SENTINEL,
        end_time: Union[int, None] = SENTINEL,
        highest_resolution: Optional[bool] = SENTINEL,
        drop_background_audio: Optional[bool] = SENTINEL,
        use_profanity_filter: Union[bool, None] = SENTINEL,
        dubbing_studio: Optional[bool] = SENTINEL,
        disable_voice_cloning: Optional[bool] = SENTINEL,
        mode: Optional[DubRequestMode] = SENTINEL,
        csv_fps: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DoDubbingResponse]:  # type: ignore[override]
        """
        Dubs a provided audio or video file into given language.

        Parameters
        ----------
        file : typing.Optional[core.File]
            A list of file paths to audio recordings intended for voice cloning

        csv_file : typing.Optional[core.File]
            CSV file containing transcription/translation metadata

        foreground_audio_file : typing.Optional[core.File]
            For use only with csv input

        background_audio_file : typing.Optional[core.File]
            For use only with csv input

        name : typing.Optional[str]
            Name of the dubbing project.

        source_url : typing.Optional[str]
            URL of the source video/audio file.

        source_lang : typing.Optional[str]
            Source language. Expects a valid iso639-1 or iso639-3 language code.

        target_lang : typing.Optional[str]
            The Target language to dub the content into. Expects a valid iso639-1 or iso639-3 language code.

        target_accent : typing.Optional[str]
            [Experimental] An accent to apply when selecting voices from the library and to use to inform translation of the dialect to prefer.

        num_speakers : typing.Optional[int]
            Number of speakers to use for the dubbing. Set to 0 to automatically detect the number of speakers

        watermark : typing.Optional[bool]
            Whether to apply watermark to the output video.

        start_time : typing.Optional[int]
            Start time of the source video/audio file.

        end_time : typing.Optional[int]
            End time of the source video/audio file.

        highest_resolution : typing.Optional[bool]
            Whether to use the highest resolution available.

        drop_background_audio : typing.Optional[bool]
            An advanced setting. Whether to drop background audio from the final dub. This can improve dub quality where it's known that audio shouldn't have a background track such as for speeches or monologues.

        use_profanity_filter : typing.Optional[bool]
            [BETA] Whether transcripts should have profanities censored with the words '[censored]'

        dubbing_studio : typing.Optional[bool]
            Whether to prepare dub for edits in dubbing studio or edits as a dubbing resource.

        disable_voice_cloning : typing.Optional[bool]
            Instead of using a voice clone in dubbing, use a similar voice from the ElevenLabs Voice Library. Voices used from the library will contribute towards a workspace's custom voices limit, and if there aren't enough available slots the dub will fail. Using this feature requires the caller to have the 'add_voice_from_voice_library' permission on their workspace to access new voices.

        mode : typing.Optional[DubRequestMode]
            The mode in which to run this Dubbing job. Defaults to automatic, use manual if specifically providing a CSV transcript to use. Note that manual mode is experimental and production use is strongly discouraged.

        csv_fps : typing.Optional[float]
            Frames per second to use when parsing a CSV file for dubbing. If not provided, FPS will be inferred from timecodes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DoDubbingResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.create(
                file="file",
                csv_file="csv_file",
                foreground_audio_file="foreground_audio_file",
                background_audio_file="background_audio_file",
                name="name",
                source_url="source_url",
                source_lang="auto",
                target_lang="target_lang",
                target_accent="target_accent",
                num_speakers=9,
                watermark=True,
                start_time=3,
                end_time=8,
                highest_resolution=False,
                drop_background_audio=False,
                use_profanity_filter=True,
                dubbing_studio=False,
                disable_voice_cloning=True,
                mode="automatic",
                csv_fps=3.1,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "csv_file": csv_file,
                        "foreground_audio_file": foreground_audio_file,
                        "background_audio_file": background_audio_file,
                        "name": name,
                        "source_url": source_url,
                        "source_lang": source_lang,
                        "target_lang": target_lang,
                        "target_accent": target_accent,
                        "num_speakers": num_speakers,
                        "watermark": watermark,
                        "start_time": start_time,
                        "end_time": end_time,
                        "highest_resolution": highest_resolution,
                        "drop_background_audio": drop_background_audio,
                        "use_profanity_filter": use_profanity_filter,
                        "dubbing_studio": dubbing_studio,
                        "disable_voice_cloning": disable_voice_cloning,
                        "mode": mode,
                        "csv_fps": csv_fps,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DubbingMetadataResponse]:  # type: ignore[override]
        """
        Returns metadata about a dubbing project, including whether it's still in progress or not

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingMetadataResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.get(
                dubbing_id="dubbing_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(dubbing_id, request_options=request_options)

    def delete(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DeleteDubbingResponseModel]:  # type: ignore[override]
        """
        Deletes a dubbing project.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDubbingResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.delete(
                dubbing_id="dubbing_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(dubbing_id, request_options=request_options)


class AsyncRawDubbingClient:
    """
    Async raw-response client for AsyncDubbingClient.
    """

    def __init__(self, client: AsyncDubbingClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        dubbing_status: Union[ListDubbingStatus, None] = SENTINEL,
        dubbing_statuses: Union[List[DubbingStatuses], None] = SENTINEL,
        dubbing_models: Union[List[DubbingModels], None] = SENTINEL,
        target_language_codes: Union[List[str], None] = SENTINEL,
        creation_sources: Union[List[CreationSources], None] = SENTINEL,
        filter_by_creator: Union[ListFilterByCreator, None] = SENTINEL,
        order_by: Union[ListOrderBy, None] = SENTINEL,
        order_direction: Union[ListOrderDirection, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingMetadataPageResponseModel]:
        data = await AsyncDubbingClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "dubbing_status": dubbing_status,
                        "dubbing_statuses": dubbing_statuses,
                        "dubbing_models": dubbing_models,
                        "target_language_codes": target_language_codes,
                        "creation_sources": creation_sources,
                        "filter_by_creator": filter_by_creator,
                        "order_by": order_by,
                        "order_direction": order_direction,
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
        file: Union[bytes, None] = SENTINEL,
        csv_file: Union[bytes, None] = SENTINEL,
        foreground_audio_file: Union[bytes, None] = SENTINEL,
        background_audio_file: Union[bytes, None] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        source_lang: Optional[str] = SENTINEL,
        target_lang: Union[str, None] = SENTINEL,
        target_accent: Union[str, None] = SENTINEL,
        num_speakers: Optional[int] = SENTINEL,
        watermark: Optional[bool] = SENTINEL,
        start_time: Union[int, None] = SENTINEL,
        end_time: Union[int, None] = SENTINEL,
        highest_resolution: Optional[bool] = SENTINEL,
        drop_background_audio: Optional[bool] = SENTINEL,
        use_profanity_filter: Union[bool, None] = SENTINEL,
        dubbing_studio: Optional[bool] = SENTINEL,
        disable_voice_cloning: Optional[bool] = SENTINEL,
        mode: Optional[DubRequestMode] = SENTINEL,
        csv_fps: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DoDubbingResponse]:
        data = await AsyncDubbingClient.create(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "csv_file": csv_file,
                        "foreground_audio_file": foreground_audio_file,
                        "background_audio_file": background_audio_file,
                        "name": name,
                        "source_url": source_url,
                        "source_lang": source_lang,
                        "target_lang": target_lang,
                        "target_accent": target_accent,
                        "num_speakers": num_speakers,
                        "watermark": watermark,
                        "start_time": start_time,
                        "end_time": end_time,
                        "highest_resolution": highest_resolution,
                        "drop_background_audio": drop_background_audio,
                        "use_profanity_filter": use_profanity_filter,
                        "dubbing_studio": dubbing_studio,
                        "disable_voice_cloning": disable_voice_cloning,
                        "mode": mode,
                        "csv_fps": csv_fps,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DubbingMetadataResponse]:
        data = await AsyncDubbingClient.get(
            self._client, dubbing_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, dubbing_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteDubbingResponseModel]:
        data = await AsyncDubbingClient.delete(
            self._client, dubbing_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
