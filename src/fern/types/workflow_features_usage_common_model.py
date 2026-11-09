from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .feature_status_common_model import FeatureStatusCommonModel


class WorkflowFeaturesUsageCommonModel(BaseModel):
    """WorkflowFeaturesUsageCommonModel

    :param enabled: enabled, defaults to None
    :type enabled: bool, optional
    :param tool_node: tool_node, defaults to None
    :type tool_node: FeatureStatusCommonModel, optional
    :param standalone_agent_node: standalone_agent_node, defaults to None
    :type standalone_agent_node: FeatureStatusCommonModel, optional
    :param phone_number_node: phone_number_node, defaults to None
    :type phone_number_node: FeatureStatusCommonModel, optional
    :param end_node: end_node, defaults to None
    :type end_node: FeatureStatusCommonModel, optional
    """

    enabled: Optional[bool] = Field(default=None)
    tool_node: Optional[FeatureStatusCommonModel] = Field(default=None)
    standalone_agent_node: Optional[FeatureStatusCommonModel] = Field(default=None)
    phone_number_node: Optional[FeatureStatusCommonModel] = Field(default=None)
    end_node: Optional[FeatureStatusCommonModel] = Field(default=None)
