from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SafetyResponseModel(BaseModel):
    """SafetyResponseModel

    :param is_blocked_ivc: is_blocked_ivc, defaults to None
    :type is_blocked_ivc: bool, optional
    :param is_blocked_non_ivc: is_blocked_non_ivc, defaults to None
    :type is_blocked_non_ivc: bool, optional
    :param ignore_safety_evaluation: ignore_safety_evaluation, defaults to None
    :type ignore_safety_evaluation: bool, optional
    """

    is_blocked_ivc: Optional[bool] = Field(default=None)
    is_blocked_non_ivc: Optional[bool] = Field(default=None)
    ignore_safety_evaluation: Optional[bool] = Field(default=None)
