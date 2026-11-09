from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PositionInput(BaseModel):
    """PositionInput

    :param x: x, defaults to None
    :type x: float, optional
    :param y: y, defaults to None
    :type y: float, optional
    """

    x: Optional[float] = Field(default=None)
    y: Optional[float] = Field(default=None)
