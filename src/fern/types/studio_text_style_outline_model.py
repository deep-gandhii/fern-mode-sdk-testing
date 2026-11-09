from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class StudioTextStyleOutlineModel(BaseModel):
    """StudioTextStyleOutlineModel

    :param enabled: enabled
    :type enabled: bool
    :param color: color
    :type color: str
    :param opacity: opacity
    :type opacity: float
    :param width: width
    :type width: float
    """

    enabled: bool
    color: str
    opacity: float
    width: float
