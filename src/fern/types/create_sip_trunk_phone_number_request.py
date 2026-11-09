from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .inbound_sip_trunk_config_request_model import InboundSipTrunkConfigRequestModel
from .outbound_sip_trunk_config_request_model import OutboundSipTrunkConfigRequestModel

CreateSipTrunkPhoneNumberRequestProvider = typing.Union[
    typing.Literal["sip_trunk"], typing.Any
]


class CreateSipTrunkPhoneNumberRequest(BaseModel):
    """CreateSipTrunkPhoneNumberRequest

    :param phone_number: Phone number
    :type phone_number: str
    :param label: Label for the phone number
    :type label: str
    :param supports_inbound: This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls, defaults to None
    :type supports_inbound: bool, optional
    :param supports_outbound: This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls, defaults to None
    :type supports_outbound: bool, optional
    :param provider: provider, defaults to None
    :type provider: CreateSipTrunkPhoneNumberRequestProvider, optional
    :param agent_id: Agent ID to assign the phone number to, defaults to None
    :type agent_id: str, optional
    :param inbound_trunk_config: inbound_trunk_config, defaults to None
    :type inbound_trunk_config: InboundSipTrunkConfigRequestModel, optional
    :param outbound_trunk_config: outbound_trunk_config, defaults to None
    :type outbound_trunk_config: OutboundSipTrunkConfigRequestModel, optional
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
    provider: Optional[CreateSipTrunkPhoneNumberRequestProvider] = Field(default=None)
    agent_id: Optional[str] = Field(
        default=None, description="Agent ID to assign the phone number to"
    )
    inbound_trunk_config: Optional[InboundSipTrunkConfigRequestModel] = Field(
        default=None
    )
    outbound_trunk_config: Optional[OutboundSipTrunkConfigRequestModel] = Field(
        default=None
    )
