from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    AddProjectResponseModel,
    BodyCreateStudioProjectV1StudioProjectsPost,
    BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization,
    BodyCreateStudioProjectV1StudioProjectsPostFiction,
    BodyCreateStudioProjectV1StudioProjectsPostSourceType,
    BodyCreateStudioProjectV1StudioProjectsPostTargetAudience,
    BodyUpdateStudioProjectV1StudioProjectsProjectIdPost,
    ConvertProjectResponseModel,
    DeleteProjectResponseModel,
    EditProjectResponseModel,
    GetProjectsResponse,
    HttpValidationError,
    ProjectExtendedResponse,
    ProjectMutedTracksResponseModel,
    QualityPresetType,
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
    from .pronunciation_dictionaries.client import (
        PronunciationDictionariesClient as _PronunciationDictionariesClient,
        AsyncPronunciationDictionariesClient as _AsyncPronunciationDictionariesClient,
    )
    from .content.client import (
        ContentClient as _ContentClient,
        AsyncContentClient as _AsyncContentClient,
    )
    from .snapshots.client import (
        SnapshotsClient as _SnapshotsClient,
        AsyncSnapshotsClient as _AsyncSnapshotsClient,
    )
    from .chapters.client import (
        ChaptersClient as _ChaptersClient,
        AsyncChaptersClient as _AsyncChaptersClient,
    )


class ProjectsClient(BaseService):
    """
    Fern-style resource client for ProjectsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._pronunciation_dictionaries: Any = None
        self._content: Any = None
        self._snapshots: Any = None
        self._chapters: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._convert_config: SdkConfig = {}
        self._get_muted_tracks_config: SdkConfig = {}

    @property
    def pronunciation_dictionaries(self) -> "_PronunciationDictionariesClient":
        """Lazily construct and return the pronunciation_dictionaries sub-resource client."""
        if self._pronunciation_dictionaries is None:
            from .pronunciation_dictionaries.client import (
                PronunciationDictionariesClient,
            )

            _child = PronunciationDictionariesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._pronunciation_dictionaries = _child
        return self._pronunciation_dictionaries

    @property
    def content(self) -> "_ContentClient":
        """Lazily construct and return the content sub-resource client."""
        if self._content is None:
            from .content.client import ContentClient

            _child = ContentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._content = _child
        return self._content

    @property
    def snapshots(self) -> "_SnapshotsClient":
        """Lazily construct and return the snapshots sub-resource client."""
        if self._snapshots is None:
            from .snapshots.client import SnapshotsClient

            _child = SnapshotsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._snapshots = _child
        return self._snapshots

    @property
    def chapters(self) -> "_ChaptersClient":
        """Lazily construct and return the chapters sub-resource client."""
        if self._chapters is None:
            from .chapters.client import ChaptersClient

            _child = ChaptersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._chapters = _child
        return self._chapters

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
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_base_url(base_url)
        if self._content is not None:
            self._content.set_base_url(base_url)
        if self._snapshots is not None:
            self._snapshots.set_base_url(base_url)
        if self._chapters is not None:
            self._chapters.set_base_url(base_url)

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
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_config(config)
        if self._content is not None:
            self._content.set_config(config)
        if self._snapshots is not None:
            self._snapshots.set_config(config)
        if self._chapters is not None:
            self._chapters.set_config(config)

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
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_timeout(timeout)
        if self._content is not None:
            self._content.set_timeout(timeout)
        if self._snapshots is not None:
            self._snapshots.set_timeout(timeout)
        if self._chapters is not None:
            self._chapters.set_timeout(timeout)

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

    def set_convert_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_config = config
        return self

    def set_get_muted_tracks_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_muted_tracks.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_muted_tracks_config = config
        return self

    @property
    def with_raw_response(self) -> "RawProjectsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawProjectsClient(self)

    @cast_models
    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> GetProjectsResponse:
        """
        Returns a list of your Studio projects with metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectsResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.list()
        """

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetProjectsResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetProjectsResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        name: str,
        default_title_voice_id: Union[str, None] = SENTINEL,
        default_paragraph_voice_id: Union[str, None] = SENTINEL,
        default_model_id: Union[str, None] = SENTINEL,
        from_url: Union[str, None] = SENTINEL,
        from_document: Union[bytes, None] = SENTINEL,
        from_content_json: Optional[str] = SENTINEL,
        quality_preset: Optional[QualityPresetType] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        genres: Optional[List[str]] = SENTINEL,
        target_audience: Union[
            BodyCreateStudioProjectV1StudioProjectsPostTargetAudience, None
        ] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        content_type: Union[str, None] = SENTINEL,
        original_publication_date: Union[str, None] = SENTINEL,
        mature_content: Union[bool, None] = SENTINEL,
        isbn_number: Union[str, None] = SENTINEL,
        acx_volume_normalization: Optional[bool] = SENTINEL,
        volume_normalization: Optional[bool] = SENTINEL,
        pronunciation_dictionary_locators: Optional[List[str]] = SENTINEL,
        callback_url: Union[str, None] = SENTINEL,
        fiction: Union[
            BodyCreateStudioProjectV1StudioProjectsPostFiction, None
        ] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization, None
        ] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        auto_assign_voices: Union[bool, None] = SENTINEL,
        source_type: Union[
            BodyCreateStudioProjectV1StudioProjectsPostSourceType, None
        ] = SENTINEL,
        voice_settings: Optional[List[str]] = SENTINEL,
        create_publishing_read: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddProjectResponseModel:
        """
        Creates a new Studio project, it can be either initialized as blank, from a document or from a URL.

        Parameters
        ----------
        name : str
            The name of the Studio project, used for identification only.

        default_title_voice_id : typing.Optional[str]
            The voice_id that corresponds to the default voice used for new titles.

        default_paragraph_voice_id : typing.Optional[str]
            The voice_id that corresponds to the default voice used for new paragraphs.

        default_model_id : typing.Optional[str]
            The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models.

        from_url : typing.Optional[str]
            An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        from_document : typing.Optional[core.File]
            An optional .epub, .pdf, .txt or similar file can be provided. If provided, we will initialize the Studio project with its content. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        from_content_json : typing.Optional[str]
            An optional content to initialize the Studio project with. If this is set, 'from_url' and 'from_document' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

                Example:
                [{"name": "Chapter A", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts_node"}]}, {"sub_type": "h1", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts_node"}]}]}, {"name": "Chapter B", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts_node"}]}, {"sub_type": "h2", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts_node"}]}]}]

        quality_preset : typing.Optional[QualityPresetType]

        title : typing.Optional[str]
            An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.

        author : typing.Optional[str]
            An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.

        description : typing.Optional[str]
            An optional description of the Studio project.

        genres : typing.Optional[typing.Sequence[str]]
            An optional list of genres associated with the Studio project.

        target_audience : typing.Optional[BodyCreateStudioProjectV1StudioProjectsPostTargetAudience]
            An optional target audience of the Studio project.

        language : typing.Optional[str]
            An optional language of the Studio project. Two-letter language code (ISO 639-1).

        content_type : typing.Optional[str]
            An optional content type of the Studio project.

        original_publication_date : typing.Optional[str]
            An optional original publication date of the Studio project, in the format YYYY-MM-DD or YYYY.

        mature_content : typing.Optional[bool]
            An optional specification of whether this Studio project contains mature content.

        isbn_number : typing.Optional[str]
            An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download.

        acx_volume_normalization : typing.Optional[bool]
            [Deprecated] When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements

        volume_normalization : typing.Optional[bool]
            When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[str]]
            A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'.

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

        fiction : typing.Optional[BodyCreateStudioProjectV1StudioProjectsPostFiction]
            An optional specification of whether the content of this Studio project is fiction.

        apply_text_normalization : typing.Optional[BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization]
            This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
                When set to 'auto', the system will automatically decide whether to apply text normalization
                (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
                with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.

        auto_convert : typing.Optional[bool]
            Whether to auto convert the Studio project to audio or not.

        auto_assign_voices : typing.Optional[bool]
            [Alpha Feature] Whether automatically assign voices to phrases in the create Project.

        source_type : typing.Optional[BodyCreateStudioProjectV1StudioProjectsPostSourceType]
            The type of Studio project to create.

        voice_settings : typing.Optional[typing.Sequence[str]]
            Optional voice settings overrides for the project, encoded as a list of JSON strings.

                Example:
                ["{\\"voice_id\\": \\"21m00Tcm4TlvDq8ikWAM\\", \\"stability\\": 0.7, \\"similarity_boost\\": 0.8, \\"style\\": 0.5, \\"speed\\": 1.0, \\"use_speaker_boost\\": true}"]

        create_publishing_read : typing.Optional[bool]
            If true, creates a corresponding read for direct publishing in draft state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddProjectResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.create(
            name="Project 1",
            default_title_voice_id="default_title_voice_id",
            default_paragraph_voice_id="default_paragraph_voice_id",
            default_model_id="default_model_id",
            from_url="from_url",
            from_document="from_document",
            from_content_json="[{\\"name\\": \\"Chapter A\\", \\"blocks\\": [{\\"sub_type\\": \\"p\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"A\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"B\\", \\"type\\": \\"tts_node\\"}]}, {\\"sub_type\\": \\"h1\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"C\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"D\\", \\"type\\": \\"tts_node\\"}]}]}, {\\"name\\": \\"Chapter B\\", \\"blocks\\": [{\\"sub_type\\": \\"p\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"E\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"F\\", \\"type\\": \\"tts_node\\"}]}, {\\"sub_type\\": \\"h2\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"G\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"H\\", \\"type\\": \\"tts_node\\"}]}]}]",
            quality_preset="standard",
            title="title",
            author="author",
            description="description",
            genres=[
                "genres"
            ],
            target_audience="children",
            language="ir",
            content_type="content_type",
            original_publication_date="9179-04-48",
            mature_content=True,
            isbn_number="isbn_number",
            acx_volume_normalization=False,
            volume_normalization=True,
            pronunciation_dictionary_locators=[
                "pronunciation_dictionary_locators"
            ],
            callback_url="callback_url",
            fiction="fiction",
            apply_text_normalization="auto",
            auto_convert=True,
            auto_assign_voices=True,
            source_type="blank",
            voice_settings=[
                "voice_settings"
            ],
            create_publishing_read=False,
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateStudioProjectV1StudioProjectsPost(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "default_title_voice_id": default_title_voice_id,
                        "default_paragraph_voice_id": default_paragraph_voice_id,
                        "default_model_id": default_model_id,
                        "from_url": from_url,
                        "from_document": from_document,
                        "from_content_json": from_content_json,
                        "quality_preset": quality_preset,
                        "title": title,
                        "author": author,
                        "description": description,
                        "genres": genres,
                        "target_audience": target_audience,
                        "language": language,
                        "content_type": content_type,
                        "original_publication_date": original_publication_date,
                        "mature_content": mature_content,
                        "isbn_number": isbn_number,
                        "acx_volume_normalization": acx_volume_normalization,
                        "volume_normalization": volume_normalization,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "callback_url": callback_url,
                        "fiction": fiction,
                        "apply_text_normalization": apply_text_normalization,
                        "auto_convert": auto_convert,
                        "auto_assign_voices": auto_assign_voices,
                        "source_type": source_type,
                        "voice_settings": voice_settings,
                        "create_publishing_read": create_publishing_read,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateStudioProjectV1StudioProjectsPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects",
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
                AddProjectResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddProjectResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        project_id: str,
        *,
        share_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ProjectExtendedResponse:
        """
        Returns information about a specific Studio project. This endpoint returns more detailed information about a project than `GET /v1/studio`.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        share_id : typing.Optional[str]
            The share ID of the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectExtendedResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.get(
            project_id="21m00Tcm4TlvDq8ikWAM",
            share_id="share_id",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).is_optional().is_nullable().validate(share_id, "share_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_query("share_id", share_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ProjectExtendedResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ProjectExtendedResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        project_id: str,
        *,
        name: str,
        default_title_voice_id: str,
        default_paragraph_voice_id: str,
        title: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        isbn_number: Union[str, None] = SENTINEL,
        volume_normalization: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> EditProjectResponseModel:
        """
        Updates the specified Studio project by setting the values of the parameters passed.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        name : str
            The name of the Studio project, used for identification only.

        default_title_voice_id : str
            The voice_id that corresponds to the default voice used for new titles.

        default_paragraph_voice_id : str
            The voice_id that corresponds to the default voice used for new paragraphs.

        title : typing.Optional[str]
            An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.

        author : typing.Optional[str]
            An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.

        isbn_number : typing.Optional[str]
            An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download.

        volume_normalization : typing.Optional[bool]
            When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditProjectResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.update(
            project_id="21m00Tcm4TlvDq8ikWAM",
            name="Project 1",
            default_title_voice_id="21m00Tcm4TlvDq8ikWAM",
            default_paragraph_voice_id="21m00Tcm4TlvDq8ikWAM",
            title="title",
            author="author",
            isbn_number="isbn_number",
            volume_normalization=True,
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdateStudioProjectV1StudioProjectsProjectIdPost(
            name=name,
            default_title_voice_id=default_title_voice_id,
            default_paragraph_voice_id=default_paragraph_voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "title": title,
                        "author": author,
                        "isbn_number": isbn_number,
                        "volume_normalization": volume_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyUpdateStudioProjectV1StudioProjectsProjectIdPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                EditProjectResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EditProjectResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DeleteProjectResponseModel:
        """
        Deletes a Studio project.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteProjectResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.delete(
            project_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteProjectResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteProjectResponseModel, response)
            )
        )

    @cast_models
    def convert(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> ConvertProjectResponseModel:
        """
        Starts conversion of a Studio project and all of its chapters.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConvertProjectResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.convert(
            project_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._convert_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/convert",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ConvertProjectResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConvertProjectResponseModel, response)
            )
        )

    @cast_models
    def get_muted_tracks(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> ProjectMutedTracksResponseModel:
        """
        Returns a list of chapter IDs that have muted tracks in a project.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectMutedTracksResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.get_muted_tracks(
            project_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._get_muted_tracks_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/muted-tracks",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ProjectMutedTracksResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ProjectMutedTracksResponseModel, response)
            )
        )


class RawProjectsClient:
    """
    Raw-response client for ProjectsClient.

    Each method delegates to the matching :class:`ProjectsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ProjectsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetProjectsResponse]:
        data = ProjectsClient.list(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        name: str,
        default_title_voice_id: Union[str, None] = SENTINEL,
        default_paragraph_voice_id: Union[str, None] = SENTINEL,
        default_model_id: Union[str, None] = SENTINEL,
        from_url: Union[str, None] = SENTINEL,
        from_document: Union[bytes, None] = SENTINEL,
        from_content_json: Optional[str] = SENTINEL,
        quality_preset: Optional[QualityPresetType] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        genres: Optional[List[str]] = SENTINEL,
        target_audience: Union[
            BodyCreateStudioProjectV1StudioProjectsPostTargetAudience, None
        ] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        content_type: Union[str, None] = SENTINEL,
        original_publication_date: Union[str, None] = SENTINEL,
        mature_content: Union[bool, None] = SENTINEL,
        isbn_number: Union[str, None] = SENTINEL,
        acx_volume_normalization: Optional[bool] = SENTINEL,
        volume_normalization: Optional[bool] = SENTINEL,
        pronunciation_dictionary_locators: Optional[List[str]] = SENTINEL,
        callback_url: Union[str, None] = SENTINEL,
        fiction: Union[
            BodyCreateStudioProjectV1StudioProjectsPostFiction, None
        ] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization, None
        ] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        auto_assign_voices: Union[bool, None] = SENTINEL,
        source_type: Union[
            BodyCreateStudioProjectV1StudioProjectsPostSourceType, None
        ] = SENTINEL,
        voice_settings: Optional[List[str]] = SENTINEL,
        create_publishing_read: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddProjectResponseModel]:
        data = ProjectsClient.create(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "default_title_voice_id": default_title_voice_id,
                        "default_paragraph_voice_id": default_paragraph_voice_id,
                        "default_model_id": default_model_id,
                        "from_url": from_url,
                        "from_document": from_document,
                        "from_content_json": from_content_json,
                        "quality_preset": quality_preset,
                        "title": title,
                        "author": author,
                        "description": description,
                        "genres": genres,
                        "target_audience": target_audience,
                        "language": language,
                        "content_type": content_type,
                        "original_publication_date": original_publication_date,
                        "mature_content": mature_content,
                        "isbn_number": isbn_number,
                        "acx_volume_normalization": acx_volume_normalization,
                        "volume_normalization": volume_normalization,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "callback_url": callback_url,
                        "fiction": fiction,
                        "apply_text_normalization": apply_text_normalization,
                        "auto_convert": auto_convert,
                        "auto_assign_voices": auto_assign_voices,
                        "source_type": source_type,
                        "voice_settings": voice_settings,
                        "create_publishing_read": create_publishing_read,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        project_id: str,
        *,
        share_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectExtendedResponse]:
        data = ProjectsClient.get(
            self._client,
            project_id,
            **dict[str, Any](
                {k: v for k, v in {"share_id": share_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        project_id: str,
        *,
        name: str,
        default_title_voice_id: str,
        default_paragraph_voice_id: str,
        title: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        isbn_number: Union[str, None] = SENTINEL,
        volume_normalization: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditProjectResponseModel]:
        data = ProjectsClient.update(
            self._client,
            project_id,
            name=name,
            default_title_voice_id=default_title_voice_id,
            default_paragraph_voice_id=default_paragraph_voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "title": title,
                        "author": author,
                        "isbn_number": isbn_number,
                        "volume_normalization": volume_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteProjectResponseModel]:
        data = ProjectsClient.delete(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def convert(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ConvertProjectResponseModel]:
        data = ProjectsClient.convert(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_muted_tracks(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectMutedTracksResponseModel]:
        data = ProjectsClient.get_muted_tracks(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncProjectsClient(ProjectsClient):
    """
    Async wrapper for ProjectsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def pronunciation_dictionaries(self) -> "_AsyncPronunciationDictionariesClient":
        """Lazily construct and return the async pronunciation_dictionaries sub-resource client."""
        if self._pronunciation_dictionaries is None:
            from .pronunciation_dictionaries.client import (
                AsyncPronunciationDictionariesClient,
            )

            _child = AsyncPronunciationDictionariesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._pronunciation_dictionaries = _child
        return self._pronunciation_dictionaries

    @property
    def content(self) -> "_AsyncContentClient":
        """Lazily construct and return the async content sub-resource client."""
        if self._content is None:
            from .content.client import AsyncContentClient

            _child = AsyncContentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._content = _child
        return self._content

    @property
    def snapshots(self) -> "_AsyncSnapshotsClient":
        """Lazily construct and return the async snapshots sub-resource client."""
        if self._snapshots is None:
            from .snapshots.client import AsyncSnapshotsClient

            _child = AsyncSnapshotsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._snapshots = _child
        return self._snapshots

    @property
    def chapters(self) -> "_AsyncChaptersClient":
        """Lazily construct and return the async chapters sub-resource client."""
        if self._chapters is None:
            from .chapters.client import AsyncChaptersClient

            _child = AsyncChaptersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._chapters = _child
        return self._chapters

    @property
    def with_raw_response(self) -> "AsyncRawProjectsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawProjectsClient(self)

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetProjectsResponse]:  # type: ignore[override]
        """
        Returns a list of your Studio projects with metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.list()


        asyncio.run(main())
        """
        return to_async(super().list)(request_options=request_options)

    def create(
        self,
        *,
        name: str,
        default_title_voice_id: Union[str, None] = SENTINEL,
        default_paragraph_voice_id: Union[str, None] = SENTINEL,
        default_model_id: Union[str, None] = SENTINEL,
        from_url: Union[str, None] = SENTINEL,
        from_document: Union[bytes, None] = SENTINEL,
        from_content_json: Optional[str] = SENTINEL,
        quality_preset: Optional[QualityPresetType] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        genres: Optional[List[str]] = SENTINEL,
        target_audience: Union[
            BodyCreateStudioProjectV1StudioProjectsPostTargetAudience, None
        ] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        content_type: Union[str, None] = SENTINEL,
        original_publication_date: Union[str, None] = SENTINEL,
        mature_content: Union[bool, None] = SENTINEL,
        isbn_number: Union[str, None] = SENTINEL,
        acx_volume_normalization: Optional[bool] = SENTINEL,
        volume_normalization: Optional[bool] = SENTINEL,
        pronunciation_dictionary_locators: Optional[List[str]] = SENTINEL,
        callback_url: Union[str, None] = SENTINEL,
        fiction: Union[
            BodyCreateStudioProjectV1StudioProjectsPostFiction, None
        ] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization, None
        ] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        auto_assign_voices: Union[bool, None] = SENTINEL,
        source_type: Union[
            BodyCreateStudioProjectV1StudioProjectsPostSourceType, None
        ] = SENTINEL,
        voice_settings: Optional[List[str]] = SENTINEL,
        create_publishing_read: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddProjectResponseModel]:  # type: ignore[override]
        """
        Creates a new Studio project, it can be either initialized as blank, from a document or from a URL.

        Parameters
        ----------
        name : str
            The name of the Studio project, used for identification only.

        default_title_voice_id : typing.Optional[str]
            The voice_id that corresponds to the default voice used for new titles.

        default_paragraph_voice_id : typing.Optional[str]
            The voice_id that corresponds to the default voice used for new paragraphs.

        default_model_id : typing.Optional[str]
            The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models.

        from_url : typing.Optional[str]
            An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        from_document : typing.Optional[core.File]
            An optional .epub, .pdf, .txt or similar file can be provided. If provided, we will initialize the Studio project with its content. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        from_content_json : typing.Optional[str]
            An optional content to initialize the Studio project with. If this is set, 'from_url' and 'from_document' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

                Example:
                [{"name": "Chapter A", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts_node"}]}, {"sub_type": "h1", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts_node"}]}]}, {"name": "Chapter B", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts_node"}]}, {"sub_type": "h2", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts_node"}]}]}]

        quality_preset : typing.Optional[QualityPresetType]

        title : typing.Optional[str]
            An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.

        author : typing.Optional[str]
            An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.

        description : typing.Optional[str]
            An optional description of the Studio project.

        genres : typing.Optional[typing.Sequence[str]]
            An optional list of genres associated with the Studio project.

        target_audience : typing.Optional[BodyCreateStudioProjectV1StudioProjectsPostTargetAudience]
            An optional target audience of the Studio project.

        language : typing.Optional[str]
            An optional language of the Studio project. Two-letter language code (ISO 639-1).

        content_type : typing.Optional[str]
            An optional content type of the Studio project.

        original_publication_date : typing.Optional[str]
            An optional original publication date of the Studio project, in the format YYYY-MM-DD or YYYY.

        mature_content : typing.Optional[bool]
            An optional specification of whether this Studio project contains mature content.

        isbn_number : typing.Optional[str]
            An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download.

        acx_volume_normalization : typing.Optional[bool]
            [Deprecated] When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements

        volume_normalization : typing.Optional[bool]
            When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[str]]
            A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'.

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

        fiction : typing.Optional[BodyCreateStudioProjectV1StudioProjectsPostFiction]
            An optional specification of whether the content of this Studio project is fiction.

        apply_text_normalization : typing.Optional[BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization]
            This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
                When set to 'auto', the system will automatically decide whether to apply text normalization
                (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
                with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.

        auto_convert : typing.Optional[bool]
            Whether to auto convert the Studio project to audio or not.

        auto_assign_voices : typing.Optional[bool]
            [Alpha Feature] Whether automatically assign voices to phrases in the create Project.

        source_type : typing.Optional[BodyCreateStudioProjectV1StudioProjectsPostSourceType]
            The type of Studio project to create.

        voice_settings : typing.Optional[typing.Sequence[str]]
            Optional voice settings overrides for the project, encoded as a list of JSON strings.

                Example:
                ["{\\"voice_id\\": \\"21m00Tcm4TlvDq8ikWAM\\", \\"stability\\": 0.7, \\"similarity_boost\\": 0.8, \\"style\\": 0.5, \\"speed\\": 1.0, \\"use_speaker_boost\\": true}"]

        create_publishing_read : typing.Optional[bool]
            If true, creates a corresponding read for direct publishing in draft state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddProjectResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.create(
                name="Project 1",
                default_title_voice_id="default_title_voice_id",
                default_paragraph_voice_id="default_paragraph_voice_id",
                default_model_id="default_model_id",
                from_url="from_url",
                from_document="from_document",
                from_content_json="[{\\"name\\": \\"Chapter A\\", \\"blocks\\": [{\\"sub_type\\": \\"p\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"A\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"B\\", \\"type\\": \\"tts_node\\"}]}, {\\"sub_type\\": \\"h1\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"C\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"D\\", \\"type\\": \\"tts_node\\"}]}]}, {\\"name\\": \\"Chapter B\\", \\"blocks\\": [{\\"sub_type\\": \\"p\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"E\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"F\\", \\"type\\": \\"tts_node\\"}]}, {\\"sub_type\\": \\"h2\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"G\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"H\\", \\"type\\": \\"tts_node\\"}]}]}]",
                quality_preset="standard",
                title="title",
                author="author",
                description="description",
                genres=[
                    "genres"
                ],
                target_audience="children",
                language="ir",
                content_type="content_type",
                original_publication_date="9179-04-48",
                mature_content=True,
                isbn_number="isbn_number",
                acx_volume_normalization=False,
                volume_normalization=True,
                pronunciation_dictionary_locators=[
                    "pronunciation_dictionary_locators"
                ],
                callback_url="callback_url",
                fiction="fiction",
                apply_text_normalization="auto",
                auto_convert=True,
                auto_assign_voices=True,
                source_type="blank",
                voice_settings=[
                    "voice_settings"
                ],
                create_publishing_read=False,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "default_title_voice_id": default_title_voice_id,
                        "default_paragraph_voice_id": default_paragraph_voice_id,
                        "default_model_id": default_model_id,
                        "from_url": from_url,
                        "from_document": from_document,
                        "from_content_json": from_content_json,
                        "quality_preset": quality_preset,
                        "title": title,
                        "author": author,
                        "description": description,
                        "genres": genres,
                        "target_audience": target_audience,
                        "language": language,
                        "content_type": content_type,
                        "original_publication_date": original_publication_date,
                        "mature_content": mature_content,
                        "isbn_number": isbn_number,
                        "acx_volume_normalization": acx_volume_normalization,
                        "volume_normalization": volume_normalization,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "callback_url": callback_url,
                        "fiction": fiction,
                        "apply_text_normalization": apply_text_normalization,
                        "auto_convert": auto_convert,
                        "auto_assign_voices": auto_assign_voices,
                        "source_type": source_type,
                        "voice_settings": voice_settings,
                        "create_publishing_read": create_publishing_read,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        project_id: str,
        *,
        share_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ProjectExtendedResponse]:  # type: ignore[override]
        """
        Returns information about a specific Studio project. This endpoint returns more detailed information about a project than `GET /v1/studio`.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        share_id : typing.Optional[str]
            The share ID of the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectExtendedResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.get(
                project_id="21m00Tcm4TlvDq8ikWAM",
                share_id="share_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            project_id,
            **dict[str, Any](
                {k: v for k, v in {"share_id": share_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def update(
        self,
        project_id: str,
        *,
        name: str,
        default_title_voice_id: str,
        default_paragraph_voice_id: str,
        title: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        isbn_number: Union[str, None] = SENTINEL,
        volume_normalization: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EditProjectResponseModel]:  # type: ignore[override]
        """
        Updates the specified Studio project by setting the values of the parameters passed.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        name : str
            The name of the Studio project, used for identification only.

        default_title_voice_id : str
            The voice_id that corresponds to the default voice used for new titles.

        default_paragraph_voice_id : str
            The voice_id that corresponds to the default voice used for new paragraphs.

        title : typing.Optional[str]
            An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.

        author : typing.Optional[str]
            An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.

        isbn_number : typing.Optional[str]
            An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download.

        volume_normalization : typing.Optional[bool]
            When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditProjectResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.update(
                project_id="21m00Tcm4TlvDq8ikWAM",
                name="Project 1",
                default_title_voice_id="21m00Tcm4TlvDq8ikWAM",
                default_paragraph_voice_id="21m00Tcm4TlvDq8ikWAM",
                title="title",
                author="author",
                isbn_number="isbn_number",
                volume_normalization=True,
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            project_id,
            name=name,
            default_title_voice_id=default_title_voice_id,
            default_paragraph_voice_id=default_paragraph_voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "title": title,
                        "author": author,
                        "isbn_number": isbn_number,
                        "volume_normalization": volume_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DeleteProjectResponseModel]:  # type: ignore[override]
        """
        Deletes a Studio project.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteProjectResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.delete(
                project_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(project_id, request_options=request_options)

    def convert(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[ConvertProjectResponseModel]:  # type: ignore[override]
        """
        Starts conversion of a Studio project and all of its chapters.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConvertProjectResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.convert(
                project_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().convert)(project_id, request_options=request_options)

    def get_muted_tracks(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[ProjectMutedTracksResponseModel]:  # type: ignore[override]
        """
        Returns a list of chapter IDs that have muted tracks in a project.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectMutedTracksResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.get_muted_tracks(
                project_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get_muted_tracks)(
            project_id, request_options=request_options
        )


class AsyncRawProjectsClient:
    """
    Async raw-response client for AsyncProjectsClient.
    """

    def __init__(self, client: AsyncProjectsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetProjectsResponse]:
        data = await AsyncProjectsClient.list(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        name: str,
        default_title_voice_id: Union[str, None] = SENTINEL,
        default_paragraph_voice_id: Union[str, None] = SENTINEL,
        default_model_id: Union[str, None] = SENTINEL,
        from_url: Union[str, None] = SENTINEL,
        from_document: Union[bytes, None] = SENTINEL,
        from_content_json: Optional[str] = SENTINEL,
        quality_preset: Optional[QualityPresetType] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        genres: Optional[List[str]] = SENTINEL,
        target_audience: Union[
            BodyCreateStudioProjectV1StudioProjectsPostTargetAudience, None
        ] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        content_type: Union[str, None] = SENTINEL,
        original_publication_date: Union[str, None] = SENTINEL,
        mature_content: Union[bool, None] = SENTINEL,
        isbn_number: Union[str, None] = SENTINEL,
        acx_volume_normalization: Optional[bool] = SENTINEL,
        volume_normalization: Optional[bool] = SENTINEL,
        pronunciation_dictionary_locators: Optional[List[str]] = SENTINEL,
        callback_url: Union[str, None] = SENTINEL,
        fiction: Union[
            BodyCreateStudioProjectV1StudioProjectsPostFiction, None
        ] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreateStudioProjectV1StudioProjectsPostApplyTextNormalization, None
        ] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        auto_assign_voices: Union[bool, None] = SENTINEL,
        source_type: Union[
            BodyCreateStudioProjectV1StudioProjectsPostSourceType, None
        ] = SENTINEL,
        voice_settings: Optional[List[str]] = SENTINEL,
        create_publishing_read: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddProjectResponseModel]:
        data = await AsyncProjectsClient.create(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "default_title_voice_id": default_title_voice_id,
                        "default_paragraph_voice_id": default_paragraph_voice_id,
                        "default_model_id": default_model_id,
                        "from_url": from_url,
                        "from_document": from_document,
                        "from_content_json": from_content_json,
                        "quality_preset": quality_preset,
                        "title": title,
                        "author": author,
                        "description": description,
                        "genres": genres,
                        "target_audience": target_audience,
                        "language": language,
                        "content_type": content_type,
                        "original_publication_date": original_publication_date,
                        "mature_content": mature_content,
                        "isbn_number": isbn_number,
                        "acx_volume_normalization": acx_volume_normalization,
                        "volume_normalization": volume_normalization,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                        "callback_url": callback_url,
                        "fiction": fiction,
                        "apply_text_normalization": apply_text_normalization,
                        "auto_convert": auto_convert,
                        "auto_assign_voices": auto_assign_voices,
                        "source_type": source_type,
                        "voice_settings": voice_settings,
                        "create_publishing_read": create_publishing_read,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        project_id: str,
        *,
        share_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectExtendedResponse]:
        data = await AsyncProjectsClient.get(
            self._client,
            project_id,
            **dict[str, Any](
                {k: v for k, v in {"share_id": share_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        project_id: str,
        *,
        name: str,
        default_title_voice_id: str,
        default_paragraph_voice_id: str,
        title: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        isbn_number: Union[str, None] = SENTINEL,
        volume_normalization: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditProjectResponseModel]:
        data = await AsyncProjectsClient.update(
            self._client,
            project_id,
            name=name,
            default_title_voice_id=default_title_voice_id,
            default_paragraph_voice_id=default_paragraph_voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "title": title,
                        "author": author,
                        "isbn_number": isbn_number,
                        "volume_normalization": volume_normalization,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteProjectResponseModel]:
        data = await AsyncProjectsClient.delete(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def convert(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ConvertProjectResponseModel]:
        data = await AsyncProjectsClient.convert(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_muted_tracks(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectMutedTracksResponseModel]:
        data = await AsyncProjectsClient.get_muted_tracks(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
