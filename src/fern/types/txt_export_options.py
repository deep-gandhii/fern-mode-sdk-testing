from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

TxtExportOptionsFormat = typing.Union[typing.Literal["txt"], typing.Any]


class TxtExportOptions(BaseModel):
    """TxtExportOptions

    :param max_characters_per_line: max_characters_per_line, defaults to None
    :type max_characters_per_line: int, optional
    :param include_speakers: include_speakers, defaults to None
    :type include_speakers: bool, optional
    :param include_timestamps: include_timestamps, defaults to None
    :type include_timestamps: bool, optional
    :param format: format
    :type format: TxtExportOptionsFormat
    :param segment_on_silence_longer_than_s: segment_on_silence_longer_than_s, defaults to None
    :type segment_on_silence_longer_than_s: float, optional
    :param max_segment_duration_s: max_segment_duration_s, defaults to None
    :type max_segment_duration_s: float, optional
    :param max_segment_chars: max_segment_chars, defaults to None
    :type max_segment_chars: int, optional
    """

    max_characters_per_line: Optional[int] = Field(default=None)
    include_speakers: Optional[bool] = Field(default=None)
    include_timestamps: Optional[bool] = Field(default=None)
    format: TxtExportOptionsFormat = Field(default="txt")
    segment_on_silence_longer_than_s: Optional[float] = Field(default=None)
    max_segment_duration_s: Optional[float] = Field(default=None)
    max_segment_chars: Optional[int] = Field(default=None)
