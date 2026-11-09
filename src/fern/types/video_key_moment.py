from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class VideoKeyMoment(BaseModel):
    """VideoKeyMoment

    :param timestamp_ms: timestamp_ms
    :type timestamp_ms: int
    :param type: type
    :type type: str
    :param description: description
    :type description: str
    """

    timestamp_ms: int
    type: str
    description: str
