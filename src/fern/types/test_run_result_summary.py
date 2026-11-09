from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .test_run_result_bucket import TestRunResultBucket


class TestRunResultSummary(BaseModel):
    """TestRunResultSummary

    :param test_id: test_id
    :type test_id: str
    :param test_name: test_name
    :type test_name: str
    :param workflow_node_id: workflow_node_id, defaults to None
    :type workflow_node_id: str, optional
    :param buckets: buckets
    :type buckets: List[TestRunResultBucket]
    """

    test_id: str
    test_name: str
    workflow_node_id: Optional[str] = Field(default=None)
    buckets: List[TestRunResultBucket]
