from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .video_subject import VideoSubject
from .video_segment import VideoSegment
from .video_key_moment import VideoKeyMoment


class VideoAnalysisResult(BaseModel):
    """VideoAnalysisResult

    :param title: title
    :type title: str
    :param description: description
    :type description: str
    :param content_type: content_type, defaults to None
    :type content_type: str, optional
    :param overall_pacing: overall_pacing, defaults to None
    :type overall_pacing: str, optional
    :param subjects: subjects, defaults to None
    :type subjects: List[VideoSubject], optional
    :param segments: segments, defaults to None
    :type segments: List[VideoSegment], optional
    :param key_moments: key_moments, defaults to None
    :type key_moments: List[VideoKeyMoment], optional
    """

    title: str
    description: str
    content_type: Optional[str] = Field(default=None)
    overall_pacing: Optional[str] = Field(default=None)
    subjects: Optional[List[VideoSubject]] = Field(default=None)
    segments: Optional[List[VideoSegment]] = Field(default=None)
    key_moments: Optional[List[VideoKeyMoment]] = Field(default=None)
