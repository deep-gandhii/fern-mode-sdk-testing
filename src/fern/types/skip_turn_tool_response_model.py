from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

SkipTurnToolResponseModelResultType = typing.Union[
    typing.Literal["skip_turn_success"], typing.Any
]

SkipTurnToolResponseModelStatus = typing.Union[typing.Literal["success"], typing.Any]


class SkipTurnToolResponseModel(BaseModel):
    """SkipTurnToolResponseModel

    :param result_type: result_type, defaults to None
    :type result_type: SkipTurnToolResponseModelResultType, optional
    :param status: status, defaults to None
    :type status: SkipTurnToolResponseModelStatus, optional
    :param reason: reason, defaults to None
    :type reason: str, optional
    """

    result_type: Optional[SkipTurnToolResponseModelResultType] = Field(default=None)
    status: Optional[SkipTurnToolResponseModelStatus] = Field(default=None)
    reason: Optional[str] = Field(default=None)
