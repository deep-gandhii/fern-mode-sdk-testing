from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

LanguageDetectionToolConfigSystemToolType = typing.Union[
    typing.Literal["language_detection"], typing.Any
]


class LanguageDetectionToolConfig(BaseModel):
    """LanguageDetectionToolConfig

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: LanguageDetectionToolConfigSystemToolType, optional
    """

    system_tool_type: Optional[LanguageDetectionToolConfigSystemToolType] = Field(
        default=None
    )
