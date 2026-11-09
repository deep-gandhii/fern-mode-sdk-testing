from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .adhoc_agent_config_override_for_test_request_model import (
    AdhocAgentConfigOverrideForTestRequestModel,
)


class ResubmitTestsRequestModel(BaseModel):
    """ResubmitTestsRequestModel

    :param test_run_ids: List of test run IDs to resubmit
    :type test_run_ids: List[str]
    :param agent_config_override: Configuration overrides to use for testing. If not provided, the agent's default configuration will be used., defaults to None
    :type agent_config_override: AdhocAgentConfigOverrideForTestRequestModel, optional
    :param agent_id: Agent ID to resubmit tests for
    :type agent_id: str
    :param branch_id: ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch., defaults to None
    :type branch_id: str, optional
    """

    test_run_ids: List[str] = Field(description="List of test run IDs to resubmit")
    agent_config_override: Optional[AdhocAgentConfigOverrideForTestRequestModel] = (
        Field(
            default=None,
            description="Configuration overrides to use for testing. If not provided, the agent's default configuration will be used.",
        )
    )
    agent_id: str = Field(description="Agent ID to resubmit tests for")
    branch_id: Optional[str] = Field(
        default=None,
        description="ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch.",
    )
