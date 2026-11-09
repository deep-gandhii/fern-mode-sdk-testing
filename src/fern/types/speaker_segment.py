from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .segment_subtitle_frame import SegmentSubtitleFrame
from .dubbed_segment import DubbedSegment


class SpeakerSegment(BaseModel):
    """SpeakerSegment

    :param id: id
    :type id: str
    :param start_time: start_time
    :type start_time: float
    :param end_time: end_time
    :type end_time: float
    :param text: text
    :type text: str
    :param subtitles: subtitles
    :type subtitles: List[SegmentSubtitleFrame]
    :param dubs: dubs
    :type dubs: Dict[str, DubbedSegment]
    """

    id: str
    start_time: float
    end_time: float
    text: str
    subtitles: List[SegmentSubtitleFrame]
    dubs: Dict[str, DubbedSegment]
