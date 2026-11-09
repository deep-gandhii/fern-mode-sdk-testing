from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class LlmTokensCategoryUsage(BaseModel):
    """LlmTokensCategoryUsage

    :param tokens: tokens, defaults to None
    :type tokens: int, optional
    :param price: price, defaults to None
    :type price: float, optional
    """

    tokens: Optional[int] = Field(default=None)
    price: Optional[float] = Field(default=None)
