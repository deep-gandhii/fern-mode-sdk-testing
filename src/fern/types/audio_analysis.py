from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .audio_analysis_result import AudioAnalysisResult

AudioAnalysisStatus = typing.Union[
    typing.Literal["processing", "completed", "failed"], typing.Any
]


class AudioAnalysis(BaseModel):
    """AudioAnalysis

    :param status: status
    :type status: AudioAnalysisStatus
    :param data: data
    :type data: AudioAnalysisResult
    :param updated_at_ms: updated_at_ms, defaults to None
    :type updated_at_ms: int, optional
    """

    status: AudioAnalysisStatus
    data: Optional[AudioAnalysisResult]
    updated_at_ms: Optional[int] = Field(default=None)
