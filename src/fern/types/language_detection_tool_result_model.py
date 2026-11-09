from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

LanguageDetectionToolResultModelResultType = typing.Union[
    typing.Literal["language_detection_success"], typing.Any
]

LanguageDetectionToolResultModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class LanguageDetectionToolResultModel(BaseModel):
    """LanguageDetectionToolResultModel

    :param result_type: result_type, defaults to None
    :type result_type: LanguageDetectionToolResultModelResultType, optional
    :param status: status, defaults to None
    :type status: LanguageDetectionToolResultModelStatus, optional
    :param reason: reason, defaults to None
    :type reason: str, optional
    :param language: language, defaults to None
    :type language: str, optional
    """

    result_type: Optional[LanguageDetectionToolResultModelResultType] = Field(
        default=None
    )
    status: Optional[LanguageDetectionToolResultModelStatus] = Field(default=None)
    reason: Optional[str] = Field(default=None)
    language: Optional[str] = Field(default=None)
