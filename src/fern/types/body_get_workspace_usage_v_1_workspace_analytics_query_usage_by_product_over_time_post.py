from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .column_filter import ColumnFilter

BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem = (
    typing.Union[
        typing.Literal[
            "product_type",
            "model",
            "voice_id",
            "user_id",
            "fiat_currency",
            "fiat_charge_type",
            "region",
            "reporting_workspace_id",
            "request_source",
            "resource_id",
            "subresource_id",
            "request_queue_type",
            "voice_multiplier",
            "hashed_xi_api_key",
            "billing_group_id",
            "surface",
            "actor",
        ],
        typing.Any,
    ]
)


class BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePost(
    BaseModel
):
    """BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePost

    :param start_time: Start of the time range as a Unix timestamp in milliseconds. Must be at least 2020-01-01.
    :type start_time: int
    :param end_time: End of the time range as a Unix timestamp in milliseconds. Must be at least 2020-01-01.
    :type end_time: int
    :param interval_seconds: Bucket size in seconds. Each row in the response covers this many seconds of the selected time range. For example, pass 3600 for hourly buckets or 86400 for daily buckets. Whether `time_zone` shifts bucket boundaries depends on this value: whole-day multiples (e.g. 86400) align to local midnight; whole-hour multiples up to 24 hours (e.g. 3600, 14400) align to local hour boundaries from midnight; sub-hour values and other sizes remain UTC-anchored regardless of `time_zone`., defaults to None
    :type interval_seconds: int, optional
    :param group_by: group_by, defaults to None
    :type group_by: List[BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem], optional
    :param filters: filters, defaults to None
    :type filters: List[ColumnFilter], optional
    :param time_zone: IANA time zone identifier (e.g. 'America/New_York', 'Europe/London', 'UTC') used to align bucket boundaries for eligible `interval_seconds` values. Whole-day multiples start at local midnight; whole-hour multiples up to 24 hours align to local hour boundaries from midnight. Sub-hour intervals and other bucket sizes remain UTC-anchored regardless of this setting. Defaults to UTC., defaults to None
    :type time_zone: str, optional
    """

    start_time: int = Field(
        description="Start of the time range as a Unix timestamp in milliseconds. Must be at least 2020-01-01."
    )
    end_time: int = Field(
        description="End of the time range as a Unix timestamp in milliseconds. Must be at least 2020-01-01."
    )
    interval_seconds: Optional[int] = Field(
        default=None,
        description="Bucket size in seconds. Each row in the response covers this many seconds of the selected time range. For example, pass 3600 for hourly buckets or 86400 for daily buckets. Whether `time_zone` shifts bucket boundaries depends on this value: whole-day multiples (e.g. 86400) align to local midnight; whole-hour multiples up to 24 hours (e.g. 3600, 14400) align to local hour boundaries from midnight; sub-hour values and other sizes remain UTC-anchored regardless of `time_zone`.",
    )
    group_by: Optional[
        List[
            BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItem
        ]
    ] = Field(default=None)
    filters: Optional[List[ColumnFilter]] = Field(default=None)
    time_zone: Optional[str] = Field(
        default=None,
        description="IANA time zone identifier (e.g. 'America/New_York', 'Europe/London', 'UTC') used to align bucket boundaries for eligible `interval_seconds` values. Whole-day multiples start at local midnight; whole-hour multiples up to 24 hours align to local hour boundaries from midnight. Sub-hour intervals and other bucket sizes remain UTC-anchored regardless of this setting. Defaults to UTC.",
    )
