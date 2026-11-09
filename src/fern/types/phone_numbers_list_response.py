from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .get_phone_number_twilio_response_model import GetPhoneNumberTwilioResponseModel
from .get_phone_number_exotel_response_model import GetPhoneNumberExotelResponseModel
from .get_phone_number_sip_trunk_response_model import (
    GetPhoneNumberSipTrunkResponseModel,
)


# fernMode variant type for a shared-component member of PhoneNumbersListResponse
class PhoneNumbersListResponse_Twilio(GetPhoneNumberTwilioResponseModel):
    pass


# fernMode variant type for a shared-component member of PhoneNumbersListResponse
class PhoneNumbersListResponse_Exotel(GetPhoneNumberExotelResponseModel):
    pass


# fernMode variant type for a shared-component member of PhoneNumbersListResponse
class PhoneNumbersListResponse_SipTrunk(GetPhoneNumberSipTrunkResponseModel):
    pass


# Union type for PhoneNumbersListResponse
# Pydantic will attempt to validate against each type in order
PhoneNumbersListResponse = Union[
    GetPhoneNumberTwilioResponseModel,
    GetPhoneNumberExotelResponseModel,
    GetPhoneNumberSipTrunkResponseModel,
]
# TypeAdapter for runtime validation of PhoneNumbersListResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PhoneNumbersListResponse_adapter = TypeAdapter(PhoneNumbersListResponse)
