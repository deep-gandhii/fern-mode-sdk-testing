from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .phone_number_transfer import PhoneNumberTransfer

TransferToNumberToolConfigInputSystemToolType = typing.Union[
    typing.Literal["transfer_to_number"], typing.Any
]


class TransferToNumberToolConfigInput(BaseModel):
    """TransferToNumberToolConfigInput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: TransferToNumberToolConfigInputSystemToolType, optional
    :param transfers: transfers
    :type transfers: List[PhoneNumberTransfer]
    :param enable_client_message: Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility., defaults to None
    :type enable_client_message: bool, optional
    """

    system_tool_type: Optional[TransferToNumberToolConfigInputSystemToolType] = Field(
        default=None
    )
    transfers: List[PhoneNumberTransfer]
    enable_client_message: Optional[bool] = Field(
        default=None,
        description="Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.",
    )
