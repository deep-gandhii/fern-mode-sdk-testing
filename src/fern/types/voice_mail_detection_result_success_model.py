from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

VoiceMailDetectionResultSuccessModelResultType = typing.Union[
    typing.Literal["voicemail_detection_success"], typing.Any
]

VoiceMailDetectionResultSuccessModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class VoiceMailDetectionResultSuccessModel(BaseModel):
    """VoiceMailDetectionResultSuccessModel

    :param result_type: result_type, defaults to None
    :type result_type: VoiceMailDetectionResultSuccessModelResultType, optional
    :param status: status, defaults to None
    :type status: VoiceMailDetectionResultSuccessModelStatus, optional
    :param voicemail_message: voicemail_message, defaults to None
    :type voicemail_message: str, optional
    :param reason: reason, defaults to None
    :type reason: str, optional
    """

    result_type: Optional[VoiceMailDetectionResultSuccessModelResultType] = Field(
        default=None
    )
    status: Optional[VoiceMailDetectionResultSuccessModelStatus] = Field(default=None)
    voicemail_message: Optional[str] = Field(default=None)
    reason: Optional[str] = Field(default=None)
