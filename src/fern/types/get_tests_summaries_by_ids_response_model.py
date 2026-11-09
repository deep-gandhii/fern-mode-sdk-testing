from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .unit_test_summary_response_model import UnitTestSummaryResponseModel


class GetTestsSummariesByIdsResponseModel(BaseModel):
    """GetTestsSummariesByIdsResponseModel

    :param tests: Dictionary mapping test IDs to their summary information
    :type tests: Dict[str, UnitTestSummaryResponseModel]
    """

    tests: Dict[str, UnitTestSummaryResponseModel] = Field(
        description="Dictionary mapping test IDs to their summary information"
    )
