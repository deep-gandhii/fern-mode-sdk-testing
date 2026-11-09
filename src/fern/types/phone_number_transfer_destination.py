from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PhoneNumberTransferDestinationType = typing.Union[typing.Literal["phone"], typing.Any]


class PhoneNumberTransferDestination(BaseModel):
    """PhoneNumberTransferDestination

    :param type: type, defaults to None
    :type type: PhoneNumberTransferDestinationType, optional
    :param phone_number: phone_number
    :type phone_number: str
    """

    type: Optional[PhoneNumberTransferDestinationType] = Field(default=None)
    phone_number: str
