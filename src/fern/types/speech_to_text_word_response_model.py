from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .speech_to_text_character_response_model import SpeechToTextCharacterResponseModel

SpeechToTextWordResponseModelType = typing.Union[
    typing.Literal["word", "spacing", "audio_event"], typing.Any
]


class SpeechToTextWordResponseModel(BaseModel):
    """Word-level detail of the transcription with timing information.

    :param text: The word or sound that was transcribed.
    :type text: str
    :param start: The start time of the word or sound in seconds., defaults to None
    :type start: float, optional
    :param end: The end time of the word or sound in seconds., defaults to None
    :type end: float, optional
    :param type: The type of the word or sound. 'audio_event' is used for non-word sounds like laughter or footsteps.
    :type type: SpeechToTextWordResponseModelType
    :param speaker_id: Unique identifier for the speaker of this word., defaults to None
    :type speaker_id: str, optional
    :param logprob: The log of the probability with which this word was predicted. Logprobs are in range [-infinity, 0], higher logprobs indicate a higher confidence the model has in its predictions.
    :type logprob: float
    :param characters: The characters that make up the word and their timing information., defaults to None
    :type characters: List[SpeechToTextCharacterResponseModel], optional
    :param channel_index: The channel this word was spoken on (for multichannel audio). Null for single-channel transcriptions., defaults to None
    :type channel_index: int, optional
    """

    text: str = Field(description="The word or sound that was transcribed.")
    start: Optional[float] = Field(
        default=None, description="The start time of the word or sound in seconds."
    )
    end: Optional[float] = Field(
        default=None, description="The end time of the word or sound in seconds."
    )
    type: SpeechToTextWordResponseModelType = Field(
        description="The type of the word or sound. 'audio_event' is used for non-word sounds like laughter or footsteps."
    )
    speaker_id: Optional[str] = Field(
        default=None, description="Unique identifier for the speaker of this word."
    )
    logprob: float = Field(
        description="The log of the probability with which this word was predicted. Logprobs are in range [-infinity, 0], higher logprobs indicate a higher confidence the model has in its predictions."
    )
    characters: Optional[List[SpeechToTextCharacterResponseModel]] = Field(
        default=None,
        description="The characters that make up the word and their timing information.",
    )
    channel_index: Optional[int] = Field(
        default=None,
        description="The channel this word was spoken on (for multichannel audio). Null for single-channel transcriptions.",
    )
