from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .segment_subtitle_frame import SegmentSubtitleFrame
from .dubbing_media_reference import DubbingMediaReference


class DubbedSegment(BaseModel):
    """DubbedSegment

    :param start_time: start_time
    :type start_time: float
    :param end_time: end_time
    :type end_time: float
    :param text: text
    :type text: str
    :param subtitles: subtitles
    :type subtitles: List[SegmentSubtitleFrame]
    :param audio_stale: audio_stale
    :type audio_stale: bool
    :param media_ref: media_ref
    :type media_ref: DubbingMediaReference
    """

    start_time: float
    end_time: float
    text: Optional[str]
    subtitles: List[SegmentSubtitleFrame]
    audio_stale: bool
    media_ref: DubbingMediaReference
