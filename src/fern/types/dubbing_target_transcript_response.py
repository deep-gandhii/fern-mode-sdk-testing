from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dubbing_target_transcript_segment import DubbingTargetTranscriptSegment


class DubbingTargetTranscriptResponse(BaseModel):
    """DubbingTargetTranscriptResponse

    :param source_language: BCP-47 language tag of the source transcript., defaults to None
    :type source_language: str, optional
    :param target_language: BCP-47 language tag this target is translated into.
    :type target_language: str
    :param segments: The target segments, in playback order.
    :type segments: List[DubbingTargetTranscriptSegment]
    :param revision: The target's revision at read time.
    :type revision: int
    """

    source_language: Optional[str] = Field(
        default=None, description="BCP-47 language tag of the source transcript."
    )
    target_language: str = Field(
        description="BCP-47 language tag this target is translated into."
    )
    segments: List[DubbingTargetTranscriptSegment] = Field(
        description="The target segments, in playback order."
    )
    revision: int = Field(description="The target's revision at read time.")
