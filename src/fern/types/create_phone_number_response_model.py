from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CreatePhoneNumberResponseModel(BaseModel):
    """CreatePhoneNumberResponseModel

    :param phone_number_id: Phone entity ID
    :type phone_number_id: str
    """

    phone_number_id: str = Field(description="Phone entity ID")
