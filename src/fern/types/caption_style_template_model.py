from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CaptionStyleTemplateModel(BaseModel):
    """CaptionStyleTemplateModel

    :param key: key
    :type key: str
    :param label: label
    :type label: str
    :param requires_high_fps: requires_high_fps, defaults to None
    :type requires_high_fps: bool, optional
    """

    key: str
    label: str
    requires_high_fps: Optional[bool] = Field(default=None)
