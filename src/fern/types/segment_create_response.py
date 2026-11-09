from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SegmentCreateResponse(BaseModel):
    """SegmentCreateResponse

    :param version: version
    :type version: int
    :param new_segment: new_segment
    :type new_segment: str
    """

    version: int
    new_segment: str
