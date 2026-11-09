from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

TransferToNumberResultTwilioSuccessModelResultType = typing.Union[
    typing.Literal["transfer_to_number_twilio_success"], typing.Any
]

TransferToNumberResultTwilioSuccessModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class TransferToNumberResultTwilioSuccessModel(BaseModel):
    """TransferToNumberResultTwilioSuccessModel

    :param result_type: result_type, defaults to None
    :type result_type: TransferToNumberResultTwilioSuccessModelResultType, optional
    :param status: status, defaults to None
    :type status: TransferToNumberResultTwilioSuccessModelStatus, optional
    :param transfer_number: transfer_number
    :type transfer_number: str
    :param reason: reason, defaults to None
    :type reason: str, optional
    :param client_message: client_message, defaults to None
    :type client_message: str, optional
    :param agent_message: agent_message
    :type agent_message: str
    :param conference_name: conference_name
    :type conference_name: str
    :param post_dial_digits: post_dial_digits, defaults to None
    :type post_dial_digits: str, optional
    :param note: note, defaults to None
    :type note: str, optional
    """

    result_type: Optional[TransferToNumberResultTwilioSuccessModelResultType] = Field(
        default=None
    )
    status: Optional[TransferToNumberResultTwilioSuccessModelStatus] = Field(
        default=None
    )
    transfer_number: str
    reason: Optional[str] = Field(default=None)
    client_message: Optional[str] = Field(default=None)
    agent_message: str
    conference_name: str
    post_dial_digits: Optional[str] = Field(default=None)
    note: Optional[str] = Field(default=None)
