from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ThresholdGuardrail(BaseModel):
    """ThresholdGuardrail

    :param is_enabled: is_enabled, defaults to None
    :type is_enabled: bool, optional
    :param threshold: threshold, defaults to None
    :type threshold: float, optional
    """

    is_enabled: Optional[bool] = Field(default=None)
    threshold: Optional[float] = Field(default=None)
