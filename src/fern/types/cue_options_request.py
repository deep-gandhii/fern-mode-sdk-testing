from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class CueOptionsRequest(BaseModel):
    """CueOptionsRequest

    :param min_duration_ms: Minimum duration of each cue in milliseconds., defaults to None
    :type min_duration_ms: int, optional
    :param max_duration_ms: Maximum duration of each cue in milliseconds., defaults to None
    :type max_duration_ms: int, optional
    :param max_lines_per_cue: Maximum number of lines per cue., defaults to None
    :type max_lines_per_cue: int, optional
    :param max_chars_per_line: Maximum number of characters per line in a cue., defaults to None
    :type max_chars_per_line: int, optional
    :param max_chars_per_s: Maximum characters per second reading speed. If not set, no reading speed limit is applied., defaults to None
    :type max_chars_per_s: int, optional
    :param min_gap_between_cues_frames: Minimum gap between consecutive cues in frames. If not set, no minimum gap is enforced., defaults to None
    :type min_gap_between_cues_frames: int, optional
    """

    min_duration_ms: Optional[int] = Field(
        default=None, description="Minimum duration of each cue in milliseconds."
    )
    max_duration_ms: Optional[int] = Field(
        default=None, description="Maximum duration of each cue in milliseconds."
    )
    max_lines_per_cue: Optional[int] = Field(
        default=None, description="Maximum number of lines per cue."
    )
    max_chars_per_line: Optional[int] = Field(
        default=None, description="Maximum number of characters per line in a cue."
    )
    max_chars_per_s: Optional[int] = Field(
        default=None,
        description="Maximum characters per second reading speed. If not set, no reading speed limit is applied.",
    )
    min_gap_between_cues_frames: Optional[int] = Field(
        default=None,
        description="Minimum gap between consecutive cues in frames. If not set, no minimum gap is enforced.",
    )
