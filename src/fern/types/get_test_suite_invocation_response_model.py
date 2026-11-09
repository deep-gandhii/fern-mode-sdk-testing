from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .bucketing_status import BucketingStatus
from .test_run_result_summary import TestRunResultSummary
from .unit_test_run_response_model import UnitTestRunResponseModel


class GetTestSuiteInvocationResponseModel(BaseModel):
    """GetTestSuiteInvocationResponseModel

    :param id: id
    :type id: str
    :param agent_id: agent_id, defaults to None
    :type agent_id: str, optional
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    :param created_at: created_at, defaults to None
    :type created_at: int, optional
    :param folder_id: folder_id, defaults to None
    :type folder_id: str, optional
    :param repeat_count: repeat_count, defaults to None
    :type repeat_count: int, optional
    :param bucketing_status: None when repeat_count==1 (no bucketing). Otherwise tracks bucketing lifecycle., defaults to None
    :type bucketing_status: BucketingStatus, optional
    :param result_groups: result_groups, defaults to None
    :type result_groups: List[TestRunResultSummary], optional
    :param test_runs: test_runs
    :type test_runs: List[UnitTestRunResponseModel]
    """

    id: str
    agent_id: Optional[str] = Field(default=None)
    branch_id: Optional[str] = Field(default=None)
    created_at: Optional[int] = Field(default=None)
    folder_id: Optional[str] = Field(default=None)
    repeat_count: Optional[int] = Field(default=None)
    bucketing_status: Optional[BucketingStatus] = Field(
        default=None,
        description="None when repeat_count==1 (no bucketing). Otherwise tracks bucketing lifecycle.",
    )
    result_groups: Optional[List[TestRunResultSummary]] = Field(default=None)
    test_runs: List[UnitTestRunResponseModel]
