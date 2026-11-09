from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .user_feedback_score import UserFeedbackScore


class UserFeedback(BaseModel):
    """UserFeedback

    :param score: score
    :type score: UserFeedbackScore
    :param time_in_call_secs: time_in_call_secs
    :type time_in_call_secs: int
    """

    score: UserFeedbackScore
    time_in_call_secs: int
