from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PlatformCategoryUsage(BaseModel):
    """Accumulated charge for a single :class:`PlatformCategory`.

    :param credits: credits, defaults to None
    :type credits: int, optional
    :param price: price, defaults to None
    :type price: float, optional
    :param quantity: quantity, defaults to None
    :type quantity: float, optional
    """

    credits: Optional[int] = Field(default=None)
    price: Optional[float] = Field(default=None)
    quantity: Optional[float] = Field(default=None)
