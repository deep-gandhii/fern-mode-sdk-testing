from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

TransferToNumberResultSipSuccessModelResultType = typing.Union[
    typing.Literal["transfer_to_number_sip_success"], typing.Any
]

TransferToNumberResultSipSuccessModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class TransferToNumberResultSipSuccessModel(BaseModel):
    """TransferToNumberResultSipSuccessModel

    :param result_type: result_type, defaults to None
    :type result_type: TransferToNumberResultSipSuccessModelResultType, optional
    :param status: status, defaults to None
    :type status: TransferToNumberResultSipSuccessModelStatus, optional
    :param transfer_number: transfer_number
    :type transfer_number: str
    :param reason: reason, defaults to None
    :type reason: str, optional
    :param note: note, defaults to None
    :type note: str, optional
    """

    result_type: Optional[TransferToNumberResultSipSuccessModelResultType] = Field(
        default=None
    )
    status: Optional[TransferToNumberResultSipSuccessModelStatus] = Field(default=None)
    transfer_number: str
    reason: Optional[str] = Field(default=None)
    note: Optional[str] = Field(default=None)
