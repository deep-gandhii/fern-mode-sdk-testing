from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranscriptionWordType = typing.Union[typing.Literal["word", "spacing"], typing.Any]


class TranscriptionWord(BaseModel):
    """Word-level transcription data with timing information.

    :param text: The transcribed word., defaults to None
    :type text: str, optional
    :param start: Start time in seconds., defaults to None
    :type start: float, optional
    :param end: End time in seconds., defaults to None
    :type end: float, optional
    :param type: The type of word., defaults to None
    :type type: TranscriptionWordType, optional
    :param speaker_id: The ID of the speaker if available., defaults to None
    :type speaker_id: str, optional
    :param logprob: Confidence score for this word., defaults to None
    :type logprob: float, optional
    :param characters: The characters in the word., defaults to None
    :type characters: List[str], optional
    """

    text: Optional[str] = Field(default=None, description="The transcribed word.")
    start: Optional[float] = Field(default=None, description="Start time in seconds.")
    end: Optional[float] = Field(default=None, description="End time in seconds.")
    type: Optional[TranscriptionWordType] = Field(
        default=None, description="The type of word."
    )
    speaker_id: Optional[str] = Field(
        default=None, description="The ID of the speaker if available."
    )
    logprob: Optional[float] = Field(
        default=None, description="Confidence score for this word."
    )
    characters: Optional[List[str]] = Field(
        default=None, description="The characters in the word."
    )
