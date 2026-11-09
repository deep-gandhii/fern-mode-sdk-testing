from typing import Any, Optional, Generator, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AddPronunciationDictionaryRequest,
    AddPronunciationDictionaryRequestWorkspaceAccess,
    AddPronunciationDictionaryResponseModel,
    BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPost,
    BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem,
    BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess,
    BodyUpdatePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdPatch,
    GetPronunciationDictionariesMetadataResponseModel,
    GetPronunciationDictionaryMetadataResponse,
    GetPronunciationDictionaryWithRulesResponseModel,
    HttpValidationError,
    Sort,
)
from ..net.transport.serializer import Serializer
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
    from .rules.client import (
        RulesClient as _RulesClient,
        AsyncRulesClient as _AsyncRulesClient,
    )


class PronunciationDictionariesClient(BaseService):
    """
    Fern-style resource client for PronunciationDictionariesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._rules: Any = None
        self._create_from_file_config: SdkConfig = {}
        self._create_from_rules_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._download_config: SdkConfig = {}
        self._list_config: SdkConfig = {}

    @property
    def rules(self) -> "_RulesClient":
        """Lazily construct and return the rules sub-resource client."""
        if self._rules is None:
            from .rules.client import RulesClient

            _child = RulesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._rules = _child
        return self._rules

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
        if self._rules is not None:
            self._rules.set_base_url(base_url)

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
        if self._rules is not None:
            self._rules.set_config(config)

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
        if self._rules is not None:
            self._rules.set_timeout(timeout)

        return self

    def set_create_from_file_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_from_file.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_from_file_config = config
        return self

    def set_create_from_rules_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_from_rules.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_from_rules_config = config
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

    def set_download_config(self, config: SdkConfig):
        """
        Sets method-level configuration for download.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._download_config = config
        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    @property
    def with_raw_response(self) -> "RawPronunciationDictionariesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawPronunciationDictionariesClient(self)

    @cast_models
    def create_from_file(
        self,
        *,
        name: str,
        file: Union[bytes, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        workspace_access: Union[
            AddPronunciationDictionaryRequestWorkspaceAccess, None
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddPronunciationDictionaryResponseModel:
        """
        Creates a new pronunciation dictionary from a lexicon .PLS file

        Parameters
        ----------
        name : str
            The name of the pronunciation dictionary, used for identification only.

        file : typing.Optional[core.File]
            A lexicon .pls file which we will use to initialize the project with.

        description : typing.Optional[str]
            A description of the pronunciation dictionary, used for identification only.

        workspace_access : typing.Optional[AddPronunciationDictionaryRequestWorkspaceAccess]
            Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddPronunciationDictionaryResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.pronunciation_dictionaries.create_from_file(
            name="My Dictionary",
            file="file",
            description="description",
            workspace_access="admin",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_from_file_config, request_options
        )

        request_body = AddPronunciationDictionaryRequest(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "description": description,
                        "workspace_access": workspace_access,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(AddPronunciationDictionaryRequest).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries/add-from-file",
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
                AddPronunciationDictionaryResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    AddPronunciationDictionaryResponseModel, response
                )
            )
        )

    @cast_models
    def create_from_rules(
        self,
        *,
        rules: List[
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
        ],
        name: str,
        description: Union[str, None] = SENTINEL,
        workspace_access: Union[
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess,
            None,
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddPronunciationDictionaryResponseModel:
        """
        Creates a new pronunciation dictionary from provided rules.

        Parameters
        ----------
        rules : typing.Sequence[BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem]
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }

        name : str
            The name of the pronunciation dictionary, used for identification only.

        description : typing.Optional[str]
            A description of the pronunciation dictionary, used for identification only.

        workspace_access : typing.Optional[BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess]
            Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddPronunciationDictionaryResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.pronunciation_dictionaries.create_from_rules(
            rules=[
                {
                    "string_to_replace": "string_to_replace",
                    "case_sensitive": True,
                    "word_boundaries": True,
                    "type": "alias",
                    "alias": "alias"
                }
            ],
            name="My Dictionary",
            description="description",
            workspace_access="admin",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_from_rules_config, request_options
        )

        request_body = (
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPost(
                rules=rules,
                name=name,
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "description": description,
                            "workspace_access": workspace_access,
                        }.items()
                        if v is not SENTINEL
                    }
                ),
            )
        )
        Validator(
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries/add-from-rules",
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
                AddPronunciationDictionaryResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    AddPronunciationDictionaryResponseModel, response
                )
            )
        )

    @cast_models
    def get(
        self,
        pronunciation_dictionary_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> GetPronunciationDictionaryWithRulesResponseModel:
        """
        Get metadata for a pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionaryWithRulesResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.pronunciation_dictionaries.get(
            pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(
            pronunciation_dictionary_id, "pronunciation_dictionary_id"
        )

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries/{{pronunciation_dictionary_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("pronunciation_dictionary_id", pronunciation_dictionary_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetPronunciationDictionaryWithRulesResponseModel.model_validate(
                    response
                )
                if should_validate_response(resolved_config)
                else construct_lenient(
                    GetPronunciationDictionaryWithRulesResponseModel, response
                )
            )
        )

    @cast_models
    def update(
        self,
        pronunciation_dictionary_id: str,
        *,
        archived: Optional[bool] = SENTINEL,
        name: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetPronunciationDictionaryMetadataResponse:
        """
        Partially update the pronunciation dictionary without changing the version

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        archived : typing.Optional[bool]
            Whether to archive the pronunciation dictionary.

        name : typing.Optional[str]
            The name of the pronunciation dictionary, used for identification only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionaryMetadataResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.pronunciation_dictionaries.update(
            pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
            archived=True,
            name="My Dictionary",
        )
        """

        Validator(str).validate(
            pronunciation_dictionary_id, "pronunciation_dictionary_id"
        )

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdatePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdPatch(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"archived": archived, "name": name}.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyUpdatePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdPatch
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries/{{pronunciation_dictionary_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("pronunciation_dictionary_id", pronunciation_dictionary_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetPronunciationDictionaryMetadataResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    GetPronunciationDictionaryMetadataResponse, response
                )
            )
        )

    @cast_models
    def download(
        self,
        dictionary_id: str,
        version_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Get a PLS file with a pronunciation dictionary version rules

        Parameters
        ----------
        dictionary_id : str
            The id of the pronunciation dictionary

        version_id : str
            The id of the pronunciation dictionary version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            The PLS file containing pronunciation dictionary rules

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.pronunciation_dictionaries.download(
            dictionary_id="21m00Tcm4TlvDq8ikWAM",
            version_id="BdF0s0aZ3oFoKnDYdTox",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(str).validate(dictionary_id, "dictionary_id")
        Validator(str).validate(version_id, "version_id")

        resolved_config = self._get_resolved_config(
            self._download_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries/{{dictionary_id}}/{{version_id}}/download",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dictionary_id", dictionary_id)
            .add_path("version_id", version_id)
            .serialize()
            .set_method("GET")
            .set_binary_download()
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        sort: Union[Sort, None] = SENTINEL,
        sort_direction: Union[str, None] = SENTINEL,
        include_archived: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetPronunciationDictionariesMetadataResponseModel:
        """
        Get a list of the pronunciation dictionaries you have access to and their metadata

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many pronunciation dictionaries to return at maximum. Can not exceed 100, defaults to 30.

        sort : typing.Optional[Sort]
            Which field to sort by, one of 'created_at_unix' or 'name'.

        sort_direction : typing.Optional[str]
            Which direction to sort the voices in. 'ascending' or 'descending'.

        include_archived : typing.Optional[bool]
            Whether to include archived pronunciation dictionaries in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionariesMetadataResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import Sort

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.pronunciation_dictionaries.list(
            cursor="cursor",
            page_size=30,
            sort="creation_time_unix",
            sort_direction="sort_direction",
            include_archived=False,
        )
        """

        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(Sort).is_optional().is_nullable().validate(sort, "sort")
        Validator(str).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )
        Validator(bool).is_optional().is_nullable().validate(
            include_archived, "include_archived"
        )

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("sort", sort, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .add_query("include_archived", include_archived, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetPronunciationDictionariesMetadataResponseModel.model_validate(
                    response
                )
                if should_validate_response(resolved_config)
                else construct_lenient(
                    GetPronunciationDictionariesMetadataResponseModel, response
                )
            )
        )


class RawPronunciationDictionariesClient:
    """
    Raw-response client for PronunciationDictionariesClient.

    Each method delegates to the matching :class:`PronunciationDictionariesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: PronunciationDictionariesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create_from_file(
        self,
        *,
        name: str,
        file: Union[bytes, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        workspace_access: Union[
            AddPronunciationDictionaryRequestWorkspaceAccess, None
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddPronunciationDictionaryResponseModel]:
        data = PronunciationDictionariesClient.create_from_file(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "description": description,
                        "workspace_access": workspace_access,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create_from_rules(
        self,
        *,
        rules: List[
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
        ],
        name: str,
        description: Union[str, None] = SENTINEL,
        workspace_access: Union[
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess,
            None,
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddPronunciationDictionaryResponseModel]:
        data = PronunciationDictionariesClient.create_from_rules(
            self._client,
            rules=rules,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "description": description,
                        "workspace_access": workspace_access,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        pronunciation_dictionary_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPronunciationDictionaryWithRulesResponseModel]:
        data = PronunciationDictionariesClient.get(
            self._client, pronunciation_dictionary_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        pronunciation_dictionary_id: str,
        *,
        archived: Optional[bool] = SENTINEL,
        name: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPronunciationDictionaryMetadataResponse]:
        data = PronunciationDictionariesClient.update(
            self._client,
            pronunciation_dictionary_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"archived": archived, "name": name}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def download(
        self,
        dictionary_id: str,
        version_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = PronunciationDictionariesClient.download(
            _call_client, dictionary_id, version_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        sort: Union[Sort, None] = SENTINEL,
        sort_direction: Union[str, None] = SENTINEL,
        include_archived: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPronunciationDictionariesMetadataResponseModel]:
        data = PronunciationDictionariesClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "include_archived": include_archived,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncPronunciationDictionariesClient(PronunciationDictionariesClient):
    """
    Async wrapper for PronunciationDictionariesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def rules(self) -> "_AsyncRulesClient":
        """Lazily construct and return the async rules sub-resource client."""
        if self._rules is None:
            from .rules.client import AsyncRulesClient

            _child = AsyncRulesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._rules = _child
        return self._rules

    @property
    def with_raw_response(self) -> "AsyncRawPronunciationDictionariesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawPronunciationDictionariesClient(self)

    def create_from_file(
        self,
        *,
        name: str,
        file: Union[bytes, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        workspace_access: Union[
            AddPronunciationDictionaryRequestWorkspaceAccess, None
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddPronunciationDictionaryResponseModel]:  # type: ignore[override]
        """
        Creates a new pronunciation dictionary from a lexicon .PLS file

        Parameters
        ----------
        name : str
            The name of the pronunciation dictionary, used for identification only.

        file : typing.Optional[core.File]
            A lexicon .pls file which we will use to initialize the project with.

        description : typing.Optional[str]
            A description of the pronunciation dictionary, used for identification only.

        workspace_access : typing.Optional[AddPronunciationDictionaryRequestWorkspaceAccess]
            Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddPronunciationDictionaryResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.pronunciation_dictionaries.create_from_file(
                name="My Dictionary",
                file="file",
                description="description",
                workspace_access="admin",
            )


        asyncio.run(main())
        """
        return to_async(super().create_from_file)(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "description": description,
                        "workspace_access": workspace_access,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create_from_rules(
        self,
        *,
        rules: List[
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
        ],
        name: str,
        description: Union[str, None] = SENTINEL,
        workspace_access: Union[
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess,
            None,
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddPronunciationDictionaryResponseModel]:  # type: ignore[override]
        """
        Creates a new pronunciation dictionary from provided rules.

        Parameters
        ----------
        rules : typing.Sequence[BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem]
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }

        name : str
            The name of the pronunciation dictionary, used for identification only.

        description : typing.Optional[str]
            A description of the pronunciation dictionary, used for identification only.

        workspace_access : typing.Optional[BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess]
            Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddPronunciationDictionaryResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.pronunciation_dictionaries.create_from_rules(
                rules=[
                    {
                        "string_to_replace": "string_to_replace",
                        "case_sensitive": True,
                        "word_boundaries": True,
                        "type": "alias",
                        "alias": "alias"
                    }
                ],
                name="My Dictionary",
                description="description",
                workspace_access="admin",
            )


        asyncio.run(main())
        """
        return to_async(super().create_from_rules)(
            rules=rules,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "description": description,
                        "workspace_access": workspace_access,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        pronunciation_dictionary_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetPronunciationDictionaryWithRulesResponseModel]:  # type: ignore[override]
        """
        Get metadata for a pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionaryWithRulesResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.pronunciation_dictionaries.get(
                pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            pronunciation_dictionary_id, request_options=request_options
        )

    def update(
        self,
        pronunciation_dictionary_id: str,
        *,
        archived: Optional[bool] = SENTINEL,
        name: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetPronunciationDictionaryMetadataResponse]:  # type: ignore[override]
        """
        Partially update the pronunciation dictionary without changing the version

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        archived : typing.Optional[bool]
            Whether to archive the pronunciation dictionary.

        name : typing.Optional[str]
            The name of the pronunciation dictionary, used for identification only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionaryMetadataResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.pronunciation_dictionaries.update(
                pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
                archived=True,
                name="My Dictionary",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            pronunciation_dictionary_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"archived": archived, "name": name}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def download(
        self,
        dictionary_id: str,
        version_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Get a PLS file with a pronunciation dictionary version rules

        Parameters
        ----------
        dictionary_id : str
            The id of the pronunciation dictionary

        version_id : str
            The id of the pronunciation dictionary version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The PLS file containing pronunciation dictionary rules

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.pronunciation_dictionaries.download(
                dictionary_id="21m00Tcm4TlvDq8ikWAM",
                version_id="BdF0s0aZ3oFoKnDYdTox",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().download(
            dictionary_id, version_id, request_options=request_options
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

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        sort: Union[Sort, None] = SENTINEL,
        sort_direction: Union[str, None] = SENTINEL,
        include_archived: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetPronunciationDictionariesMetadataResponseModel]:  # type: ignore[override]
        """
        Get a list of the pronunciation dictionaries you have access to and their metadata

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many pronunciation dictionaries to return at maximum. Can not exceed 100, defaults to 30.

        sort : typing.Optional[Sort]
            Which field to sort by, one of 'created_at_unix' or 'name'.

        sort_direction : typing.Optional[str]
            Which direction to sort the voices in. 'ascending' or 'descending'.

        include_archived : typing.Optional[bool]
            Whether to include archived pronunciation dictionaries in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionariesMetadataResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import Sort

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.pronunciation_dictionaries.list(
                cursor="cursor",
                page_size=30,
                sort="creation_time_unix",
                sort_direction="sort_direction",
                include_archived=False,
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
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "include_archived": include_archived,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawPronunciationDictionariesClient:
    """
    Async raw-response client for AsyncPronunciationDictionariesClient.
    """

    def __init__(self, client: AsyncPronunciationDictionariesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create_from_file(
        self,
        *,
        name: str,
        file: Union[bytes, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        workspace_access: Union[
            AddPronunciationDictionaryRequestWorkspaceAccess, None
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddPronunciationDictionaryResponseModel]:
        data = await AsyncPronunciationDictionariesClient.create_from_file(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "description": description,
                        "workspace_access": workspace_access,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create_from_rules(
        self,
        *,
        rules: List[
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
        ],
        name: str,
        description: Union[str, None] = SENTINEL,
        workspace_access: Union[
            BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess,
            None,
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddPronunciationDictionaryResponseModel]:
        data = await AsyncPronunciationDictionariesClient.create_from_rules(
            self._client,
            rules=rules,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "description": description,
                        "workspace_access": workspace_access,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        pronunciation_dictionary_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPronunciationDictionaryWithRulesResponseModel]:
        data = await AsyncPronunciationDictionariesClient.get(
            self._client, pronunciation_dictionary_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        pronunciation_dictionary_id: str,
        *,
        archived: Optional[bool] = SENTINEL,
        name: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPronunciationDictionaryMetadataResponse]:
        data = await AsyncPronunciationDictionariesClient.update(
            self._client,
            pronunciation_dictionary_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"archived": archived, "name": name}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def download(
        self,
        dictionary_id: str,
        version_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncPronunciationDictionariesClient.download(
            _call_client, dictionary_id, version_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    async def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        sort: Union[Sort, None] = SENTINEL,
        sort_direction: Union[str, None] = SENTINEL,
        include_archived: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPronunciationDictionariesMetadataResponseModel]:
        data = await AsyncPronunciationDictionariesClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "include_archived": include_archived,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
