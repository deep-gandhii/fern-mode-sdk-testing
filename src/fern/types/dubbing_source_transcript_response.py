from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dubbing_transcript_segment import DubbingTranscriptSegment


class DubbingSourceTranscriptResponse(BaseModel):
    """DubbingSourceTranscriptResponse

    :param language: BCP-47 language tag of the source transcript (null if unknown)., defaults to None
    :type language: str, optional
    :param segments: The source segments, in playback order.
    :type segments: List[DubbingTranscriptSegment]
    :param revision: The project's source-transcript revision at read time.
    :type revision: int
    """

    language: Optional[str] = Field(
        default=None,
        description="BCP-47 language tag of the source transcript (null if unknown).",
    )
    segments: List[DubbingTranscriptSegment] = Field(
        description="The source segments, in playback order."
    )
    revision: int = Field(
        description="The project's source-transcript revision at read time."
    )
