from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .speech_to_text_chunk_response_model import SpeechToTextChunkResponseModel


class MultichannelSpeechToTextResponseModel(BaseModel):
    """Response model for multichannel speech-to-text transcription.

    :param transcripts: List of transcripts, one for each audio channel. Each transcript contains the text and word-level details for its respective channel.
    :type transcripts: List[SpeechToTextChunkResponseModel]
    :param transcription_id: The transcription ID of the response., defaults to None
    :type transcription_id: str, optional
    :param audio_duration_secs: The duration of the audio that was transcribed across all channels in seconds., defaults to None
    :type audio_duration_secs: float, optional
    """

    transcripts: List[SpeechToTextChunkResponseModel] = Field(
        description="List of transcripts, one for each audio channel. Each transcript contains the text and word-level details for its respective channel."
    )
    transcription_id: Optional[str] = Field(
        default=None, description="The transcription ID of the response."
    )
    audio_duration_secs: Optional[float] = Field(
        default=None,
        description="The duration of the audio that was transcribed across all channels in seconds.",
    )
