from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SystemEvaluationCriteria(BaseModel):
    """SystemEvaluationCriteria

    :param user_sentiment_score: user_sentiment_score
    :type user_sentiment_score: float
    :param user_frustration_score: user_frustration_score
    :type user_frustration_score: float
    """

    user_sentiment_score: float
    user_frustration_score: float
