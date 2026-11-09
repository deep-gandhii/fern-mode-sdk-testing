from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SpeechToTextCharacterResponseModel(BaseModel):
    """SpeechToTextCharacterResponseModel

    :param text: The character that was transcribed.
    :type text: str
    :param start: The start time of the character in seconds., defaults to None
    :type start: float, optional
    :param end: The end time of the character in seconds., defaults to None
    :type end: float, optional
    """

    text: str = Field(description="The character that was transcribed.")
    start: Optional[float] = Field(
        default=None, description="The start time of the character in seconds."
    )
    end: Optional[float] = Field(
        default=None, description="The end time of the character in seconds."
    )
