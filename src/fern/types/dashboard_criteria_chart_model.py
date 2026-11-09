from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DashboardCriteriaChartModelType = typing.Union[typing.Literal["criteria"], typing.Any]


class DashboardCriteriaChartModel(BaseModel):
    """DashboardCriteriaChartModel

    :param name: name
    :type name: str
    :param type: type, defaults to None
    :type type: DashboardCriteriaChartModelType, optional
    :param criteria_id: criteria_id
    :type criteria_id: str
    """

    name: str
    type: Optional[DashboardCriteriaChartModelType] = Field(default=None)
    criteria_id: str
