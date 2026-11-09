from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .speech_to_text_word_response_model import SpeechToTextWordResponseModel
from .additional_format_response_model import AdditionalFormatResponseModel
from .detected_entity import DetectedEntity


class SpeechToTextChunkResponseModel(BaseModel):
    """Chunk-level detail of the transcription with timing information.

    :param language_code: The detected language code (e.g. 'eng' for English).
    :type language_code: str
    :param language_probability: The confidence score of the language detection (0 to 1).
    :type language_probability: float
    :param text: The raw text of the transcription.
    :type text: str
    :param words: List of words with their timing information.
    :type words: List[SpeechToTextWordResponseModel]
    :param channel_index: The channel index this transcript belongs to (for multichannel audio)., defaults to None
    :type channel_index: int, optional
    :param additional_formats: Requested additional formats of the transcript., defaults to None
    :type additional_formats: List[AdditionalFormatResponseModel], optional
    :param transcription_id: The transcription ID of the response., defaults to None
    :type transcription_id: str, optional
    :param entities: List of detected entities with their text, type, and character positions in the transcript., defaults to None
    :type entities: List[DetectedEntity], optional
    :param audio_duration_secs: The duration of the audio that was transcribed in seconds., defaults to None
    :type audio_duration_secs: float, optional
    """

    language_code: str = Field(
        description="The detected language code (e.g. 'eng' for English)."
    )
    language_probability: float = Field(
        description="The confidence score of the language detection (0 to 1)."
    )
    text: str = Field(description="The raw text of the transcription.")
    words: List[SpeechToTextWordResponseModel] = Field(
        description="List of words with their timing information."
    )
    channel_index: Optional[int] = Field(
        default=None,
        description="The channel index this transcript belongs to (for multichannel audio).",
    )
    additional_formats: Optional[List[AdditionalFormatResponseModel]] = Field(
        default=None, description="Requested additional formats of the transcript."
    )
    transcription_id: Optional[str] = Field(
        default=None, description="The transcription ID of the response."
    )
    entities: Optional[List[DetectedEntity]] = Field(
        default=None,
        description="List of detected entities with their text, type, and character positions in the transcript.",
    )
    audio_duration_secs: Optional[float] = Field(
        default=None,
        description="The duration of the audio that was transcribed in seconds.",
    )
