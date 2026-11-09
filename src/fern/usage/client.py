from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    BreakdownTypes,
    HttpValidationError,
    MetricType,
    UsageAggregationInterval,
    UsageCharactersResponseModel,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
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
    def with_raw_response(self) -> "RawUsageClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawUsageClient(self)

    @cast_models
    def get(
        self,
        *,
        start_unix: int,
        end_unix: int,
        include_workspace_metrics: Union[bool, None] = SENTINEL,
        breakdown_type: Union[BreakdownTypes, None] = SENTINEL,
        aggregation_interval: Union[UsageAggregationInterval, None] = SENTINEL,
        aggregation_bucket_size: Union[int, None] = SENTINEL,
        metric: Union[MetricType, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> UsageCharactersResponseModel:
        """
        (Deprecated) This endpoint is deprecated. Use /v1/workspace/analytics/query/usage-by-product-over-time instead, which exposes the bucket size as `interval_seconds` (an integer in seconds) rather than `aggregation_interval`. Returns the usage metrics for the current user or the entire workspace they are part of. The response provides a time axis based on the specified aggregation interval (default: day), with usage values for each interval along that axis. Usage is broken down by the selected breakdown type. For example, breakdown type "voice" will return the usage of each voice for each interval along the time axis.

        Parameters
        ----------
        start_unix : int
            UTC Unix timestamp for the start of the usage window, in milliseconds. To include the first day of the window, the timestamp should be at 00:00:00 of that day.

        end_unix : int
            UTC Unix timestamp for the end of the usage window, in milliseconds. To include the last day of the window, the timestamp should be at 23:59:59 of that day.

        include_workspace_metrics : typing.Optional[bool]
            Whether or not to include the statistics of the entire workspace.

        breakdown_type : typing.Optional[BreakdownTypes]
            How to break down the information. Cannot be "user" if include_workspace_metrics is False.

        aggregation_interval : typing.Optional[UsageAggregationInterval]
            How to aggregate usage data over time. Can be "hour", "day", "week", "month", or "cumulative".

        aggregation_bucket_size : typing.Optional[int]
            Aggregation bucket size in seconds. Overrides the aggregation interval.

        metric : typing.Optional[MetricType]
            Which metric to aggregate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageCharactersResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import BreakdownTypes, UsageAggregationInterval, MetricType

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.usage.get(
            start_unix=1685574000,
            end_unix=1688165999,
            include_workspace_metrics=True,
            breakdown_type="none",
            aggregation_interval="hour",
            aggregation_bucket_size=6,
            metric="credits",
        )
        """

        Validator(int).validate(start_unix, "start_unix")
        Validator(int).validate(end_unix, "end_unix")
        Validator(bool).is_optional().is_nullable().validate(
            include_workspace_metrics, "include_workspace_metrics"
        )
        Validator(BreakdownTypes).is_optional().is_nullable().validate(
            breakdown_type, "breakdown_type"
        )
        Validator(UsageAggregationInterval).is_optional().is_nullable().validate(
            aggregation_interval, "aggregation_interval"
        )
        Validator(int).is_optional().is_nullable().validate(
            aggregation_bucket_size, "aggregation_bucket_size"
        )
        Validator(MetricType).is_optional().is_nullable().validate(metric, "metric")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/usage/character-stats",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("start_unix", start_unix)
            .add_query("end_unix", end_unix)
            .add_query(
                "include_workspace_metrics", include_workspace_metrics, nullable=True
            )
            .add_query("breakdown_type", breakdown_type, nullable=True)
            .add_query("aggregation_interval", aggregation_interval, nullable=True)
            .add_query(
                "aggregation_bucket_size", aggregation_bucket_size, nullable=True
            )
            .add_query("metric", metric, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                UsageCharactersResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(UsageCharactersResponseModel, response)
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

    def get(
        self,
        *,
        start_unix: int,
        end_unix: int,
        include_workspace_metrics: Union[bool, None] = SENTINEL,
        breakdown_type: Union[BreakdownTypes, None] = SENTINEL,
        aggregation_interval: Union[UsageAggregationInterval, None] = SENTINEL,
        aggregation_bucket_size: Union[int, None] = SENTINEL,
        metric: Union[MetricType, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[UsageCharactersResponseModel]:
        data = UsageClient.get(
            self._client,
            start_unix=start_unix,
            end_unix=end_unix,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_workspace_metrics": include_workspace_metrics,
                        "breakdown_type": breakdown_type,
                        "aggregation_interval": aggregation_interval,
                        "aggregation_bucket_size": aggregation_bucket_size,
                        "metric": metric,
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

    def get(
        self,
        *,
        start_unix: int,
        end_unix: int,
        include_workspace_metrics: Union[bool, None] = SENTINEL,
        breakdown_type: Union[BreakdownTypes, None] = SENTINEL,
        aggregation_interval: Union[UsageAggregationInterval, None] = SENTINEL,
        aggregation_bucket_size: Union[int, None] = SENTINEL,
        metric: Union[MetricType, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[UsageCharactersResponseModel]:  # type: ignore[override]
        """
        (Deprecated) This endpoint is deprecated. Use /v1/workspace/analytics/query/usage-by-product-over-time instead, which exposes the bucket size as `interval_seconds` (an integer in seconds) rather than `aggregation_interval`. Returns the usage metrics for the current user or the entire workspace they are part of. The response provides a time axis based on the specified aggregation interval (default: day), with usage values for each interval along that axis. Usage is broken down by the selected breakdown type. For example, breakdown type "voice" will return the usage of each voice for each interval along the time axis.

        Parameters
        ----------
        start_unix : int
            UTC Unix timestamp for the start of the usage window, in milliseconds. To include the first day of the window, the timestamp should be at 00:00:00 of that day.

        end_unix : int
            UTC Unix timestamp for the end of the usage window, in milliseconds. To include the last day of the window, the timestamp should be at 23:59:59 of that day.

        include_workspace_metrics : typing.Optional[bool]
            Whether or not to include the statistics of the entire workspace.

        breakdown_type : typing.Optional[BreakdownTypes]
            How to break down the information. Cannot be "user" if include_workspace_metrics is False.

        aggregation_interval : typing.Optional[UsageAggregationInterval]
            How to aggregate usage data over time. Can be "hour", "day", "week", "month", or "cumulative".

        aggregation_bucket_size : typing.Optional[int]
            Aggregation bucket size in seconds. Overrides the aggregation interval.

        metric : typing.Optional[MetricType]
            Which metric to aggregate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageCharactersResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import BreakdownTypes, UsageAggregationInterval, MetricType

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.usage.get(
                start_unix=1685574000,
                end_unix=1688165999,
                include_workspace_metrics=True,
                breakdown_type="none",
                aggregation_interval="hour",
                aggregation_bucket_size=6,
                metric="credits",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            start_unix=start_unix,
            end_unix=end_unix,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_workspace_metrics": include_workspace_metrics,
                        "breakdown_type": breakdown_type,
                        "aggregation_interval": aggregation_interval,
                        "aggregation_bucket_size": aggregation_bucket_size,
                        "metric": metric,
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

    async def get(
        self,
        *,
        start_unix: int,
        end_unix: int,
        include_workspace_metrics: Union[bool, None] = SENTINEL,
        breakdown_type: Union[BreakdownTypes, None] = SENTINEL,
        aggregation_interval: Union[UsageAggregationInterval, None] = SENTINEL,
        aggregation_bucket_size: Union[int, None] = SENTINEL,
        metric: Union[MetricType, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[UsageCharactersResponseModel]:
        data = await AsyncUsageClient.get(
            self._client,
            start_unix=start_unix,
            end_unix=end_unix,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_workspace_metrics": include_workspace_metrics,
                        "breakdown_type": breakdown_type,
                        "aggregation_interval": aggregation_interval,
                        "aggregation_bucket_size": aggregation_bucket_size,
                        "metric": metric,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
