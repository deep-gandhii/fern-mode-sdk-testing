from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .dubbing_transcript_segment import DubbingTranscriptSegment


class DubbingSourceSegmentUpdateResponse(BaseModel):
    """The result of a source-segment add or edit: the segment and the new revision.

    :param segment: One segment of a source transcript.
    :type segment: DubbingTranscriptSegment
    :param revision: The project's source-transcript revision after this edit.
    :type revision: int
    """

    segment: DubbingTranscriptSegment = Field(
        description="One segment of a source transcript."
    )
    revision: int = Field(
        description="The project's source-transcript revision after this edit."
    )
