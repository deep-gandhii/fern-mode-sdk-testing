from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyCreateForcedAlignmentV1ForcedAlignmentPost(BaseModel):
    """BodyCreateForcedAlignmentV1ForcedAlignmentPost

    :param file: The file to align. All major audio formats are supported. The file size must be less than 1GB.
    :type file: bytes
    :param text: The text to align with the audio. The input text can be in any format, however diarization is not supported at this time.
    :type text: str
    """

    file: bytes = Field(
        description="The file to align. All major audio formats are supported. The file size must be less than 1GB."
    )
    text: str = Field(
        description="The text to align with the audio. The input text can be in any format, however diarization is not supported at this time."
    )
