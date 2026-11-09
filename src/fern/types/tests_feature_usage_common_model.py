from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TestsFeatureUsageCommonModel(BaseModel):
    """TestsFeatureUsageCommonModel

    :param enabled: enabled, defaults to None
    :type enabled: bool, optional
    :param tests_ran_after_last_modification: tests_ran_after_last_modification, defaults to None
    :type tests_ran_after_last_modification: bool, optional
    :param tests_ran_in_last_7_days: tests_ran_in_last_7_days, defaults to None
    :type tests_ran_in_last_7_days: bool, optional
    """

    enabled: Optional[bool] = Field(default=None)
    tests_ran_after_last_modification: Optional[bool] = Field(default=None)
    tests_ran_in_last_7_days: Optional[bool] = Field(default=None)
