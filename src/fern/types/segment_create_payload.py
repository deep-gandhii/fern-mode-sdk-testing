from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel


class SegmentCreatePayload(BaseModel):
    """SegmentCreatePayload

    :param start_time: start_time
    :type start_time: float
    :param end_time: end_time
    :type end_time: float
    :param text: text, defaults to None
    :type text: str, optional
    :param translations: translations, defaults to None
    :type translations: Dict[str, str], optional
    """

    start_time: float
    end_time: float
    text: Optional[str] = Field(default=None)
    translations: Optional[Dict[str, str]] = Field(default=None)
