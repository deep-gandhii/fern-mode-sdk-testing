from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ListTestsByIdsRequestModel(BaseModel):
    """ListTestsByIdsRequestModel

    :param test_ids: List of test IDs to fetch. No duplicates allowed. Prefer at most 1000 IDs per request.
    :type test_ids: List[str]
    """

    test_ids: List[str] = Field(
        description="List of test IDs to fetch. No duplicates allowed. Prefer at most 1000 IDs per request."
    )
