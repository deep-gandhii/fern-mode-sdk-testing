from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

TransferToNumberResultErrorModelResultType = typing.Union[
    typing.Literal["transfer_to_number_error"], typing.Any
]

TransferToNumberResultErrorModelStatus = typing.Union[
    typing.Literal["error"], typing.Any
]


class TransferToNumberResultErrorModel(BaseModel):
    """TransferToNumberResultErrorModel

    :param result_type: result_type, defaults to None
    :type result_type: TransferToNumberResultErrorModelResultType, optional
    :param status: status, defaults to None
    :type status: TransferToNumberResultErrorModelStatus, optional
    :param error: error
    :type error: str
    :param details: details, defaults to None
    :type details: str, optional
    """

    result_type: Optional[TransferToNumberResultErrorModelResultType] = Field(
        default=None
    )
    status: Optional[TransferToNumberResultErrorModelStatus] = Field(default=None)
    error: str
    details: Optional[str] = Field(default=None)
