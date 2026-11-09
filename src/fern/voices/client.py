from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AddVoiceResponseModel,
    BodyAddSharedVoiceV1VoicesAddPublicUserIdVoiceIdPost,
    DeleteVoiceResponseModel,
    EditVoiceRequest,
    EditVoiceRequestLabels,
    EditVoiceResponseModel,
    GetLibraryVoicesResponse,
    GetSharedCategory,
    GetSharedSort,
    GetVoicesResponse,
    GetVoicesV2Response,
    HttpValidationError,
    ListSimilarVoicesRequest,
    Voice,
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
    from .pvc.client import PvcClient as _PvcClient, AsyncPvcClient as _AsyncPvcClient
    from .samples.client import (
        SamplesClient as _SamplesClient,
        AsyncSamplesClient as _AsyncSamplesClient,
    )
    from .settings.client import (
        SettingsClient as _SettingsClient,
        AsyncSettingsClient as _AsyncSettingsClient,
    )
    from .accents.client import (
        AccentsClient as _AccentsClient,
        AsyncAccentsClient as _AsyncAccentsClient,
    )
    from .ivc.client import IvcClient as _IvcClient, AsyncIvcClient as _AsyncIvcClient


class VoicesClient(BaseService):
    """
    Fern-style resource client for VoicesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._pvc: Any = None
        self._samples: Any = None
        self._settings: Any = None
        self._accents: Any = None
        self._ivc: Any = None
        self._get_all_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._search_config: SdkConfig = {}
        self._share_config: SdkConfig = {}
        self._get_shared_config: SdkConfig = {}
        self._find_similar_voices_config: SdkConfig = {}

    @property
    def pvc(self) -> "_PvcClient":
        """Lazily construct and return the pvc sub-resource client."""
        if self._pvc is None:
            from .pvc.client import PvcClient

            _child = PvcClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._pvc = _child
        return self._pvc

    @property
    def samples(self) -> "_SamplesClient":
        """Lazily construct and return the samples sub-resource client."""
        if self._samples is None:
            from .samples.client import SamplesClient

            _child = SamplesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._samples = _child
        return self._samples

    @property
    def settings(self) -> "_SettingsClient":
        """Lazily construct and return the settings sub-resource client."""
        if self._settings is None:
            from .settings.client import SettingsClient

            _child = SettingsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._settings = _child
        return self._settings

    @property
    def accents(self) -> "_AccentsClient":
        """Lazily construct and return the accents sub-resource client."""
        if self._accents is None:
            from .accents.client import AccentsClient

            _child = AccentsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._accents = _child
        return self._accents

    @property
    def ivc(self) -> "_IvcClient":
        """Lazily construct and return the ivc sub-resource client."""
        if self._ivc is None:
            from .ivc.client import IvcClient

            _child = IvcClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._ivc = _child
        return self._ivc

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
        if self._pvc is not None:
            self._pvc.set_base_url(base_url)
        if self._samples is not None:
            self._samples.set_base_url(base_url)
        if self._settings is not None:
            self._settings.set_base_url(base_url)
        if self._accents is not None:
            self._accents.set_base_url(base_url)
        if self._ivc is not None:
            self._ivc.set_base_url(base_url)

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
        if self._pvc is not None:
            self._pvc.set_config(config)
        if self._samples is not None:
            self._samples.set_config(config)
        if self._settings is not None:
            self._settings.set_config(config)
        if self._accents is not None:
            self._accents.set_config(config)
        if self._ivc is not None:
            self._ivc.set_config(config)

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
        if self._pvc is not None:
            self._pvc.set_timeout(timeout)
        if self._samples is not None:
            self._samples.set_timeout(timeout)
        if self._settings is not None:
            self._settings.set_timeout(timeout)
        if self._accents is not None:
            self._accents.set_timeout(timeout)
        if self._ivc is not None:
            self._ivc.set_timeout(timeout)

        return self

    def set_get_all_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_all.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_all_config = config
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

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_search_config(self, config: SdkConfig):
        """
        Sets method-level configuration for search.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._search_config = config
        return self

    def set_share_config(self, config: SdkConfig):
        """
        Sets method-level configuration for share.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._share_config = config
        return self

    def set_get_shared_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_shared.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_shared_config = config
        return self

    def set_find_similar_voices_config(self, config: SdkConfig):
        """
        Sets method-level configuration for find_similar_voices.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._find_similar_voices_config = config
        return self

    @property
    def with_raw_response(self) -> "RawVoicesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawVoicesClient(self)

    @cast_models
    def get_all(
        self,
        *,
        show_legacy: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetVoicesResponse:
        """
        Returns a list of all available voices for a user. Stops working once the user's workspace exceeds 500 voices.

        Parameters
        ----------
        show_legacy : typing.Optional[bool]
            If set to true, legacy premade voices will be included in responses from /v1/voices

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoicesResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.get_all(
            show_legacy=False,
        )
        """

        Validator(bool).is_optional().is_nullable().validate(show_legacy, "show_legacy")

        resolved_config = self._get_resolved_config(
            self._get_all_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("show_legacy", show_legacy, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetVoicesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetVoicesResponse, response)
            )
        )

    @cast_models
    def get(
        self,
        voice_id: str,
        *,
        with_settings: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Voice:
        """
        Returns metadata about a specific voice.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        with_settings : typing.Optional[bool]
            This parameter is now deprecated. It is ignored and will be removed in a future version.

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
        client.voices.get(
            voice_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(bool).is_optional().is_nullable().validate(
            with_settings, "with_settings"
        )

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/{{voice_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_query("with_settings", with_settings, nullable=True)
            .serialize()
            .set_method("GET")
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
    def delete(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DeleteVoiceResponseModel:
        """
        Deletes a voice by its ID.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteVoiceResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.delete(
            voice_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/{{voice_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteVoiceResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteVoiceResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        voice_id: str,
        *,
        name: str,
        files: Optional[List[bytes]] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[EditVoiceRequestLabels, None] = SENTINEL,
        moderate_metadata: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> EditVoiceResponseModel:
        """
        Edit a voice created by you.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        name : str
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        files : typing.Optional[typing.Sequence[core.File]]
            Audio files to add to the voice

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        description : typing.Optional[str]
            A description of the voice.

        labels : typing.Optional[EditVoiceRequestLabels]
            Labels for the voice. Keys can be language, accent, gender, or age.

        moderate_metadata : typing.Optional[bool]
            Run synchronous LLM moderation over the voice name and description when they change. Has no effect unless the voice_library_metadata_moderation feature flag is enabled for the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditVoiceResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.update(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            name="John Smith",
            files=[
                "files"
            ],
            remove_background_noise=True,
            description="description",
            labels={},
            moderate_metadata=False,
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = EditVoiceRequest(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "files": files,
                        "remove_background_noise": remove_background_noise,
                        "description": description,
                        "labels": labels,
                        "moderate_metadata": moderate_metadata,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(EditVoiceRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/{{voice_id}}/edit",
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
            None
            if response in (b"", "")
            else (
                EditVoiceResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EditVoiceResponseModel, response)
            )
        )

    @cast_models
    def search(
        self,
        *,
        next_page_token: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        sort: Union[str, None] = SENTINEL,
        sort_direction: Union[str, None] = SENTINEL,
        voice_type: Union[str, None] = SENTINEL,
        category: Union[str, None] = SENTINEL,
        fine_tuning_state: Union[str, None] = SENTINEL,
        collection_id: Union[str, None] = SENTINEL,
        include_total_count: Union[bool, None] = SENTINEL,
        voice_ids: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetVoicesV2Response:
        """
        Gets a list of all available voices for a user with search, filtering and pagination.

        Parameters
        ----------
        next_page_token : typing.Optional[str]
            The next page token to use for pagination. Returned from the previous request. Use this in combination with the has_more flag for reliable pagination.

        page_size : typing.Optional[int]
            How many voices to return at maximum. Can not exceed 100, defaults to 10. Page 0 may include more voices due to default voices being included.

        search : typing.Optional[str]
            Search term to filter voices by. Searches in name, description, labels, category.

        sort : typing.Optional[str]
            Which field to sort by, one of 'created_at_unix' or 'name'. 'created_at_unix' may not be available for older voices.

        sort_direction : typing.Optional[str]
            Which direction to sort the voices in. 'asc' or 'desc'.

        voice_type : typing.Optional[str]
            Type of the voice to filter by. One of 'personal', 'community', 'default', 'workspace', 'non-default', 'non-community', 'saved'. 'non-default' is equal to all but 'default'. 'non-community' is equal to 'personal' and 'workspace' combined (excludes library copies). 'saved' is equal to non-default, but includes default voices if they have been added to a collection.

        category : typing.Optional[str]
            Category of the voice to filter by. One of 'premade', 'cloned', 'generated', 'professional'

        fine_tuning_state : typing.Optional[str]
            State of the voice's fine tuning to filter by. Applicable only to professional voices clones. One of 'draft', 'not_verified', 'not_started', 'queued', 'fine_tuning', 'fine_tuned', 'failed', 'delayed'

        collection_id : typing.Optional[str]
            Collection ID to filter voices by.

        include_total_count : typing.Optional[bool]
            Whether to include the total count of voices found in the response. NOTE: The total_count value is a live snapshot and may change between requests as users create, modify, or delete voices. For pagination, rely on the has_more flag instead. Only enable this when you actually need the total count (e.g., for display purposes), as it incurs a performance cost.

        voice_ids : typing.Optional[typing.Sequence[str]]
            Voice IDs to lookup by. Maximum 100 voice IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoicesV2Response
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.search(
            next_page_token="next_page_token",
            page_size=10,
            search="search",
            sort="sort",
            sort_direction="sort_direction",
            voice_type="voice_type",
            category="category",
            fine_tuning_state="fine_tuning_state",
            collection_id="collection_id",
            include_total_count=True,
            voice_ids=[
                "voice_ids"
            ],
        )
        """

        Validator(str).is_optional().is_nullable().validate(
            next_page_token, "next_page_token"
        )
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(str).is_optional().is_nullable().validate(sort, "sort")
        Validator(str).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )
        Validator(str).is_optional().is_nullable().validate(voice_type, "voice_type")
        Validator(str).is_optional().is_nullable().validate(category, "category")
        Validator(str).is_optional().is_nullable().validate(
            fine_tuning_state, "fine_tuning_state"
        )
        Validator(str).is_optional().is_nullable().validate(
            collection_id, "collection_id"
        )
        Validator(bool).is_optional().is_nullable().validate(
            include_total_count, "include_total_count"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            voice_ids, "voice_ids"
        )

        resolved_config = self._get_resolved_config(
            self._search_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v2/voices",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("next_page_token", next_page_token, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query("sort", sort, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .add_query("voice_type", voice_type, nullable=True)
            .add_query("category", category, nullable=True)
            .add_query("fine_tuning_state", fine_tuning_state, nullable=True)
            .add_query("collection_id", collection_id, nullable=True)
            .add_query("include_total_count", include_total_count, nullable=True)
            .add_query("voice_ids", voice_ids, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetVoicesV2Response.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetVoicesV2Response, response)
            )
        )

    @cast_models
    def share(
        self,
        public_user_id: str,
        voice_id: str,
        *,
        new_name: str,
        bookmarked: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddVoiceResponseModel:
        """
        Add a shared voice to your collection of Voices

        Parameters
        ----------
        public_user_id : str
            Public user ID used to publicly identify ElevenLabs users.

        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        new_name : str
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        bookmarked : typing.Optional[bool]

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
        client.voices.share(
            public_user_id="63e06b7e7cafdc46be4d2e0b3f045940231ae058d508589653d74d1265a574ca",
            voice_id="21m00Tcm4TlvDq8ikWAM",
            new_name="John Smith",
            bookmarked=True,
        )
        """

        Validator(str).validate(public_user_id, "public_user_id")
        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(self._share_config, request_options)

        request_body = BodyAddSharedVoiceV1VoicesAddPublicUserIdVoiceIdPost(
            new_name=new_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"bookmarked": bookmarked}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyAddSharedVoiceV1VoicesAddPublicUserIdVoiceIdPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/add/{{public_user_id}}/{{voice_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("public_user_id", public_user_id)
            .add_path("voice_id", voice_id)
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
    def get_shared(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        category: Union[GetSharedCategory, None] = SENTINEL,
        gender: Union[str, None] = SENTINEL,
        age: Union[str, None] = SENTINEL,
        accent: Union[str, None] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        locale: Union[str, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        use_cases: Union[List[str], None] = SENTINEL,
        descriptives: Union[List[str], None] = SENTINEL,
        featured: Union[bool, None] = SENTINEL,
        min_notice_period_days: Union[int, None] = SENTINEL,
        include_custom_rates: Union[bool, None] = SENTINEL,
        include_live_moderated: Union[bool, None] = SENTINEL,
        reader_app_enabled: Union[bool, None] = SENTINEL,
        owner_id: Union[str, None] = SENTINEL,
        sort: Union[GetSharedSort, None] = SENTINEL,
        page: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetLibraryVoicesResponse:
        """
        Retrieves a list of shared voices.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many shared voices to return at maximum. Can not exceed 100, defaults to 30.

        category : typing.Optional[GetSharedCategory]
            Voice category used for filtering

        gender : typing.Optional[str]
            Gender used for filtering

        age : typing.Optional[str]
            Age used for filtering

        accent : typing.Optional[str]
            Accent used for filtering

        language : typing.Optional[str]
            Language used for filtering

        locale : typing.Optional[str]
            Locale used for filtering

        search : typing.Optional[str]
            Search term used for filtering

        use_cases : typing.Optional[typing.Sequence[str]]
            Use-case used for filtering

        descriptives : typing.Optional[typing.Sequence[str]]
            Search term used for filtering

        featured : typing.Optional[bool]
            Filter featured voices

        min_notice_period_days : typing.Optional[int]
            Filter voices with a minimum notice period of the given number of days.

        include_custom_rates : typing.Optional[bool]
            Include/exclude voices with custom rates

        include_live_moderated : typing.Optional[bool]
            Include/exclude voices that are live moderated

        reader_app_enabled : typing.Optional[bool]
            Filter voices that are enabled for the reader app

        owner_id : typing.Optional[str]
            Filter voices by public owner ID

        sort : typing.Optional[GetSharedSort]
            Sort criteria. Must be one of: created_date, usage_character_count_1y, trending, cloned_by_count.

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibraryVoicesResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import GetSharedCategory, GetSharedSort

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.get_shared(
            page_size=30,
            category="professional",
            gender="gender",
            age="age",
            accent="accent",
            language="language",
            locale="locale",
            search="search",
            use_cases=[
                "use_cases"
            ],
            descriptives=[
                "descriptives"
            ],
            featured=True,
            min_notice_period_days=4,
            include_custom_rates=True,
            include_live_moderated=True,
            reader_app_enabled=True,
            owner_id="owner_id",
            sort="created_date",
            page=0,
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(GetSharedCategory).is_optional().is_nullable().validate(
            category, "category"
        )
        Validator(str).is_optional().is_nullable().validate(gender, "gender")
        Validator(str).is_optional().is_nullable().validate(age, "age")
        Validator(str).is_optional().is_nullable().validate(accent, "accent")
        Validator(str).is_optional().is_nullable().validate(language, "language")
        Validator(str).is_optional().is_nullable().validate(locale, "locale")
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(str).is_array().is_optional().is_nullable().validate(
            use_cases, "use_cases"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            descriptives, "descriptives"
        )
        Validator(bool).is_optional().is_nullable().validate(featured, "featured")
        Validator(int).is_optional().is_nullable().validate(
            min_notice_period_days, "min_notice_period_days"
        )
        Validator(bool).is_optional().is_nullable().validate(
            include_custom_rates, "include_custom_rates"
        )
        Validator(bool).is_optional().is_nullable().validate(
            include_live_moderated, "include_live_moderated"
        )
        Validator(bool).is_optional().is_nullable().validate(
            reader_app_enabled, "reader_app_enabled"
        )
        Validator(str).is_optional().is_nullable().validate(owner_id, "owner_id")
        Validator(GetSharedSort).is_optional().is_nullable().validate(sort, "sort")
        Validator(int).is_optional().is_nullable().validate(page, "page")

        resolved_config = self._get_resolved_config(
            self._get_shared_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/shared-voices",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("page_size", page_size, nullable=True)
            .add_query("category", category, nullable=True)
            .add_query("gender", gender, nullable=True)
            .add_query("age", age, nullable=True)
            .add_query("accent", accent, nullable=True)
            .add_query("language", language, nullable=True)
            .add_query("locale", locale, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query("use_cases", use_cases, nullable=True)
            .add_query("descriptives", descriptives, nullable=True)
            .add_query("featured", featured, nullable=True)
            .add_query("min_notice_period_days", min_notice_period_days, nullable=True)
            .add_query("include_custom_rates", include_custom_rates, nullable=True)
            .add_query("include_live_moderated", include_live_moderated, nullable=True)
            .add_query("reader_app_enabled", reader_app_enabled, nullable=True)
            .add_query("owner_id", owner_id, nullable=True)
            .add_query("sort", sort, nullable=True)
            .add_query("page", page, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetLibraryVoicesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetLibraryVoicesResponse, response)
            )
        )

    @cast_models
    def find_similar_voices(
        self,
        *,
        audio_file: Optional[bytes] = SENTINEL,
        similarity_threshold: Union[float, None] = SENTINEL,
        top_k: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetLibraryVoicesResponse:
        """
        Returns a list of shared voices similar to the provided audio sample. If neither similarity_threshold nor top_k is provided, we will apply default values.

        Parameters
        ----------
        audio_file : typing.Optional[core.File]

        similarity_threshold : typing.Optional[float]
            Threshold for voice similarity between provided sample and library voices. Values range from 0 to 2. The smaller the value the more similar voices will be returned.

        top_k : typing.Optional[int]
            Number of most similar voices to return. If similarity_threshold is provided, less than this number of voices may be returned. Values range from 1 to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibraryVoicesResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.find_similar_voices(
            audio_file="audio_file",
            similarity_threshold=8.7,
            top_k=3,
        )
        """

        resolved_config = self._get_resolved_config(
            self._find_similar_voices_config, request_options
        )

        request_body = ListSimilarVoicesRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "audio_file": audio_file,
                        "similarity_threshold": similarity_threshold,
                        "top_k": top_k,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(ListSimilarVoicesRequest).is_optional().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/similar-voices",
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
                GetLibraryVoicesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetLibraryVoicesResponse, response)
            )
        )


class RawVoicesClient:
    """
    Raw-response client for VoicesClient.

    Each method delegates to the matching :class:`VoicesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: VoicesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get_all(
        self,
        *,
        show_legacy: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetVoicesResponse]:
        data = VoicesClient.get_all(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"show_legacy": show_legacy}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        voice_id: str,
        *,
        with_settings: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Voice]:
        data = VoicesClient.get(
            self._client,
            voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"with_settings": with_settings}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteVoiceResponseModel]:
        data = VoicesClient.delete(
            self._client, voice_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        voice_id: str,
        *,
        name: str,
        files: Optional[List[bytes]] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[EditVoiceRequestLabels, None] = SENTINEL,
        moderate_metadata: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditVoiceResponseModel]:
        data = VoicesClient.update(
            self._client,
            voice_id,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "files": files,
                        "remove_background_noise": remove_background_noise,
                        "description": description,
                        "labels": labels,
                        "moderate_metadata": moderate_metadata,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def search(
        self,
        *,
        next_page_token: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        sort: Union[str, None] = SENTINEL,
        sort_direction: Union[str, None] = SENTINEL,
        voice_type: Union[str, None] = SENTINEL,
        category: Union[str, None] = SENTINEL,
        fine_tuning_state: Union[str, None] = SENTINEL,
        collection_id: Union[str, None] = SENTINEL,
        include_total_count: Union[bool, None] = SENTINEL,
        voice_ids: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetVoicesV2Response]:
        data = VoicesClient.search(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "next_page_token": next_page_token,
                        "page_size": page_size,
                        "search": search,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "voice_type": voice_type,
                        "category": category,
                        "fine_tuning_state": fine_tuning_state,
                        "collection_id": collection_id,
                        "include_total_count": include_total_count,
                        "voice_ids": voice_ids,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def share(
        self,
        public_user_id: str,
        voice_id: str,
        *,
        new_name: str,
        bookmarked: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceResponseModel]:
        data = VoicesClient.share(
            self._client,
            public_user_id,
            voice_id,
            new_name=new_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"bookmarked": bookmarked}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_shared(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        category: Union[GetSharedCategory, None] = SENTINEL,
        gender: Union[str, None] = SENTINEL,
        age: Union[str, None] = SENTINEL,
        accent: Union[str, None] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        locale: Union[str, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        use_cases: Union[List[str], None] = SENTINEL,
        descriptives: Union[List[str], None] = SENTINEL,
        featured: Union[bool, None] = SENTINEL,
        min_notice_period_days: Union[int, None] = SENTINEL,
        include_custom_rates: Union[bool, None] = SENTINEL,
        include_live_moderated: Union[bool, None] = SENTINEL,
        reader_app_enabled: Union[bool, None] = SENTINEL,
        owner_id: Union[str, None] = SENTINEL,
        sort: Union[GetSharedSort, None] = SENTINEL,
        page: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLibraryVoicesResponse]:
        data = VoicesClient.get_shared(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "category": category,
                        "gender": gender,
                        "age": age,
                        "accent": accent,
                        "language": language,
                        "locale": locale,
                        "search": search,
                        "use_cases": use_cases,
                        "descriptives": descriptives,
                        "featured": featured,
                        "min_notice_period_days": min_notice_period_days,
                        "include_custom_rates": include_custom_rates,
                        "include_live_moderated": include_live_moderated,
                        "reader_app_enabled": reader_app_enabled,
                        "owner_id": owner_id,
                        "sort": sort,
                        "page": page,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def find_similar_voices(
        self,
        *,
        audio_file: Optional[bytes] = SENTINEL,
        similarity_threshold: Union[float, None] = SENTINEL,
        top_k: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLibraryVoicesResponse]:
        data = VoicesClient.find_similar_voices(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "audio_file": audio_file,
                        "similarity_threshold": similarity_threshold,
                        "top_k": top_k,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncVoicesClient(VoicesClient):
    """
    Async wrapper for VoicesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def pvc(self) -> "_AsyncPvcClient":
        """Lazily construct and return the async pvc sub-resource client."""
        if self._pvc is None:
            from .pvc.client import AsyncPvcClient

            _child = AsyncPvcClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._pvc = _child
        return self._pvc

    @property
    def samples(self) -> "_AsyncSamplesClient":
        """Lazily construct and return the async samples sub-resource client."""
        if self._samples is None:
            from .samples.client import AsyncSamplesClient

            _child = AsyncSamplesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._samples = _child
        return self._samples

    @property
    def settings(self) -> "_AsyncSettingsClient":
        """Lazily construct and return the async settings sub-resource client."""
        if self._settings is None:
            from .settings.client import AsyncSettingsClient

            _child = AsyncSettingsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._settings = _child
        return self._settings

    @property
    def accents(self) -> "_AsyncAccentsClient":
        """Lazily construct and return the async accents sub-resource client."""
        if self._accents is None:
            from .accents.client import AsyncAccentsClient

            _child = AsyncAccentsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._accents = _child
        return self._accents

    @property
    def ivc(self) -> "_AsyncIvcClient":
        """Lazily construct and return the async ivc sub-resource client."""
        if self._ivc is None:
            from .ivc.client import AsyncIvcClient

            _child = AsyncIvcClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._ivc = _child
        return self._ivc

    @property
    def with_raw_response(self) -> "AsyncRawVoicesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawVoicesClient(self)

    def get_all(
        self,
        *,
        show_legacy: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetVoicesResponse]:  # type: ignore[override]
        """
        Returns a list of all available voices for a user. Stops working once the user's workspace exceeds 500 voices.

        Parameters
        ----------
        show_legacy : typing.Optional[bool]
            If set to true, legacy premade voices will be included in responses from /v1/voices

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoicesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.get_all(
                show_legacy=False,
            )


        asyncio.run(main())
        """
        return to_async(super().get_all)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"show_legacy": show_legacy}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        voice_id: str,
        *,
        with_settings: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Voice]:  # type: ignore[override]
        """
        Returns metadata about a specific voice.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        with_settings : typing.Optional[bool]
            This parameter is now deprecated. It is ignored and will be removed in a future version.

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
            await client.voices.get(
                voice_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"with_settings": with_settings}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DeleteVoiceResponseModel]:  # type: ignore[override]
        """
        Deletes a voice by its ID.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteVoiceResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.delete(
                voice_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(voice_id, request_options=request_options)

    def update(
        self,
        voice_id: str,
        *,
        name: str,
        files: Optional[List[bytes]] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[EditVoiceRequestLabels, None] = SENTINEL,
        moderate_metadata: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EditVoiceResponseModel]:  # type: ignore[override]
        """
        Edit a voice created by you.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        name : str
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        files : typing.Optional[typing.Sequence[core.File]]
            Audio files to add to the voice

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        description : typing.Optional[str]
            A description of the voice.

        labels : typing.Optional[EditVoiceRequestLabels]
            Labels for the voice. Keys can be language, accent, gender, or age.

        moderate_metadata : typing.Optional[bool]
            Run synchronous LLM moderation over the voice name and description when they change. Has no effect unless the voice_library_metadata_moderation feature flag is enabled for the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditVoiceResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.update(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                name="John Smith",
                files=[
                    "files"
                ],
                remove_background_noise=True,
                description="description",
                labels={},
                moderate_metadata=False,
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            voice_id,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "files": files,
                        "remove_background_noise": remove_background_noise,
                        "description": description,
                        "labels": labels,
                        "moderate_metadata": moderate_metadata,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def search(
        self,
        *,
        next_page_token: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        sort: Union[str, None] = SENTINEL,
        sort_direction: Union[str, None] = SENTINEL,
        voice_type: Union[str, None] = SENTINEL,
        category: Union[str, None] = SENTINEL,
        fine_tuning_state: Union[str, None] = SENTINEL,
        collection_id: Union[str, None] = SENTINEL,
        include_total_count: Union[bool, None] = SENTINEL,
        voice_ids: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetVoicesV2Response]:  # type: ignore[override]
        """
        Gets a list of all available voices for a user with search, filtering and pagination.

        Parameters
        ----------
        next_page_token : typing.Optional[str]
            The next page token to use for pagination. Returned from the previous request. Use this in combination with the has_more flag for reliable pagination.

        page_size : typing.Optional[int]
            How many voices to return at maximum. Can not exceed 100, defaults to 10. Page 0 may include more voices due to default voices being included.

        search : typing.Optional[str]
            Search term to filter voices by. Searches in name, description, labels, category.

        sort : typing.Optional[str]
            Which field to sort by, one of 'created_at_unix' or 'name'. 'created_at_unix' may not be available for older voices.

        sort_direction : typing.Optional[str]
            Which direction to sort the voices in. 'asc' or 'desc'.

        voice_type : typing.Optional[str]
            Type of the voice to filter by. One of 'personal', 'community', 'default', 'workspace', 'non-default', 'non-community', 'saved'. 'non-default' is equal to all but 'default'. 'non-community' is equal to 'personal' and 'workspace' combined (excludes library copies). 'saved' is equal to non-default, but includes default voices if they have been added to a collection.

        category : typing.Optional[str]
            Category of the voice to filter by. One of 'premade', 'cloned', 'generated', 'professional'

        fine_tuning_state : typing.Optional[str]
            State of the voice's fine tuning to filter by. Applicable only to professional voices clones. One of 'draft', 'not_verified', 'not_started', 'queued', 'fine_tuning', 'fine_tuned', 'failed', 'delayed'

        collection_id : typing.Optional[str]
            Collection ID to filter voices by.

        include_total_count : typing.Optional[bool]
            Whether to include the total count of voices found in the response. NOTE: The total_count value is a live snapshot and may change between requests as users create, modify, or delete voices. For pagination, rely on the has_more flag instead. Only enable this when you actually need the total count (e.g., for display purposes), as it incurs a performance cost.

        voice_ids : typing.Optional[typing.Sequence[str]]
            Voice IDs to lookup by. Maximum 100 voice IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoicesV2Response
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.search(
                next_page_token="next_page_token",
                page_size=10,
                search="search",
                sort="sort",
                sort_direction="sort_direction",
                voice_type="voice_type",
                category="category",
                fine_tuning_state="fine_tuning_state",
                collection_id="collection_id",
                include_total_count=True,
                voice_ids=[
                    "voice_ids"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().search)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "next_page_token": next_page_token,
                        "page_size": page_size,
                        "search": search,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "voice_type": voice_type,
                        "category": category,
                        "fine_tuning_state": fine_tuning_state,
                        "collection_id": collection_id,
                        "include_total_count": include_total_count,
                        "voice_ids": voice_ids,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def share(
        self,
        public_user_id: str,
        voice_id: str,
        *,
        new_name: str,
        bookmarked: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddVoiceResponseModel]:  # type: ignore[override]
        """
        Add a shared voice to your collection of Voices

        Parameters
        ----------
        public_user_id : str
            Public user ID used to publicly identify ElevenLabs users.

        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        new_name : str
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        bookmarked : typing.Optional[bool]

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
            await client.voices.share(
                public_user_id="63e06b7e7cafdc46be4d2e0b3f045940231ae058d508589653d74d1265a574ca",
                voice_id="21m00Tcm4TlvDq8ikWAM",
                new_name="John Smith",
                bookmarked=True,
            )


        asyncio.run(main())
        """
        return to_async(super().share)(
            public_user_id,
            voice_id,
            new_name=new_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"bookmarked": bookmarked}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get_shared(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        category: Union[GetSharedCategory, None] = SENTINEL,
        gender: Union[str, None] = SENTINEL,
        age: Union[str, None] = SENTINEL,
        accent: Union[str, None] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        locale: Union[str, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        use_cases: Union[List[str], None] = SENTINEL,
        descriptives: Union[List[str], None] = SENTINEL,
        featured: Union[bool, None] = SENTINEL,
        min_notice_period_days: Union[int, None] = SENTINEL,
        include_custom_rates: Union[bool, None] = SENTINEL,
        include_live_moderated: Union[bool, None] = SENTINEL,
        reader_app_enabled: Union[bool, None] = SENTINEL,
        owner_id: Union[str, None] = SENTINEL,
        sort: Union[GetSharedSort, None] = SENTINEL,
        page: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetLibraryVoicesResponse]:  # type: ignore[override]
        """
        Retrieves a list of shared voices.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many shared voices to return at maximum. Can not exceed 100, defaults to 30.

        category : typing.Optional[GetSharedCategory]
            Voice category used for filtering

        gender : typing.Optional[str]
            Gender used for filtering

        age : typing.Optional[str]
            Age used for filtering

        accent : typing.Optional[str]
            Accent used for filtering

        language : typing.Optional[str]
            Language used for filtering

        locale : typing.Optional[str]
            Locale used for filtering

        search : typing.Optional[str]
            Search term used for filtering

        use_cases : typing.Optional[typing.Sequence[str]]
            Use-case used for filtering

        descriptives : typing.Optional[typing.Sequence[str]]
            Search term used for filtering

        featured : typing.Optional[bool]
            Filter featured voices

        min_notice_period_days : typing.Optional[int]
            Filter voices with a minimum notice period of the given number of days.

        include_custom_rates : typing.Optional[bool]
            Include/exclude voices with custom rates

        include_live_moderated : typing.Optional[bool]
            Include/exclude voices that are live moderated

        reader_app_enabled : typing.Optional[bool]
            Filter voices that are enabled for the reader app

        owner_id : typing.Optional[str]
            Filter voices by public owner ID

        sort : typing.Optional[GetSharedSort]
            Sort criteria. Must be one of: created_date, usage_character_count_1y, trending, cloned_by_count.

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibraryVoicesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import GetSharedCategory, GetSharedSort

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.get_shared(
                page_size=30,
                category="professional",
                gender="gender",
                age="age",
                accent="accent",
                language="language",
                locale="locale",
                search="search",
                use_cases=[
                    "use_cases"
                ],
                descriptives=[
                    "descriptives"
                ],
                featured=True,
                min_notice_period_days=4,
                include_custom_rates=True,
                include_live_moderated=True,
                reader_app_enabled=True,
                owner_id="owner_id",
                sort="created_date",
                page=0,
            )


        asyncio.run(main())
        """
        return to_async(super().get_shared)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "category": category,
                        "gender": gender,
                        "age": age,
                        "accent": accent,
                        "language": language,
                        "locale": locale,
                        "search": search,
                        "use_cases": use_cases,
                        "descriptives": descriptives,
                        "featured": featured,
                        "min_notice_period_days": min_notice_period_days,
                        "include_custom_rates": include_custom_rates,
                        "include_live_moderated": include_live_moderated,
                        "reader_app_enabled": reader_app_enabled,
                        "owner_id": owner_id,
                        "sort": sort,
                        "page": page,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def find_similar_voices(
        self,
        *,
        audio_file: Optional[bytes] = SENTINEL,
        similarity_threshold: Union[float, None] = SENTINEL,
        top_k: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetLibraryVoicesResponse]:  # type: ignore[override]
        """
        Returns a list of shared voices similar to the provided audio sample. If neither similarity_threshold nor top_k is provided, we will apply default values.

        Parameters
        ----------
        audio_file : typing.Optional[core.File]

        similarity_threshold : typing.Optional[float]
            Threshold for voice similarity between provided sample and library voices. Values range from 0 to 2. The smaller the value the more similar voices will be returned.

        top_k : typing.Optional[int]
            Number of most similar voices to return. If similarity_threshold is provided, less than this number of voices may be returned. Values range from 1 to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibraryVoicesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.find_similar_voices(
                audio_file="audio_file",
                similarity_threshold=8.7,
                top_k=3,
            )


        asyncio.run(main())
        """
        return to_async(super().find_similar_voices)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "audio_file": audio_file,
                        "similarity_threshold": similarity_threshold,
                        "top_k": top_k,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawVoicesClient:
    """
    Async raw-response client for AsyncVoicesClient.
    """

    def __init__(self, client: AsyncVoicesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get_all(
        self,
        *,
        show_legacy: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetVoicesResponse]:
        data = await AsyncVoicesClient.get_all(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"show_legacy": show_legacy}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        voice_id: str,
        *,
        with_settings: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Voice]:
        data = await AsyncVoicesClient.get(
            self._client,
            voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"with_settings": with_settings}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteVoiceResponseModel]:
        data = await AsyncVoicesClient.delete(
            self._client, voice_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        voice_id: str,
        *,
        name: str,
        files: Optional[List[bytes]] = SENTINEL,
        remove_background_noise: Optional[bool] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[EditVoiceRequestLabels, None] = SENTINEL,
        moderate_metadata: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditVoiceResponseModel]:
        data = await AsyncVoicesClient.update(
            self._client,
            voice_id,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "files": files,
                        "remove_background_noise": remove_background_noise,
                        "description": description,
                        "labels": labels,
                        "moderate_metadata": moderate_metadata,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def search(
        self,
        *,
        next_page_token: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        sort: Union[str, None] = SENTINEL,
        sort_direction: Union[str, None] = SENTINEL,
        voice_type: Union[str, None] = SENTINEL,
        category: Union[str, None] = SENTINEL,
        fine_tuning_state: Union[str, None] = SENTINEL,
        collection_id: Union[str, None] = SENTINEL,
        include_total_count: Union[bool, None] = SENTINEL,
        voice_ids: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetVoicesV2Response]:
        data = await AsyncVoicesClient.search(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "next_page_token": next_page_token,
                        "page_size": page_size,
                        "search": search,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "voice_type": voice_type,
                        "category": category,
                        "fine_tuning_state": fine_tuning_state,
                        "collection_id": collection_id,
                        "include_total_count": include_total_count,
                        "voice_ids": voice_ids,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def share(
        self,
        public_user_id: str,
        voice_id: str,
        *,
        new_name: str,
        bookmarked: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceResponseModel]:
        data = await AsyncVoicesClient.share(
            self._client,
            public_user_id,
            voice_id,
            new_name=new_name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"bookmarked": bookmarked}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_shared(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        category: Union[GetSharedCategory, None] = SENTINEL,
        gender: Union[str, None] = SENTINEL,
        age: Union[str, None] = SENTINEL,
        accent: Union[str, None] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        locale: Union[str, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        use_cases: Union[List[str], None] = SENTINEL,
        descriptives: Union[List[str], None] = SENTINEL,
        featured: Union[bool, None] = SENTINEL,
        min_notice_period_days: Union[int, None] = SENTINEL,
        include_custom_rates: Union[bool, None] = SENTINEL,
        include_live_moderated: Union[bool, None] = SENTINEL,
        reader_app_enabled: Union[bool, None] = SENTINEL,
        owner_id: Union[str, None] = SENTINEL,
        sort: Union[GetSharedSort, None] = SENTINEL,
        page: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLibraryVoicesResponse]:
        data = await AsyncVoicesClient.get_shared(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "category": category,
                        "gender": gender,
                        "age": age,
                        "accent": accent,
                        "language": language,
                        "locale": locale,
                        "search": search,
                        "use_cases": use_cases,
                        "descriptives": descriptives,
                        "featured": featured,
                        "min_notice_period_days": min_notice_period_days,
                        "include_custom_rates": include_custom_rates,
                        "include_live_moderated": include_live_moderated,
                        "reader_app_enabled": reader_app_enabled,
                        "owner_id": owner_id,
                        "sort": sort,
                        "page": page,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def find_similar_voices(
        self,
        *,
        audio_file: Optional[bytes] = SENTINEL,
        similarity_threshold: Union[float, None] = SENTINEL,
        top_k: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLibraryVoicesResponse]:
        data = await AsyncVoicesClient.find_similar_voices(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "audio_file": audio_file,
                        "similarity_threshold": similarity_threshold,
                        "top_k": top_k,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
