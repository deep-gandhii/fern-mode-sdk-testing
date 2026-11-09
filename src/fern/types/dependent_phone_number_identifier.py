from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .telephony_provider import TelephonyProvider


class DependentPhoneNumberIdentifier(BaseModel):
    """DependentPhoneNumberIdentifier

    :param phone_number_id: phone_number_id
    :type phone_number_id: str
    :param phone_number: phone_number
    :type phone_number: str
    :param label: label
    :type label: str
    :param provider: provider
    :type provider: TelephonyProvider
    """

    phone_number_id: str
    phone_number: str
    label: str
    provider: TelephonyProvider
