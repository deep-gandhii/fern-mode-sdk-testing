from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .unit_test_summary_response_model import UnitTestSummaryResponseModel


class GetTestsPageResponseModel(BaseModel):
    """GetTestsPageResponseModel

    :param tests: tests
    :type tests: List[UnitTestSummaryResponseModel]
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    :param has_more: has_more
    :type has_more: bool
    """

    tests: List[UnitTestSummaryResponseModel]
    next_cursor: Optional[str] = Field(default=None)
    has_more: bool
