from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class MetricRecord(BaseModel):
    """MetricRecord

    :param elapsed_time: elapsed_time
    :type elapsed_time: float
    """

    elapsed_time: float
