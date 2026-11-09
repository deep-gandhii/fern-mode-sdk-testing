from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePost,
    BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem,
    ColumnFilter,
    HttpValidationError,
    WorkspaceAnalyticsQueryResponseModel,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class UsageClient(BaseService):
    """
    Fern-style resource client for UsageClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_usage_by_product_over_time_config: SdkConfig = {}

    def set_get_usage_by_product_over_time_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_usage_by_product_over_time.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_usage_by_product_over_time_config = config
        return self

    @property
    def with_raw_response(self) -> "RawUsageClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawUsageClient(self)

    @cast_models
    def get_usage_by_product_over_time(
        self,
        *,
        start_time: int,
        end_time: int,
        interval_seconds: Optional[int] = SENTINEL,
        group_by: Union[
            List[
                BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem
            ],
            None,
        ] = SENTINEL,
        filters: Union[List[ColumnFilter], None] = SENTINEL,
        time_zone: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceAnalyticsQueryResponseModel:
        """
        Returns credit usage broken down by product type over time. The response is a tabular structure with columns, column_types, column_units, and rows.

        Parameters
        ----------
        start_time : int
            Start of the time range as a Unix timestamp in milliseconds. Must be at least 2020-01-01.

        end_time : int
            End of the time range as a Unix timestamp in milliseconds. Must be at least 2020-01-01.

        interval_seconds : typing.Optional[int]
            Bucket size in seconds. Each row in the response covers this many seconds of the selected time range. For example, pass 3600 for hourly buckets or 86400 for daily buckets. Whether `time_zone` shifts bucket boundaries depends on this value: whole-day multiples (e.g. 86400) align to local midnight; whole-hour multiples up to 24 hours (e.g. 3600, 14400) align to local hour boundaries from midnight; sub-hour values and other sizes remain UTC-anchored regardless of `time_zone`.

        group_by : typing.Optional[typing.Sequence[BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem]]

        filters : typing.Optional[typing.Sequence[ColumnFilter]]

        time_zone : typing.Optional[str]
            IANA time zone identifier (e.g. 'America/New_York', 'Europe/London', 'UTC') used to align bucket boundaries for eligible `interval_seconds` values. Whole-day multiples start at local midnight; whole-hour multiples up to 24 hours align to local hour boundaries from midnight. Sub-hour intervals and other bucket sizes remain UTC-anchored regardless of this setting. Defaults to UTC.

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
        client.workspace.usage.get_usage_by_product_over_time(
            start_time=4894411226981458,
            end_time=2202116186654383,
            interval_seconds=60,
            group_by=[
                "product_type"
            ],
            filters=[
                {
                    "column": "column",
                    "operation": "in",
                    "values": [
                        "ut ad"
                    ]
                }
            ],
            time_zone="UTC",
        )
        """

        resolved_config = self._get_resolved_config(
            self._get_usage_by_product_over_time_config, request_options
        )

        request_body = (
            BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePost(
                start_time=start_time,
                end_time=end_time,
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "interval_seconds": interval_seconds,
                            "group_by": group_by,
                            "filters": filters,
                            "time_zone": time_zone,
                        }.items()
                        if v is not SENTINEL
                    }
                ),
            )
        )
        Validator(
            BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/analytics/query/usage-by-product-over-time",
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


class RawUsageClient:
    """
    Raw-response client for UsageClient.

    Each method delegates to the matching :class:`UsageClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: UsageClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get_usage_by_product_over_time(
        self,
        *,
        start_time: int,
        end_time: int,
        interval_seconds: Optional[int] = SENTINEL,
        group_by: Union[
            List[
                BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem
            ],
            None,
        ] = SENTINEL,
        filters: Union[List[ColumnFilter], None] = SENTINEL,
        time_zone: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceAnalyticsQueryResponseModel]:
        data = UsageClient.get_usage_by_product_over_time(
            self._client,
            start_time=start_time,
            end_time=end_time,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "interval_seconds": interval_seconds,
                        "group_by": group_by,
                        "filters": filters,
                        "time_zone": time_zone,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncUsageClient(UsageClient):
    """
    Async wrapper for UsageClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawUsageClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawUsageClient(self)

    def get_usage_by_product_over_time(
        self,
        *,
        start_time: int,
        end_time: int,
        interval_seconds: Optional[int] = SENTINEL,
        group_by: Union[
            List[
                BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem
            ],
            None,
        ] = SENTINEL,
        filters: Union[List[ColumnFilter], None] = SENTINEL,
        time_zone: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceAnalyticsQueryResponseModel]:  # type: ignore[override]
        """
        Returns credit usage broken down by product type over time. The response is a tabular structure with columns, column_types, column_units, and rows.

        Parameters
        ----------
        start_time : int
            Start of the time range as a Unix timestamp in milliseconds. Must be at least 2020-01-01.

        end_time : int
            End of the time range as a Unix timestamp in milliseconds. Must be at least 2020-01-01.

        interval_seconds : typing.Optional[int]
            Bucket size in seconds. Each row in the response covers this many seconds of the selected time range. For example, pass 3600 for hourly buckets or 86400 for daily buckets. Whether `time_zone` shifts bucket boundaries depends on this value: whole-day multiples (e.g. 86400) align to local midnight; whole-hour multiples up to 24 hours (e.g. 3600, 14400) align to local hour boundaries from midnight; sub-hour values and other sizes remain UTC-anchored regardless of `time_zone`.

        group_by : typing.Optional[typing.Sequence[BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem]]

        filters : typing.Optional[typing.Sequence[ColumnFilter]]

        time_zone : typing.Optional[str]
            IANA time zone identifier (e.g. 'America/New_York', 'Europe/London', 'UTC') used to align bucket boundaries for eligible `interval_seconds` values. Whole-day multiples start at local midnight; whole-hour multiples up to 24 hours align to local hour boundaries from midnight. Sub-hour intervals and other bucket sizes remain UTC-anchored regardless of this setting. Defaults to UTC.

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
            await client.workspace.usage.get_usage_by_product_over_time(
                start_time=4894411226981458,
                end_time=2202116186654383,
                interval_seconds=60,
                group_by=[
                    "product_type"
                ],
                filters=[
                    {
                        "column": "column",
                        "operation": "in",
                        "values": [
                            "ut ad"
                        ]
                    }
                ],
                time_zone="UTC",
            )


        asyncio.run(main())
        """
        return to_async(super().get_usage_by_product_over_time)(
            start_time=start_time,
            end_time=end_time,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "interval_seconds": interval_seconds,
                        "group_by": group_by,
                        "filters": filters,
                        "time_zone": time_zone,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawUsageClient:
    """
    Async raw-response client for AsyncUsageClient.
    """

    def __init__(self, client: AsyncUsageClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get_usage_by_product_over_time(
        self,
        *,
        start_time: int,
        end_time: int,
        interval_seconds: Optional[int] = SENTINEL,
        group_by: Union[
            List[
                BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem
            ],
            None,
        ] = SENTINEL,
        filters: Union[List[ColumnFilter], None] = SENTINEL,
        time_zone: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceAnalyticsQueryResponseModel]:
        data = await AsyncUsageClient.get_usage_by_product_over_time(
            self._client,
            start_time=start_time,
            end_time=end_time,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "interval_seconds": interval_seconds,
                        "group_by": group_by,
                        "filters": filters,
                        "time_zone": time_zone,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
