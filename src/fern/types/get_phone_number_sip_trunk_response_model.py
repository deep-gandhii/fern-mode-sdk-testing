from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .phone_number_agent_info import PhoneNumberAgentInfo
from .get_phone_number_outbound_sip_trunk_config_response_model import (
    GetPhoneNumberOutboundSipTrunkConfigResponseModel,
)
from .get_phone_number_inbound_sip_trunk_config_response_model import (
    GetPhoneNumberInboundSipTrunkConfigResponseModel,
)
from .livekit_stack_type import LivekitStackType

GetPhoneNumberSipTrunkResponseModelProvider = typing.Union[
    typing.Literal["sip_trunk"], typing.Any
]


class GetPhoneNumberSipTrunkResponseModel(BaseModel):
    """GetPhoneNumberSipTrunkResponseModel

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
    :type provider: GetPhoneNumberSipTrunkResponseModelProvider, optional
    :param provider_config: provider_config, defaults to None
    :type provider_config: GetPhoneNumberOutboundSipTrunkConfigResponseModel, optional
    :param outbound_trunk: Configuration of the Outbound SIP trunk - if configured., defaults to None
    :type outbound_trunk: GetPhoneNumberOutboundSipTrunkConfigResponseModel, optional
    :param inbound_trunk: Configuration of the Inbound SIP trunk - if configured., defaults to None
    :type inbound_trunk: GetPhoneNumberInboundSipTrunkConfigResponseModel, optional
    :param livekit_stack: livekit_stack
    :type livekit_stack: LivekitStackType
    :param store_sip_messages: Whether to store SIP messages for this phone number., defaults to None
    :type store_sip_messages: bool, optional
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
    provider: Optional[GetPhoneNumberSipTrunkResponseModelProvider] = Field(
        default=None, description="Phone provider"
    )
    provider_config: Optional[GetPhoneNumberOutboundSipTrunkConfigResponseModel] = (
        Field(default=None)
    )
    outbound_trunk: Optional[GetPhoneNumberOutboundSipTrunkConfigResponseModel] = Field(
        default=None,
        description="Configuration of the Outbound SIP trunk - if configured.",
    )
    inbound_trunk: Optional[GetPhoneNumberInboundSipTrunkConfigResponseModel] = Field(
        default=None,
        description="Configuration of the Inbound SIP trunk - if configured.",
    )
    livekit_stack: LivekitStackType
    store_sip_messages: Optional[bool] = Field(
        default=None, description="Whether to store SIP messages for this phone number."
    )
