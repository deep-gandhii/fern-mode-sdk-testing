from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DubbingTargetTranscriptSegment(BaseModel):
    """One segment of a target transcript: a source segment plus its translation.

    :param id: Stable identifier of the segment (from the source).
    :type id: str
    :param speaker_id: Identifier of the segment's speaker.
    :type speaker_id: str
    :param start_s: Start time of the segment, in seconds.
    :type start_s: float
    :param end_s: End time of the segment, in seconds.
    :type end_s: float
    :param source_text: The source-language text of the segment.
    :type source_text: str
    :param translation: The translated text, or null if not translated yet (needs translation)., defaults to None
    :type translation: str, optional
    """

    id: str = Field(description="Stable identifier of the segment (from the source).")
    speaker_id: str = Field(description="Identifier of the segment's speaker.")
    start_s: float = Field(description="Start time of the segment, in seconds.")
    end_s: float = Field(description="End time of the segment, in seconds.")
    source_text: str = Field(description="The source-language text of the segment.")
    translation: Optional[str] = Field(
        default=None,
        description="The translated text, or null if not translated yet (needs translation).",
    )
