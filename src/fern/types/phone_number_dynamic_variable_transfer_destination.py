from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PhoneNumberDynamicVariableTransferDestinationType = typing.Union[
    typing.Literal["phone_dynamic_variable"], typing.Any
]


class PhoneNumberDynamicVariableTransferDestination(BaseModel):
    """PhoneNumberDynamicVariableTransferDestination

    :param type: type, defaults to None
    :type type: PhoneNumberDynamicVariableTransferDestinationType, optional
    :param phone_number: phone_number
    :type phone_number: str
    """

    type: Optional[PhoneNumberDynamicVariableTransferDestinationType] = Field(
        default=None
    )
    phone_number: str
