from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyListApiRequestsV1WorkspaceAnalyticsRequestsPost,
    BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort,
    ColumnFilter,
    HttpValidationError,
    WorkspaceAnalyticsQueryResponseModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class RequestsClient(BaseService):
    """
    Fern-style resource client for RequestsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    @property
    def with_raw_response(self) -> "RawRequestsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawRequestsClient(self)

    @cast_models
    def get(
        self,
        *,
        start_time: Union[int, None] = SENTINEL,
        end_time: Union[int, None] = SENTINEL,
        limit: Optional[int] = SENTINEL,
        sort: Union[
            BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort, None
        ] = SENTINEL,
        filters: Union[List[ColumnFilter], None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceAnalyticsQueryResponseModel:
        """
        Returns a list of API requests. Supports filtering by time range, column filters, and search terms. At least one of start_time or end_time must be provided. An optional sort parameter controls timestamp ordering. Results are ordered by timestamp. Descending if end_time is used, ascending if start_time is used. The response is a tabular structure with columns, column_types, column_units, and rows.

        Parameters
        ----------
        start_time : typing.Optional[int]
            Start of the time range as a Unix timestamp in milliseconds.

        end_time : typing.Optional[int]
            End of the time range as a Unix timestamp in milliseconds.

        limit : typing.Optional[int]

        sort : typing.Optional[BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort]
            Optional timestamp sort direction. If omitted, defaults to desc when end_time is provided, otherwise asc.

        filters : typing.Optional[typing.Sequence[ColumnFilter]]

        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceAnalyticsQueryResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.analytics.requests.get(
            start_time=1055364925217508,
            end_time=146161626697436,
            limit=100,
            sort="asc",
            filters=[
                {
                    "column": "column",
                    "operation": "in",
                    "values": [
                        "ut ad"
                    ]
                }
            ],
            search="search",
        )
        """

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        request_body = BodyListApiRequestsV1WorkspaceAnalyticsRequestsPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "limit": limit,
                        "sort": sort,
                        "filters": filters,
                        "search": search,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyListApiRequestsV1WorkspaceAnalyticsRequestsPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/analytics/requests",
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
                WorkspaceAnalyticsQueryResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WorkspaceAnalyticsQueryResponseModel, response)
            )
        )


class RawRequestsClient:
    """
    Raw-response client for RequestsClient.

    Each method delegates to the matching :class:`RequestsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: RequestsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        *,
        start_time: Union[int, None] = SENTINEL,
        end_time: Union[int, None] = SENTINEL,
        limit: Optional[int] = SENTINEL,
        sort: Union[
            BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort, None
        ] = SENTINEL,
        filters: Union[List[ColumnFilter], None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceAnalyticsQueryResponseModel]:
        data = RequestsClient.get(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "limit": limit,
                        "sort": sort,
                        "filters": filters,
                        "search": search,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncRequestsClient(RequestsClient):
    """
    Async wrapper for RequestsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawRequestsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawRequestsClient(self)

    def get(
        self,
        *,
        start_time: Union[int, None] = SENTINEL,
        end_time: Union[int, None] = SENTINEL,
        limit: Optional[int] = SENTINEL,
        sort: Union[
            BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort, None
        ] = SENTINEL,
        filters: Union[List[ColumnFilter], None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceAnalyticsQueryResponseModel]:  # type: ignore[override]
        """
        Returns a list of API requests. Supports filtering by time range, column filters, and search terms. At least one of start_time or end_time must be provided. An optional sort parameter controls timestamp ordering. Results are ordered by timestamp. Descending if end_time is used, ascending if start_time is used. The response is a tabular structure with columns, column_types, column_units, and rows.

        Parameters
        ----------
        start_time : typing.Optional[int]
            Start of the time range as a Unix timestamp in milliseconds.

        end_time : typing.Optional[int]
            End of the time range as a Unix timestamp in milliseconds.

        limit : typing.Optional[int]

        sort : typing.Optional[BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort]
            Optional timestamp sort direction. If omitted, defaults to desc when end_time is provided, otherwise asc.

        filters : typing.Optional[typing.Sequence[ColumnFilter]]

        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceAnalyticsQueryResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.analytics.requests.get(
                start_time=1055364925217508,
                end_time=146161626697436,
                limit=100,
                sort="asc",
                filters=[
                    {
                        "column": "column",
                        "operation": "in",
                        "values": [
                            "ut ad"
                        ]
                    }
                ],
                search="search",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "limit": limit,
                        "sort": sort,
                        "filters": filters,
                        "search": search,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawRequestsClient:
    """
    Async raw-response client for AsyncRequestsClient.
    """

    def __init__(self, client: AsyncRequestsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        *,
        start_time: Union[int, None] = SENTINEL,
        end_time: Union[int, None] = SENTINEL,
        limit: Optional[int] = SENTINEL,
        sort: Union[
            BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort, None
        ] = SENTINEL,
        filters: Union[List[ColumnFilter], None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceAnalyticsQueryResponseModel]:
        data = await AsyncRequestsClient.get(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "limit": limit,
                        "sort": sort,
                        "filters": filters,
                        "search": search,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
