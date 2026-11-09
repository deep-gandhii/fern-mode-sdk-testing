from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DubbingSegmentCreateRequest(BaseModel):
    """A new source segment; its id and word-level alignment are assigned by the server.

    :param text: The text of the new segment.
    :type text: str
    :param speaker_id: Identifier of the segment's speaker.
    :type speaker_id: str
    :param start_s: Start time of the segment, in seconds.
    :type start_s: float
    :param end_s: End time of the segment, in seconds.
    :type end_s: float
    """

    text: str = Field(description="The text of the new segment.")
    speaker_id: str = Field(description="Identifier of the segment's speaker.")
    start_s: float = Field(description="Start time of the segment, in seconds.")
    end_s: float = Field(description="End time of the segment, in seconds.")
