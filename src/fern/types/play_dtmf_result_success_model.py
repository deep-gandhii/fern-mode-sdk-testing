from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

PlayDtmfResultSuccessModelResultType = typing.Union[
    typing.Literal["play_dtmf_success"], typing.Any
]

PlayDtmfResultSuccessModelStatus = typing.Union[typing.Literal["success"], typing.Any]


class PlayDtmfResultSuccessModel(BaseModel):
    """PlayDtmfResultSuccessModel

    :param result_type: result_type, defaults to None
    :type result_type: PlayDtmfResultSuccessModelResultType, optional
    :param status: status, defaults to None
    :type status: PlayDtmfResultSuccessModelStatus, optional
    :param dtmf_tones: dtmf_tones
    :type dtmf_tones: str
    :param reason: reason, defaults to None
    :type reason: str, optional
    """

    result_type: Optional[PlayDtmfResultSuccessModelResultType] = Field(default=None)
    status: Optional[PlayDtmfResultSuccessModelStatus] = Field(default=None)
    dtmf_tones: str
    reason: Optional[str] = Field(default=None)
