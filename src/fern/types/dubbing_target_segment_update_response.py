from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dubbing_target_transcript_segment import DubbingTargetTranscriptSegment


class DubbingTargetSegmentUpdateResponse(BaseModel):
    """The result of a target-translation edit: the updated segment and the new revision.

    :param segment: One segment of a target transcript: a source segment plus its translation.
    :type segment: DubbingTargetTranscriptSegment
    :param revision: The target's revision after this edit.
    :type revision: int
    """

    segment: DubbingTargetTranscriptSegment = Field(
        description="One segment of a target transcript: a source segment plus its translation."
    )
    revision: int = Field(description="The target's revision after this edit.")
