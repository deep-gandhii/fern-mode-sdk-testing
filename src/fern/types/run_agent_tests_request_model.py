from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .single_test_run_request_model import SingleTestRunRequestModel
from .adhoc_agent_config_override_for_test_request_model import (
    AdhocAgentConfigOverrideForTestRequestModel,
)


class RunAgentTestsRequestModel(BaseModel):
    """RunAgentTestsRequestModel

    :param tests: List of tests to run on the agent
    :type tests: List[SingleTestRunRequestModel]
    :param agent_config_override: Configuration overrides to use for testing. If not provided, the agent's default configuration will be used., defaults to None
    :type agent_config_override: AdhocAgentConfigOverrideForTestRequestModel, optional
    :param branch_id: ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch., defaults to None
    :type branch_id: str, optional
    :param repeat_count: Number of times to run each test. When greater than 1, results are grouped and summarized., defaults to None
    :type repeat_count: int, optional
    """

    tests: List[SingleTestRunRequestModel] = Field(
        description="List of tests to run on the agent"
    )
    agent_config_override: Optional[AdhocAgentConfigOverrideForTestRequestModel] = (
        Field(
            default=None,
            description="Configuration overrides to use for testing. If not provided, the agent's default configuration will be used.",
        )
    )
    branch_id: Optional[str] = Field(
        default=None,
        description="ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch.",
    )
    repeat_count: Optional[int] = Field(
        default=None,
        description="Number of times to run each test. When greater than 1, results are grouped and summarized.",
    )
