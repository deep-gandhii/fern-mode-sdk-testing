from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .image_analysis_result import ImageAnalysisResult

ImageAnalysisStatus = typing.Union[
    typing.Literal["processing", "completed", "failed"], typing.Any
]


class ImageAnalysis(BaseModel):
    """ImageAnalysis

    :param status: status
    :type status: ImageAnalysisStatus
    :param data: data
    :type data: ImageAnalysisResult
    :param updated_at_ms: updated_at_ms, defaults to None
    :type updated_at_ms: int, optional
    """

    status: ImageAnalysisStatus
    data: Optional[ImageAnalysisResult]
    updated_at_ms: Optional[int] = Field(default=None)
