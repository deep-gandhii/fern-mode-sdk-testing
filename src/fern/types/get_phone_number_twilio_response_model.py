from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .phone_number_agent_info import PhoneNumberAgentInfo

GetPhoneNumberTwilioResponseModelProvider = typing.Union[
    typing.Literal["twilio"], typing.Any
]


class GetPhoneNumberTwilioResponseModel(BaseModel):
    """GetPhoneNumberTwilioResponseModel

    :param phone_number: Phone number
    :type phone_number: str
    :param label: Label for the phone number
    :type label: str
    :param supports_inbound: This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls, defaults to None
    :type supports_inbound: bool, optional
    :param supports_outbound: This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls, defaults to None
    :type supports_outbound: bool, optional
    :param phone_number_id: The ID of the phone number
    :type phone_number_id: str
    :param assigned_agent: The agent that is assigned to the phone number, defaults to None
    :type assigned_agent: PhoneNumberAgentInfo, optional
    :param provider: Phone provider, defaults to None
    :type provider: GetPhoneNumberTwilioResponseModelProvider, optional
    """

    phone_number: str = Field(description="Phone number")
    label: str = Field(description="Label for the phone number")
    supports_inbound: Optional[bool] = Field(
        default=None,
        description="This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls",
    )
    supports_outbound: Optional[bool] = Field(
        default=None,
        description="This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls",
    )
    phone_number_id: str = Field(description="The ID of the phone number")
    assigned_agent: Optional[PhoneNumberAgentInfo] = Field(
        default=None, description="The agent that is assigned to the phone number"
    )
    provider: Optional[GetPhoneNumberTwilioResponseModelProvider] = Field(
        default=None, description="Phone provider"
    )
