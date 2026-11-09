from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .detailed_music_response import DetailedMusicResponse


class MultipartMusicResponse(BaseModel):
    """Multipart response structure with JSON metadata and binary audio

    :param metadata: Response model for structured music generation endpoint
    :type metadata: DetailedMusicResponse
    :param audio: Binary audio data in the requested format
    :type audio: bytes
    """

    metadata: DetailedMusicResponse = Field(
        description="Response model for structured music generation endpoint"
    )
    audio: bytes = Field(description="Binary audio data in the requested format")
