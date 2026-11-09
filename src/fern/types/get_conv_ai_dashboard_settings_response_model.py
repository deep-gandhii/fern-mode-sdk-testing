from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .dashboard_call_success_chart_model import DashboardCallSuccessChartModel
from .dashboard_criteria_chart_model import DashboardCriteriaChartModel
from .dashboard_data_collection_chart_model import DashboardDataCollectionChartModel


# fernMode variant type for a shared-component member of GetConvAiDashboardSettingsResponseModelChartsItem
class GetConvAiDashboardSettingsResponseModelChartsItem_CallSuccess(
    DashboardCallSuccessChartModel
):
    pass


# fernMode variant type for a shared-component member of GetConvAiDashboardSettingsResponseModelChartsItem
class GetConvAiDashboardSettingsResponseModelChartsItem_Criteria(
    DashboardCriteriaChartModel
):
    pass


# fernMode variant type for a shared-component member of GetConvAiDashboardSettingsResponseModelChartsItem
class GetConvAiDashboardSettingsResponseModelChartsItem_DataCollection(
    DashboardDataCollectionChartModel
):
    pass


# Union type for GetConvAiDashboardSettingsResponseModelChartsItem
# Pydantic will attempt to validate against each type in order
GetConvAiDashboardSettingsResponseModelChartsItem = Union[
    DashboardCallSuccessChartModel,
    DashboardCriteriaChartModel,
    DashboardDataCollectionChartModel,
]
# TypeAdapter for runtime validation of GetConvAiDashboardSettingsResponseModelChartsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

GetConvAiDashboardSettingsResponseModelChartsItem_adapter = TypeAdapter(
    GetConvAiDashboardSettingsResponseModelChartsItem
)


class GetConvAiDashboardSettingsResponseModel(BaseModel):
    """GetConvAiDashboardSettingsResponseModel

    :param charts: charts, defaults to None
    :type charts: List[GetConvAiDashboardSettingsResponseModelChartsItem], optional
    """

    charts: Optional[List[GetConvAiDashboardSettingsResponseModelChartsItem]] = Field(
        default=None
    )
