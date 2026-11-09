from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DashboardCallSuccessChartModelType = typing.Union[
    typing.Literal["call_success"], typing.Any
]


class DashboardCallSuccessChartModel(BaseModel):
    """DashboardCallSuccessChartModel

    :param name: name
    :type name: str
    :param type: type, defaults to None
    :type type: DashboardCallSuccessChartModelType, optional
    """

    name: str
    type: Optional[DashboardCallSuccessChartModelType] = Field(default=None)
