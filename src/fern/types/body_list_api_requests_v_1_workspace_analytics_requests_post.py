from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .column_filter import ColumnFilter

BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort = typing.Union[
    typing.Literal["asc", "desc"], typing.Any
]


class BodyListApiRequestsV1WorkspaceAnalyticsRequestsPost(BaseModel):
    """BodyListApiRequestsV1WorkspaceAnalyticsRequestsPost

    :param start_time: Start of the time range as a Unix timestamp in milliseconds., defaults to None
    :type start_time: int, optional
    :param end_time: End of the time range as a Unix timestamp in milliseconds., defaults to None
    :type end_time: int, optional
    :param limit: limit, defaults to None
    :type limit: int, optional
    :param sort: Optional timestamp sort direction. If omitted, defaults to desc when end_time is provided, otherwise asc., defaults to None
    :type sort: BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort, optional
    :param filters: filters, defaults to None
    :type filters: List[ColumnFilter], optional
    :param search: search, defaults to None
    :type search: str, optional
    """

    start_time: Optional[int] = Field(
        default=None,
        description="Start of the time range as a Unix timestamp in milliseconds.",
    )
    end_time: Optional[int] = Field(
        default=None,
        description="End of the time range as a Unix timestamp in milliseconds.",
    )
    limit: Optional[int] = Field(default=None)
    sort: Optional[BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort] = Field(
        default=None,
        description="Optional timestamp sort direction. If omitted, defaults to desc when end_time is provided, otherwise asc.",
    )
    filters: Optional[List[ColumnFilter]] = Field(default=None)
    search: Optional[str] = Field(default=None)
