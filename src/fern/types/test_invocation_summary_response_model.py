from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .resource_access_info import ResourceAccessInfo


class TestInvocationSummaryResponseModel(BaseModel):
    """TestInvocationSummaryResponseModel

    :param id: The ID of the test invocation
    :type id: str
    :param agent_id: The ID of the agent this test invocation belongs to, defaults to None
    :type agent_id: str, optional
    :param branch_id: The ID of the branch this test invocation was run on, defaults to None
    :type branch_id: str, optional
    :param created_at_unix_secs: Creation time of the test invocation in unix seconds
    :type created_at_unix_secs: int
    :param test_run_count: Number of test runs in this invocation
    :type test_run_count: int
    :param passed_count: Number of test runs that passed
    :type passed_count: int
    :param failed_count: Number of test runs that failed
    :type failed_count: int
    :param pending_count: Number of test runs that are pending
    :type pending_count: int
    :param title: Title of the test invocation - either the single test name or count of tests
    :type title: str
    :param access_info: The access information of the test invocation, defaults to None
    :type access_info: ResourceAccessInfo, optional
    :param repeat_count: Number of times each test was repeated in this invocation, defaults to None
    :type repeat_count: int, optional
    """

    id: str = Field(description="The ID of the test invocation")
    agent_id: Optional[str] = Field(
        default=None, description="The ID of the agent this test invocation belongs to"
    )
    branch_id: Optional[str] = Field(
        default=None, description="The ID of the branch this test invocation was run on"
    )
    created_at_unix_secs: int = Field(
        description="Creation time of the test invocation in unix seconds"
    )
    test_run_count: int = Field(description="Number of test runs in this invocation")
    passed_count: int = Field(description="Number of test runs that passed")
    failed_count: int = Field(description="Number of test runs that failed")
    pending_count: int = Field(description="Number of test runs that are pending")
    title: str = Field(
        description="Title of the test invocation - either the single test name or count of tests"
    )
    access_info: Optional[ResourceAccessInfo] = Field(
        default=None, description="The access information of the test invocation"
    )
    repeat_count: Optional[int] = Field(
        default=None,
        description="Number of times each test was repeated in this invocation",
    )
