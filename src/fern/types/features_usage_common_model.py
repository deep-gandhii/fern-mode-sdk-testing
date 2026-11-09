from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .feature_status_common_model import FeatureStatusCommonModel
from .workflow_features_usage_common_model import WorkflowFeaturesUsageCommonModel
from .tests_feature_usage_common_model import TestsFeatureUsageCommonModel


class FeaturesUsageCommonModel(BaseModel):
    """FeaturesUsageCommonModel

    :param language_detection: language_detection, defaults to None
    :type language_detection: FeatureStatusCommonModel, optional
    :param transfer_to_agent: transfer_to_agent, defaults to None
    :type transfer_to_agent: FeatureStatusCommonModel, optional
    :param transfer_to_number: transfer_to_number, defaults to None
    :type transfer_to_number: FeatureStatusCommonModel, optional
    :param multivoice: multivoice, defaults to None
    :type multivoice: FeatureStatusCommonModel, optional
    :param dtmf_tones: dtmf_tones, defaults to None
    :type dtmf_tones: FeatureStatusCommonModel, optional
    :param external_mcp_servers: external_mcp_servers, defaults to None
    :type external_mcp_servers: FeatureStatusCommonModel, optional
    :param pii_zrm_workspace: pii_zrm_workspace, defaults to None
    :type pii_zrm_workspace: bool, optional
    :param pii_zrm_agent: pii_zrm_agent, defaults to None
    :type pii_zrm_agent: bool, optional
    :param tool_dynamic_variable_updates: tool_dynamic_variable_updates, defaults to None
    :type tool_dynamic_variable_updates: FeatureStatusCommonModel, optional
    :param is_livekit: is_livekit, defaults to None
    :type is_livekit: bool, optional
    :param voicemail_detection: voicemail_detection, defaults to None
    :type voicemail_detection: FeatureStatusCommonModel, optional
    :param dtmf_input: dtmf_input, defaults to None
    :type dtmf_input: FeatureStatusCommonModel, optional
    :param workflow: workflow, defaults to None
    :type workflow: WorkflowFeaturesUsageCommonModel, optional
    :param agent_testing: agent_testing, defaults to None
    :type agent_testing: TestsFeatureUsageCommonModel, optional
    :param versioning: versioning, defaults to None
    :type versioning: FeatureStatusCommonModel, optional
    :param file_input: file_input, defaults to None
    :type file_input: FeatureStatusCommonModel, optional
    """

    language_detection: Optional[FeatureStatusCommonModel] = Field(default=None)
    transfer_to_agent: Optional[FeatureStatusCommonModel] = Field(default=None)
    transfer_to_number: Optional[FeatureStatusCommonModel] = Field(default=None)
    multivoice: Optional[FeatureStatusCommonModel] = Field(default=None)
    dtmf_tones: Optional[FeatureStatusCommonModel] = Field(default=None)
    external_mcp_servers: Optional[FeatureStatusCommonModel] = Field(default=None)
    pii_zrm_workspace: Optional[bool] = Field(default=None)
    pii_zrm_agent: Optional[bool] = Field(default=None)
    tool_dynamic_variable_updates: Optional[FeatureStatusCommonModel] = Field(
        default=None
    )
    is_livekit: Optional[bool] = Field(default=None)
    voicemail_detection: Optional[FeatureStatusCommonModel] = Field(default=None)
    dtmf_input: Optional[FeatureStatusCommonModel] = Field(default=None)
    workflow: Optional[WorkflowFeaturesUsageCommonModel] = Field(default=None)
    agent_testing: Optional[TestsFeatureUsageCommonModel] = Field(default=None)
    versioning: Optional[FeatureStatusCommonModel] = Field(default=None)
    file_input: Optional[FeatureStatusCommonModel] = Field(default=None)
