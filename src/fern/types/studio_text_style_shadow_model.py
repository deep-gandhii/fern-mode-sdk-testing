from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class StudioTextStyleShadowModel(BaseModel):
    """StudioTextStyleShadowModel

    :param enabled: enabled
    :type enabled: bool
    :param color: color
    :type color: str
    :param opacity: opacity
    :type opacity: float
    :param blur: blur
    :type blur: float
    :param offset_x: offset_x
    :type offset_x: float
    :param offset_y: offset_y
    :type offset_y: float
    """

    enabled: bool
    color: str
    opacity: float
    blur: float
    offset_x: float
    offset_y: float
