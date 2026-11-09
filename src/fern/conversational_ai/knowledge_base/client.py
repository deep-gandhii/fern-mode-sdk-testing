from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyComputeRagIndexesInBatchV1ConvaiKnowledgeBaseRagIndexPost,
    GetKnowledgeBaseListResponseModel,
    GetOrCreateRagIndexRequestModel,
    HttpValidationError,
    KnowledgeBaseContentSearchResponseModel,
    KnowledgeBaseDocumentType,
    KnowledgeBaseSortBy,
    SortDirection,
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
    from .documents.client import (
        DocumentsClient as _DocumentsClient,
        AsyncDocumentsClient as _AsyncDocumentsClient,
    )
    from .crawl_jobs.client import (
        CrawlJobsClient as _CrawlJobsClient,
        AsyncCrawlJobsClient as _AsyncCrawlJobsClient,
    )
    from .document.client import (
        DocumentClient as _DocumentClient,
        AsyncDocumentClient as _AsyncDocumentClient,
    )


class KnowledgeBaseClient(BaseService):
    """
    Fern-style resource client for KnowledgeBaseClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._documents: Any = None
        self._crawl_jobs: Any = None
        self._document: Any = None
        self._list_config: SdkConfig = {}
        self._get_or_create_rag_indexes_config: SdkConfig = {}
        self._search_config: SdkConfig = {}

    @property
    def documents(self) -> "_DocumentsClient":
        """Lazily construct and return the documents sub-resource client."""
        if self._documents is None:
            from .documents.client import DocumentsClient

            _child = DocumentsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._documents = _child
        return self._documents

    @property
    def crawl_jobs(self) -> "_CrawlJobsClient":
        """Lazily construct and return the crawl_jobs sub-resource client."""
        if self._crawl_jobs is None:
            from .crawl_jobs.client import CrawlJobsClient

            _child = CrawlJobsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._crawl_jobs = _child
        return self._crawl_jobs

    @property
    def document(self) -> "_DocumentClient":
        """Lazily construct and return the document sub-resource client."""
        if self._document is None:
            from .document.client import DocumentClient

            _child = DocumentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._document = _child
        return self._document

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
        if self._documents is not None:
            self._documents.set_base_url(base_url)
        if self._crawl_jobs is not None:
            self._crawl_jobs.set_base_url(base_url)
        if self._document is not None:
            self._document.set_base_url(base_url)

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
        if self._documents is not None:
            self._documents.set_config(config)
        if self._crawl_jobs is not None:
            self._crawl_jobs.set_config(config)
        if self._document is not None:
            self._document.set_config(config)

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
        if self._documents is not None:
            self._documents.set_timeout(timeout)
        if self._crawl_jobs is not None:
            self._crawl_jobs.set_timeout(timeout)
        if self._document is not None:
            self._document.set_timeout(timeout)

        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_get_or_create_rag_indexes_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_or_create_rag_indexes.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_or_create_rag_indexes_config = config
        return self

    def set_search_config(self, config: SdkConfig):
        """
        Sets method-level configuration for search.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._search_config = config
        return self

    @property
    def with_raw_response(self) -> "RawKnowledgeBaseClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawKnowledgeBaseClient(self)

    @cast_models
    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        show_only_owned_documents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        types: Union[List[KnowledgeBaseDocumentType], None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        ancestor_folder_id: Union[str, None] = SENTINEL,
        folders_first: Union[bool, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[KnowledgeBaseSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetKnowledgeBaseListResponseModel:
        """
        Get a list of available knowledge base documents

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        search : typing.Optional[str]
            If specified, the endpoint returns only such knowledge base documents whose names start with this string.

        show_only_owned_documents : typing.Optional[bool]
            If set to true, the endpoint will return only documents owned by you (and not shared from somebody else). Deprecated: use created_by_user_id instead.

        created_by_user_id : typing.Optional[str]
            Filter documents by creator user ID. When set, only documents created by this user are returned. Takes precedence over show_only_owned_documents. Use '@me' to refer to the authenticated user.

        types : typing.Optional[typing.Sequence[KnowledgeBaseDocumentType]]
            If present, the endpoint will return only documents of the given types.

        parent_folder_id : typing.Optional[str]
            If set, the endpoint will return only documents that are direct children of the given folder.

        ancestor_folder_id : typing.Optional[str]
            If set, the endpoint will return only documents that are descendants of the given folder.

        folders_first : typing.Optional[bool]
            Whether folders should be returned first in the list of documents.

        sort_direction : typing.Optional[SortDirection]
            The direction to sort the results

        sort_by : typing.Optional[KnowledgeBaseSortBy]
            The field to sort the results by

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetKnowledgeBaseListResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection, KnowledgeBaseSortBy

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.list(
            page_size=30,
            search="search",
            created_by_user_id="created_by_user_id",
            types=[
                "file"
            ],
            parent_folder_id="parent_folder_id",
            ancestor_folder_id="ancestor_folder_id",
            folders_first=True,
            sort_direction="asc",
            sort_by="name",
            cursor="cursor",
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(bool).is_optional().is_nullable().validate(
            show_only_owned_documents, "show_only_owned_documents"
        )
        Validator(str).is_optional().is_nullable().validate(
            created_by_user_id, "created_by_user_id"
        )
        Validator(
            KnowledgeBaseDocumentType
        ).is_array().is_optional().is_nullable().validate(types, "types")
        Validator(str).is_optional().is_nullable().validate(
            parent_folder_id, "parent_folder_id"
        )
        Validator(str).is_optional().is_nullable().validate(
            ancestor_folder_id, "ancestor_folder_id"
        )
        Validator(bool).is_optional().is_nullable().validate(
            folders_first, "folders_first"
        )
        Validator(SortDirection).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )
        Validator(KnowledgeBaseSortBy).is_optional().is_nullable().validate(
            sort_by, "sort_by"
        )
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("page_size", page_size, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query(
                "show_only_owned_documents", show_only_owned_documents, nullable=True
            )
            .add_query("created_by_user_id", created_by_user_id, nullable=True)
            .add_query("types", types, nullable=True)
            .add_query("parent_folder_id", parent_folder_id, nullable=True)
            .add_query("ancestor_folder_id", ancestor_folder_id, nullable=True)
            .add_query("folders_first", folders_first, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .add_query("sort_by", sort_by, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetKnowledgeBaseListResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetKnowledgeBaseListResponseModel, response)
            )
        )

    @cast_models
    def get_or_create_rag_indexes(
        self,
        *,
        items: List[GetOrCreateRagIndexRequestModel],
        request_options: Optional[RequestOptions] = None,
    ) -> dict:
        """
        Retrieves and/or creates RAG indexes for multiple knowledge base documents in a single request. Maximum 100 items per request.

        Parameters
        ----------
        items : typing.Sequence[GetOrCreateRagIndexRequestModel]
            List of requested RAG indexes. Minimum 1, maximum 100 items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dict
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.get_or_create_rag_indexes(
            items=[
                {
                    "document_id": "document_id",
                    "create_if_missing": False,
                    "model": "e5_mistral_7b_instruct"
                }
            ],
        )
        """

        resolved_config = self._get_resolved_config(
            self._get_or_create_rag_indexes_config, request_options
        )

        request_body = BodyComputeRagIndexesInBatchV1ConvaiKnowledgeBaseRagIndexPost(
            items=items
        )
        Validator(
            BodyComputeRagIndexesInBatchV1ConvaiKnowledgeBaseRagIndexPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/rag-index",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def search(
        self,
        *,
        query: str,
        page_size: Union[int, None] = SENTINEL,
        types: Union[List[KnowledgeBaseDocumentType], None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> KnowledgeBaseContentSearchResponseModel:
        """
        Fuzzy text search over knowledge base document content

        Parameters
        ----------
        query : str
            The search query text

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        types : typing.Optional[typing.Sequence[KnowledgeBaseDocumentType]]
            If present, the endpoint will return only documents of the given types.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBaseContentSearchResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.search(
            query="query",
            page_size=30,
            types=[
                "file"
            ],
            cursor="cursor",
        )
        """

        Validator(str).validate(query, "query")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(
            KnowledgeBaseDocumentType
        ).is_array().is_optional().is_nullable().validate(types, "types")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(
            self._search_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/search",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("query", query)
            .add_query("page_size", page_size, nullable=True)
            .add_query("types", types, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                KnowledgeBaseContentSearchResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    KnowledgeBaseContentSearchResponseModel, response
                )
            )
        )


class RawKnowledgeBaseClient:
    """
    Raw-response client for KnowledgeBaseClient.

    Each method delegates to the matching :class:`KnowledgeBaseClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: KnowledgeBaseClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        show_only_owned_documents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        types: Union[List[KnowledgeBaseDocumentType], None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        ancestor_folder_id: Union[str, None] = SENTINEL,
        folders_first: Union[bool, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[KnowledgeBaseSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetKnowledgeBaseListResponseModel]:
        data = KnowledgeBaseClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "search": search,
                        "show_only_owned_documents": show_only_owned_documents,
                        "created_by_user_id": created_by_user_id,
                        "types": types,
                        "parent_folder_id": parent_folder_id,
                        "ancestor_folder_id": ancestor_folder_id,
                        "folders_first": folders_first,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_or_create_rag_indexes(
        self,
        *,
        items: List[GetOrCreateRagIndexRequestModel],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[dict]:
        data = KnowledgeBaseClient.get_or_create_rag_indexes(
            self._client, items=items, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def search(
        self,
        *,
        query: str,
        page_size: Union[int, None] = SENTINEL,
        types: Union[List[KnowledgeBaseDocumentType], None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[KnowledgeBaseContentSearchResponseModel]:
        data = KnowledgeBaseClient.search(
            self._client,
            query=query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "types": types,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncKnowledgeBaseClient(KnowledgeBaseClient):
    """
    Async wrapper for KnowledgeBaseClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def documents(self) -> "_AsyncDocumentsClient":
        """Lazily construct and return the async documents sub-resource client."""
        if self._documents is None:
            from .documents.client import AsyncDocumentsClient

            _child = AsyncDocumentsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._documents = _child
        return self._documents

    @property
    def crawl_jobs(self) -> "_AsyncCrawlJobsClient":
        """Lazily construct and return the async crawl_jobs sub-resource client."""
        if self._crawl_jobs is None:
            from .crawl_jobs.client import AsyncCrawlJobsClient

            _child = AsyncCrawlJobsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._crawl_jobs = _child
        return self._crawl_jobs

    @property
    def document(self) -> "_AsyncDocumentClient":
        """Lazily construct and return the async document sub-resource client."""
        if self._document is None:
            from .document.client import AsyncDocumentClient

            _child = AsyncDocumentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._document = _child
        return self._document

    @property
    def with_raw_response(self) -> "AsyncRawKnowledgeBaseClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawKnowledgeBaseClient(self)

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        show_only_owned_documents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        types: Union[List[KnowledgeBaseDocumentType], None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        ancestor_folder_id: Union[str, None] = SENTINEL,
        folders_first: Union[bool, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[KnowledgeBaseSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetKnowledgeBaseListResponseModel]:  # type: ignore[override]
        """
        Get a list of available knowledge base documents

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        search : typing.Optional[str]
            If specified, the endpoint returns only such knowledge base documents whose names start with this string.

        show_only_owned_documents : typing.Optional[bool]
            If set to true, the endpoint will return only documents owned by you (and not shared from somebody else). Deprecated: use created_by_user_id instead.

        created_by_user_id : typing.Optional[str]
            Filter documents by creator user ID. When set, only documents created by this user are returned. Takes precedence over show_only_owned_documents. Use '@me' to refer to the authenticated user.

        types : typing.Optional[typing.Sequence[KnowledgeBaseDocumentType]]
            If present, the endpoint will return only documents of the given types.

        parent_folder_id : typing.Optional[str]
            If set, the endpoint will return only documents that are direct children of the given folder.

        ancestor_folder_id : typing.Optional[str]
            If set, the endpoint will return only documents that are descendants of the given folder.

        folders_first : typing.Optional[bool]
            Whether folders should be returned first in the list of documents.

        sort_direction : typing.Optional[SortDirection]
            The direction to sort the results

        sort_by : typing.Optional[KnowledgeBaseSortBy]
            The field to sort the results by

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetKnowledgeBaseListResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection, KnowledgeBaseSortBy

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.list(
                page_size=30,
                search="search",
                created_by_user_id="created_by_user_id",
                types=[
                    "file"
                ],
                parent_folder_id="parent_folder_id",
                ancestor_folder_id="ancestor_folder_id",
                folders_first=True,
                sort_direction="asc",
                sort_by="name",
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "search": search,
                        "show_only_owned_documents": show_only_owned_documents,
                        "created_by_user_id": created_by_user_id,
                        "types": types,
                        "parent_folder_id": parent_folder_id,
                        "ancestor_folder_id": ancestor_folder_id,
                        "folders_first": folders_first,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get_or_create_rag_indexes(
        self,
        *,
        items: List[GetOrCreateRagIndexRequestModel],
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[dict]:  # type: ignore[override]
        """
        Retrieves and/or creates RAG indexes for multiple knowledge base documents in a single request. Maximum 100 items per request.

        Parameters
        ----------
        items : typing.Sequence[GetOrCreateRagIndexRequestModel]
            List of requested RAG indexes. Minimum 1, maximum 100 items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dict
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.get_or_create_rag_indexes(
                items=[
                    {
                        "document_id": "document_id",
                        "create_if_missing": False,
                        "model": "e5_mistral_7b_instruct"
                    }
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().get_or_create_rag_indexes)(
            items=items, request_options=request_options
        )

    def search(
        self,
        *,
        query: str,
        page_size: Union[int, None] = SENTINEL,
        types: Union[List[KnowledgeBaseDocumentType], None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[KnowledgeBaseContentSearchResponseModel]:  # type: ignore[override]
        """
        Fuzzy text search over knowledge base document content

        Parameters
        ----------
        query : str
            The search query text

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        types : typing.Optional[typing.Sequence[KnowledgeBaseDocumentType]]
            If present, the endpoint will return only documents of the given types.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBaseContentSearchResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.search(
                query="query",
                page_size=30,
                types=[
                    "file"
                ],
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().search)(
            query=query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "types": types,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawKnowledgeBaseClient:
    """
    Async raw-response client for AsyncKnowledgeBaseClient.
    """

    def __init__(self, client: AsyncKnowledgeBaseClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        show_only_owned_documents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        types: Union[List[KnowledgeBaseDocumentType], None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        ancestor_folder_id: Union[str, None] = SENTINEL,
        folders_first: Union[bool, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[KnowledgeBaseSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetKnowledgeBaseListResponseModel]:
        data = await AsyncKnowledgeBaseClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "search": search,
                        "show_only_owned_documents": show_only_owned_documents,
                        "created_by_user_id": created_by_user_id,
                        "types": types,
                        "parent_folder_id": parent_folder_id,
                        "ancestor_folder_id": ancestor_folder_id,
                        "folders_first": folders_first,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_or_create_rag_indexes(
        self,
        *,
        items: List[GetOrCreateRagIndexRequestModel],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[dict]:
        data = await AsyncKnowledgeBaseClient.get_or_create_rag_indexes(
            self._client, items=items, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def search(
        self,
        *,
        query: str,
        page_size: Union[int, None] = SENTINEL,
        types: Union[List[KnowledgeBaseDocumentType], None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[KnowledgeBaseContentSearchResponseModel]:
        data = await AsyncKnowledgeBaseClient.search(
            self._client,
            query=query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "types": types,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
