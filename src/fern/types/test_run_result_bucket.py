from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .test_run_status import TestRunStatus


class TestRunResultBucket(BaseModel):
    """TestRunResultBucket

    :param test_run_ids: test_run_ids
    :type test_run_ids: List[str]
    :param title: Short one-line title for this bucket
    :type title: str
    :param reason: Short summary of why the test runs in this bucket passed or failed
    :type reason: str
    :param status: status
    :type status: TestRunStatus
    """

    test_run_ids: List[str]
    title: str = Field(description="Short one-line title for this bucket")
    reason: str = Field(
        description="Short summary of why the test runs in this bucket passed or failed"
    )
    status: TestRunStatus
