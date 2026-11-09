from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .user_feedback_score import UserFeedbackScore


class ConversationFeedbackRequestModel(BaseModel):
    """ConversationFeedbackRequestModel

    :param feedback: Either 'like' or 'dislike' to indicate the feedback for the conversation., defaults to None
    :type feedback: UserFeedbackScore, optional
    """

    feedback: Optional[UserFeedbackScore] = Field(
        default=None,
        description="Either 'like' or 'dislike' to indicate the feedback for the conversation.",
    )
