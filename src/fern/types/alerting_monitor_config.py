from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AlertingMonitorConfig(BaseModel):
    """AlertingMonitorConfig

    :param threshold: Failure rate threshold at which this monitor can notify., defaults to None
    :type threshold: float, optional
    :param auto_resolve_after_inactive_minutes: How many minutes an alert can stay inactive before it is auto-resolved., defaults to None
    :type auto_resolve_after_inactive_minutes: int, optional
    """

    threshold: Optional[float] = Field(
        default=None,
        description="Failure rate threshold at which this monitor can notify.",
    )
    auto_resolve_after_inactive_minutes: Optional[int] = Field(
        default=None,
        description="How many minutes an alert can stay inactive before it is auto-resolved.",
    )
