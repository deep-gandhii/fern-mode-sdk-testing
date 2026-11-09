from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ToolUsageStatsResponseModel(BaseModel):
    """ToolUsageStatsResponseModel

    :param total_calls: The total number of calls to the tool, defaults to None
    :type total_calls: int, optional
    :param avg_latency_secs: avg_latency_secs
    :type avg_latency_secs: float
    """

    total_calls: Optional[int] = Field(
        default=None, description="The total number of calls to the tool"
    )
    avg_latency_secs: float
