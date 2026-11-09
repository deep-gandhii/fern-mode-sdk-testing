from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class NumericDistributionAggregate(BaseModel):
    """NumericDistributionAggregate

    :param count: count, defaults to None
    :type count: int, optional
    :param sum: sum, defaults to None
    :type sum: float, optional
    :param min: min, defaults to None
    :type min: float, optional
    :param max: max, defaults to None
    :type max: float, optional
    """

    count: Optional[int] = Field(default=None)
    sum: Optional[float] = Field(default=None)
    min: Optional[float] = Field(default=None)
    max: Optional[float] = Field(default=None)
