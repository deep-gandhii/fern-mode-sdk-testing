from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DubbingTranscriptSegment(BaseModel):
    """One segment of a source transcript.

    :param id: Stable identifier of the segment.
    :type id: str
    :param text: The transcribed text of the segment.
    :type text: str
    :param speaker_id: Identifier of the segment's speaker.
    :type speaker_id: str
    :param start_s: Start time of the segment, in seconds.
    :type start_s: float
    :param end_s: End time of the segment, in seconds.
    :type end_s: float
    """

    id: str = Field(description="Stable identifier of the segment.")
    text: str = Field(description="The transcribed text of the segment.")
    speaker_id: str = Field(description="Identifier of the segment's speaker.")
    start_s: float = Field(description="Start time of the segment, in seconds.")
    end_s: float = Field(description="End time of the segment, in seconds.")
