from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

PlayDtmfResultErrorModelResultType = typing.Union[
    typing.Literal["play_dtmf_error"], typing.Any
]

PlayDtmfResultErrorModelStatus = typing.Union[typing.Literal["error"], typing.Any]


class PlayDtmfResultErrorModel(BaseModel):
    """PlayDtmfResultErrorModel

    :param result_type: result_type, defaults to None
    :type result_type: PlayDtmfResultErrorModelResultType, optional
    :param status: status, defaults to None
    :type status: PlayDtmfResultErrorModelStatus, optional
    :param error: error
    :type error: str
    :param details: details, defaults to None
    :type details: str, optional
    """

    result_type: Optional[PlayDtmfResultErrorModelResultType] = Field(default=None)
    status: Optional[PlayDtmfResultErrorModelStatus] = Field(default=None)
    error: str
    details: Optional[str] = Field(default=None)
