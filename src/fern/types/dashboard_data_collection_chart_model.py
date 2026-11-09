from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DashboardDataCollectionChartModelType = typing.Union[
    typing.Literal["data_collection"], typing.Any
]


class DashboardDataCollectionChartModel(BaseModel):
    """DashboardDataCollectionChartModel

    :param name: name
    :type name: str
    :param type: type, defaults to None
    :type type: DashboardDataCollectionChartModelType, optional
    :param data_collection_id: data_collection_id
    :type data_collection_id: str
    """

    name: str
    type: Optional[DashboardDataCollectionChartModelType] = Field(default=None)
    data_collection_id: str
