from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PositionOutput(BaseModel):
    """PositionOutput

    :param x: x
    :type x: float
    :param y: y
    :type y: float
    """

    x: float
    y: float
