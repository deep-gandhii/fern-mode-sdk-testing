from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyTranscribesSegmentsV1DubbingResourceDubbingIdTranscribePost(BaseModel):
    """BodyTranscribesSegmentsV1DubbingResourceDubbingIdTranscribePost

    :param segments: Transcribe this specific list of segments.
    :type segments: List[str]
    """

    segments: List[str] = Field(
        description="Transcribe this specific list of segments."
    )
