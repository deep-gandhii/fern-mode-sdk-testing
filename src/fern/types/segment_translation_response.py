from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SegmentTranslationResponse(BaseModel):
    """SegmentTranslationResponse

    :param version: version
    :type version: int
    """

    version: int
