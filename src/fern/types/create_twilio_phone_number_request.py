from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .region_config_request import RegionConfigRequest

CreateTwilioPhoneNumberRequestProvider = typing.Union[
    typing.Literal["twilio"], typing.Any
]


class CreateTwilioPhoneNumberRequest(BaseModel):
    """CreateTwilioPhoneNumberRequest

    :param phone_number: Phone number
    :type phone_number: str
    :param label: Label for the phone number
    :type label: str
    :param supports_inbound: This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls, defaults to None
    :type supports_inbound: bool, optional
    :param supports_outbound: This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls, defaults to None
    :type supports_outbound: bool, optional
    :param provider: provider, defaults to None
    :type provider: CreateTwilioPhoneNumberRequestProvider, optional
    :param agent_id: Agent ID to assign the phone number to, defaults to None
    :type agent_id: str, optional
    :param sid: Twilio Account SID
    :type sid: str
    :param token: Twilio Auth Token
    :type token: str
    :param region_config: Twilio Additional Region Configuration, defaults to None
    :type region_config: RegionConfigRequest, optional
    :param enable_sms: Route inbound SMS to ElevenLabs. On by default; set to false to skip SMS configuration for numbers that don't support it., defaults to None
    :type enable_sms: bool, optional
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
    provider: Optional[CreateTwilioPhoneNumberRequestProvider] = Field(default=None)
    agent_id: Optional[str] = Field(
        default=None, description="Agent ID to assign the phone number to"
    )
    sid: str = Field(description="Twilio Account SID")
    token: str = Field(description="Twilio Auth Token")
    region_config: Optional[RegionConfigRequest] = Field(
        default=None, description="Twilio Additional Region Configuration"
    )
    enable_sms: Optional[bool] = Field(
        default=None,
        description="Route inbound SMS to ElevenLabs. On by default; set to false to skip SMS configuration for numbers that don't support it.",
    )
