from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dubbing_transcript import DubbingTranscript

DubbingTranscriptsResponseModelTranscriptFormat = typing.Union[
    typing.Literal["srt", "webvtt", "json"], typing.Any
]


class DubbingTranscriptsResponseModel(BaseModel):
    """DubbingTranscriptsResponseModel

    :param transcript_format: transcript_format
    :type transcript_format: DubbingTranscriptsResponseModelTranscriptFormat
    :param srt: srt, defaults to None
    :type srt: str, optional
    :param webvtt: webvtt, defaults to None
    :type webvtt: str, optional
    :param json_: json_, defaults to None
    :type json_: DubbingTranscript, optional
    """

    transcript_format: DubbingTranscriptsResponseModelTranscriptFormat
    srt: Optional[str] = Field(default=None)
    webvtt: Optional[str] = Field(default=None)
    json_: Optional[DubbingTranscript] = Field(
        alias="json", serialization_alias="json", default=None
    )
