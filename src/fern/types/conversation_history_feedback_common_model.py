from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_feedback_type import ConversationFeedbackType
from .user_feedback_score import UserFeedbackScore


class ConversationHistoryFeedbackCommonModel(BaseModel):
    """ConversationHistoryFeedbackCommonModel

    :param type: type, defaults to None
    :type type: ConversationFeedbackType, optional
    :param overall_score: overall_score, defaults to None
    :type overall_score: UserFeedbackScore, optional
    :param likes: likes, defaults to None
    :type likes: int, optional
    :param dislikes: dislikes, defaults to None
    :type dislikes: int, optional
    :param rating: rating, defaults to None
    :type rating: int, optional
    :param comment: comment, defaults to None
    :type comment: str, optional
    """

    type: Optional[ConversationFeedbackType] = Field(default=None)
    overall_score: Optional[UserFeedbackScore] = Field(default=None)
    likes: Optional[int] = Field(default=None)
    dislikes: Optional[int] = Field(default=None)
    rating: Optional[int] = Field(default=None)
    comment: Optional[str] = Field(default=None)
