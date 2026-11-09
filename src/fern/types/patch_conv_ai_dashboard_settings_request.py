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


# fernMode variant type for a shared-component member of PatchConvAiDashboardSettingsRequestChartsItem
class PatchConvAiDashboardSettingsRequestChartsItem_CallSuccess(
    DashboardCallSuccessChartModel
):
    pass


# fernMode variant type for a shared-component member of PatchConvAiDashboardSettingsRequestChartsItem
class PatchConvAiDashboardSettingsRequestChartsItem_Criteria(
    DashboardCriteriaChartModel
):
    pass


# fernMode variant type for a shared-component member of PatchConvAiDashboardSettingsRequestChartsItem
class PatchConvAiDashboardSettingsRequestChartsItem_DataCollection(
    DashboardDataCollectionChartModel
):
    pass


# Union type for PatchConvAiDashboardSettingsRequestChartsItem
# Pydantic will attempt to validate against each type in order
PatchConvAiDashboardSettingsRequestChartsItem = Union[
    DashboardCallSuccessChartModel,
    DashboardCriteriaChartModel,
    DashboardDataCollectionChartModel,
]
# TypeAdapter for runtime validation of PatchConvAiDashboardSettingsRequestChartsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PatchConvAiDashboardSettingsRequestChartsItem_adapter = TypeAdapter(
    PatchConvAiDashboardSettingsRequestChartsItem
)


class PatchConvAiDashboardSettingsRequest(BaseModel):
    """PatchConvAiDashboardSettingsRequest

    :param charts: charts, defaults to None
    :type charts: List[PatchConvAiDashboardSettingsRequestChartsItem], optional
    """

    charts: Optional[List[PatchConvAiDashboardSettingsRequestChartsItem]] = Field(
        default=None
    )
