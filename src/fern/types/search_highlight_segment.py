from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SearchHighlightSegment(BaseModel):
    """SearchHighlightSegment

    :param value: value
    :type value: str
    :param is_hit: is_hit
    :type is_hit: bool
    """

    value: str
    is_hit: bool
