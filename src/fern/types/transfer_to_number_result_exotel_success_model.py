from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

TransferToNumberResultExotelSuccessModelResultType = typing.Union[
    typing.Literal["transfer_to_number_exotel_success"], typing.Any
]

TransferToNumberResultExotelSuccessModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class TransferToNumberResultExotelSuccessModel(BaseModel):
    """TransferToNumberResultExotelSuccessModel

    :param result_type: result_type, defaults to None
    :type result_type: TransferToNumberResultExotelSuccessModelResultType, optional
    :param status: status, defaults to None
    :type status: TransferToNumberResultExotelSuccessModelStatus, optional
    :param transfer_number: transfer_number
    :type transfer_number: str
    :param reason: reason, defaults to None
    :type reason: str, optional
    :param agent_message: agent_message, defaults to None
    :type agent_message: str, optional
    :param note: note, defaults to None
    :type note: str, optional
    """

    result_type: Optional[TransferToNumberResultExotelSuccessModelResultType] = Field(
        default=None
    )
    status: Optional[TransferToNumberResultExotelSuccessModelStatus] = Field(
        default=None
    )
    transfer_number: str
    reason: Optional[str] = Field(default=None)
    agent_message: Optional[str] = Field(default=None)
    note: Optional[str] = Field(default=None)
