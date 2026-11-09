from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class UtteranceResponseModel(BaseModel):
    """UtteranceResponseModel

    :param start: The start time of the utterance in seconds.
    :type start: float
    :param end: The end time of the utterance in seconds.
    :type end: float
    """

    start: float = Field(description="The start time of the utterance in seconds.")
    end: float = Field(description="The end time of the utterance in seconds.")
