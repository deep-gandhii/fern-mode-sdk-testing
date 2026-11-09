from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .video_analysis_result import VideoAnalysisResult

VideoAnalysisStatus = typing.Union[
    typing.Literal["processing", "completed", "failed"], typing.Any
]


class VideoAnalysis(BaseModel):
    """VideoAnalysis

    :param status: status
    :type status: VideoAnalysisStatus
    :param data: data
    :type data: VideoAnalysisResult
    :param updated_at_ms: updated_at_ms, defaults to None
    :type updated_at_ms: int, optional
    """

    status: VideoAnalysisStatus
    data: Optional[VideoAnalysisResult]
    updated_at_ms: Optional[int] = Field(default=None)
