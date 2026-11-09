from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .create_twilio_phone_number_request import CreateTwilioPhoneNumberRequest
from .create_exotel_phone_number_request import CreateExotelPhoneNumberRequest
from .create_sip_trunk_phone_number_request import CreateSipTrunkPhoneNumberRequest


# fernMode variant type for a shared-component member of PhoneNumbersCreateRequestBody
class PhoneNumbersCreateRequestBody_Twilio(CreateTwilioPhoneNumberRequest):
    pass


# fernMode variant type for a shared-component member of PhoneNumbersCreateRequestBody
class PhoneNumbersCreateRequestBody_Exotel(CreateExotelPhoneNumberRequest):
    pass


# fernMode variant type for a shared-component member of PhoneNumbersCreateRequestBody
class PhoneNumbersCreateRequestBody_SipTrunk(CreateSipTrunkPhoneNumberRequest):
    pass


# Union type for PhoneNumbersCreateRequestBody
# Pydantic will attempt to validate against each type in order
PhoneNumbersCreateRequestBody = Union[
    CreateTwilioPhoneNumberRequest,
    CreateExotelPhoneNumberRequest,
    CreateSipTrunkPhoneNumberRequest,
]
# TypeAdapter for runtime validation of PhoneNumbersCreateRequestBody
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PhoneNumbersCreateRequestBody_adapter = TypeAdapter(PhoneNumbersCreateRequestBody)
