from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SegmentSubtitleFrame(BaseModel):
    """SegmentSubtitleFrame

    :param start_time: start_time
    :type start_time: float
    :param end_time: end_time
    :type end_time: float
    :param lines: lines
    :type lines: List[str]
    """

    start_time: float
    end_time: float
    lines: List[str]
