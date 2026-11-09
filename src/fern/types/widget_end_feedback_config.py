from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .widget_end_feedback_type import WidgetEndFeedbackType


class WidgetEndFeedbackConfig(BaseModel):
    """WidgetEndFeedbackConfig

    :param type: type, defaults to None
    :type type: WidgetEndFeedbackType, optional
    """

    type: Optional[WidgetEndFeedbackType] = Field(default=None)
