from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SegmentUpdatePayload(BaseModel):
    """SegmentUpdatePayload

    :param start_time: start_time, defaults to None
    :type start_time: float, optional
    :param end_time: end_time, defaults to None
    :type end_time: float, optional
    :param text: text, defaults to None
    :type text: str, optional
    """

    start_time: Optional[float] = Field(default=None)
    end_time: Optional[float] = Field(default=None)
    text: Optional[str] = Field(default=None)
