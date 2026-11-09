from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .character_alignment_response_model import CharacterAlignmentResponseModel
from .voice_segment import VoiceSegment


class StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel(BaseModel):
    """StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel

    :param audio_base_64: Base64 encoded audio data
    :type audio_base_64: str
    :param alignment: Timestamp information for each character in the original text, defaults to None
    :type alignment: CharacterAlignmentResponseModel, optional
    :param normalized_alignment: Timestamp information for each character in the normalized text, defaults to None
    :type normalized_alignment: CharacterAlignmentResponseModel, optional
    :param voice_segments: Voice segments for the audio
    :type voice_segments: List[VoiceSegment]
    """

    audio_base_64: str = Field(
        alias="audio_base64",
        serialization_alias="audio_base64",
        description="Base64 encoded audio data",
    )
    alignment: Optional[CharacterAlignmentResponseModel] = Field(
        default=None,
        description="Timestamp information for each character in the original text",
    )
    normalized_alignment: Optional[CharacterAlignmentResponseModel] = Field(
        default=None,
        description="Timestamp information for each character in the normalized text",
    )
    voice_segments: List[VoiceSegment] = Field(
        description="Voice segments for the audio"
    )
