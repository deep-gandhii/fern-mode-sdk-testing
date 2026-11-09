from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

EndCallToolResultModelResultType = typing.Union[
    typing.Literal["end_call_success"], typing.Any
]

EndCallToolResultModelStatus = typing.Union[typing.Literal["success"], typing.Any]


class EndCallToolResultModel(BaseModel):
    """EndCallToolResultModel

    :param result_type: result_type, defaults to None
    :type result_type: EndCallToolResultModelResultType, optional
    :param status: status, defaults to None
    :type status: EndCallToolResultModelStatus, optional
    :param reason: reason, defaults to None
    :type reason: str, optional
    :param message: message, defaults to None
    :type message: str, optional
    """

    result_type: Optional[EndCallToolResultModelResultType] = Field(default=None)
    status: Optional[EndCallToolResultModelStatus] = Field(default=None)
    reason: Optional[str] = Field(default=None)
    message: Optional[str] = Field(default=None)
