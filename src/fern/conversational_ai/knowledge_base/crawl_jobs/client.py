from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyCreateCrawlJobV1ConvaiKnowledgeBaseCrawlPost,
    CreateCrawlJobResponseModel,
    GetCrawlJobResponseModel,
    HttpValidationError,
    ListCrawlJobsResponseModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class CrawlJobsClient(BaseService):
    """
    Fern-style resource client for CrawlJobsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._cancel_config: SdkConfig = {}

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

    def set_cancel_config(self, config: SdkConfig):
        """
        Sets method-level configuration for cancel.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._cancel_config = config
        return self

    @property
    def with_raw_response(self) -> "RawCrawlJobsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawCrawlJobsClient(self)

    @cast_models
    def list(
        self,
        *,
        include_job_ids: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ListCrawlJobsResponseModel:
        """
        Get a list of ongoing and recent crawl jobs for the user.

        Parameters
        ----------
        include_job_ids : typing.Optional[typing.Sequence[str]]
            Ids of additional crawl jobs to retrieve

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCrawlJobsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.crawl_jobs.list(
            include_job_ids=[
                "include_job_ids"
            ],
            page_size=30,
            cursor="cursor",
        )
        """

        Validator(str).is_array().is_optional().is_nullable().validate(
            include_job_ids, "include_job_ids"
        )
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/crawl",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("include_job_ids", include_job_ids, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListCrawlJobsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListCrawlJobsResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        url: str,
        max_depth: Optional[int] = SENTINEL,
        max_pages: Optional[int] = SENTINEL,
        pattern: Union[str, None] = SENTINEL,
        sitemap_urls: Union[List[str], None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> CreateCrawlJobResponseModel:
        """
        Create a crawl job to crawl the given URL with specified depth and page limits.

        Parameters
        ----------
        url : str
            URL to a page of documentation that the agent will have access to in order to interact with users.

        max_depth : typing.Optional[int]
            Maximum depth for crawling (1-5), defaults to 3.

        max_pages : typing.Optional[int]
            Maximum number of pages to crawl (1-10,000), defaults to 1000.

        pattern : typing.Optional[str]
            If set, only URLs that match this pattern are included.

        sitemap_urls : typing.Optional[typing.Sequence[str]]
            List of URLs to crawl from sitemap (optional, overrides automatic URL discovery).

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        enable_auto_sync : typing.Optional[bool]
            Whether to enable auto-sync for this URL document.

        auto_remove : typing.Optional[bool]
            Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCrawlJobResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.crawl_jobs.create(
            url="url",
            max_depth=3,
            max_pages=1000,
            pattern="pattern",
            sitemap_urls=[
                "sitemap_urls"
            ],
            parent_folder_id="parent_folder_id",
            enable_auto_sync=False,
            auto_remove=True,
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateCrawlJobV1ConvaiKnowledgeBaseCrawlPost(
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "max_depth": max_depth,
                        "max_pages": max_pages,
                        "pattern": pattern,
                        "sitemap_urls": sitemap_urls,
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateCrawlJobV1ConvaiKnowledgeBaseCrawlPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/crawl",
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
                CreateCrawlJobResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreateCrawlJobResponseModel, response)
            )
        )

    @cast_models
    def get(
        self, crawl_job_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetCrawlJobResponseModel:
        """
        Get details about a specific crawl job including status and progress.

        Parameters
        ----------
        crawl_job_id : str
            The id of the crawl job to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCrawlJobResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.crawl_jobs.get(
            crawl_job_id="crawl_job_id",
        )
        """

        Validator(str).validate(crawl_job_id, "crawl_job_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/crawl/{{crawl_job_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("crawl_job_id", crawl_job_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetCrawlJobResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetCrawlJobResponseModel, response)
            )
        )

    @cast_models
    def cancel(
        self, crawl_job_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Any:
        """
        Cancel a crawl job and delete all associated documents and folders.

        Parameters
        ----------
        crawl_job_id : str
            The id of the crawl job to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.crawl_jobs.cancel(
            crawl_job_id="crawl_job_id",
        )
        """

        Validator(str).validate(crawl_job_id, "crawl_job_id")

        resolved_config = self._get_resolved_config(
            self._cancel_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/crawl/{{crawl_job_id}}/cancel",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("crawl_job_id", crawl_job_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawCrawlJobsClient:
    """
    Raw-response client for CrawlJobsClient.

    Each method delegates to the matching :class:`CrawlJobsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: CrawlJobsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        include_job_ids: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCrawlJobsResponseModel]:
        data = CrawlJobsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_job_ids": include_job_ids,
                        "page_size": page_size,
                        "cursor": cursor,
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
        url: str,
        max_depth: Optional[int] = SENTINEL,
        max_pages: Optional[int] = SENTINEL,
        pattern: Union[str, None] = SENTINEL,
        sitemap_urls: Union[List[str], None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCrawlJobResponseModel]:
        data = CrawlJobsClient.create(
            self._client,
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "max_depth": max_depth,
                        "max_pages": max_pages,
                        "pattern": pattern,
                        "sitemap_urls": sitemap_urls,
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, crawl_job_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetCrawlJobResponseModel]:
        data = CrawlJobsClient.get(
            self._client, crawl_job_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def cancel(
        self, crawl_job_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = CrawlJobsClient.cancel(
            self._client, crawl_job_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncCrawlJobsClient(CrawlJobsClient):
    """
    Async wrapper for CrawlJobsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawCrawlJobsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawCrawlJobsClient(self)

    def list(
        self,
        *,
        include_job_ids: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListCrawlJobsResponseModel]:  # type: ignore[override]
        """
        Get a list of ongoing and recent crawl jobs for the user.

        Parameters
        ----------
        include_job_ids : typing.Optional[typing.Sequence[str]]
            Ids of additional crawl jobs to retrieve

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCrawlJobsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.crawl_jobs.list(
                include_job_ids=[
                    "include_job_ids"
                ],
                page_size=30,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_job_ids": include_job_ids,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        url: str,
        max_depth: Optional[int] = SENTINEL,
        max_pages: Optional[int] = SENTINEL,
        pattern: Union[str, None] = SENTINEL,
        sitemap_urls: Union[List[str], None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreateCrawlJobResponseModel]:  # type: ignore[override]
        """
        Create a crawl job to crawl the given URL with specified depth and page limits.

        Parameters
        ----------
        url : str
            URL to a page of documentation that the agent will have access to in order to interact with users.

        max_depth : typing.Optional[int]
            Maximum depth for crawling (1-5), defaults to 3.

        max_pages : typing.Optional[int]
            Maximum number of pages to crawl (1-10,000), defaults to 1000.

        pattern : typing.Optional[str]
            If set, only URLs that match this pattern are included.

        sitemap_urls : typing.Optional[typing.Sequence[str]]
            List of URLs to crawl from sitemap (optional, overrides automatic URL discovery).

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        enable_auto_sync : typing.Optional[bool]
            Whether to enable auto-sync for this URL document.

        auto_remove : typing.Optional[bool]
            Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCrawlJobResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.crawl_jobs.create(
                url="url",
                max_depth=3,
                max_pages=1000,
                pattern="pattern",
                sitemap_urls=[
                    "sitemap_urls"
                ],
                parent_folder_id="parent_folder_id",
                enable_auto_sync=False,
                auto_remove=True,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "max_depth": max_depth,
                        "max_pages": max_pages,
                        "pattern": pattern,
                        "sitemap_urls": sitemap_urls,
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, crawl_job_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetCrawlJobResponseModel]:  # type: ignore[override]
        """
        Get details about a specific crawl job including status and progress.

        Parameters
        ----------
        crawl_job_id : str
            The id of the crawl job to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCrawlJobResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.crawl_jobs.get(
                crawl_job_id="crawl_job_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(crawl_job_id, request_options=request_options)

    def cancel(
        self, crawl_job_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Cancel a crawl job and delete all associated documents and folders.

        Parameters
        ----------
        crawl_job_id : str
            The id of the crawl job to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.crawl_jobs.cancel(
                crawl_job_id="crawl_job_id",
            )


        asyncio.run(main())
        """
        return to_async(super().cancel)(crawl_job_id, request_options=request_options)


class AsyncRawCrawlJobsClient:
    """
    Async raw-response client for AsyncCrawlJobsClient.
    """

    def __init__(self, client: AsyncCrawlJobsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        include_job_ids: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCrawlJobsResponseModel]:
        data = await AsyncCrawlJobsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_job_ids": include_job_ids,
                        "page_size": page_size,
                        "cursor": cursor,
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
        url: str,
        max_depth: Optional[int] = SENTINEL,
        max_pages: Optional[int] = SENTINEL,
        pattern: Union[str, None] = SENTINEL,
        sitemap_urls: Union[List[str], None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCrawlJobResponseModel]:
        data = await AsyncCrawlJobsClient.create(
            self._client,
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "max_depth": max_depth,
                        "max_pages": max_pages,
                        "pattern": pattern,
                        "sitemap_urls": sitemap_urls,
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, crawl_job_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetCrawlJobResponseModel]:
        data = await AsyncCrawlJobsClient.get(
            self._client, crawl_job_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def cancel(
        self, crawl_job_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = await AsyncCrawlJobsClient.cancel(
            self._client, crawl_job_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
