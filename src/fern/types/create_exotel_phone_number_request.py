from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .exotel_api_subdomain import ExotelApiSubdomain

CreateExotelPhoneNumberRequestProvider = typing.Union[
    typing.Literal["exotel"], typing.Any
]


class CreateExotelPhoneNumberRequest(BaseModel):
    """CreateExotelPhoneNumberRequest

    :param phone_number: Phone number
    :type phone_number: str
    :param label: Label for the phone number
    :type label: str
    :param supports_inbound: This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls, defaults to None
    :type supports_inbound: bool, optional
    :param supports_outbound: This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls, defaults to None
    :type supports_outbound: bool, optional
    :param provider: provider, defaults to None
    :type provider: CreateExotelPhoneNumberRequestProvider, optional
    :param agent_id: Agent ID to assign the phone number to, defaults to None
    :type agent_id: str, optional
    :param account_sid: Exotel Account SID
    :type account_sid: str
    :param api_key: Exotel API Key
    :type api_key: str
    :param api_token: Exotel API Token
    :type api_token: str
    :param api_subdomain: api_subdomain
    :type api_subdomain: ExotelApiSubdomain
    :param app_id: Exotel applet identifier used in Calls/connect
    :type app_id: str
    :param applet_url: Optional full applet URL override. Defaults to Exotel start_voice URL derived from account SID and app ID., defaults to None
    :type applet_url: str, optional
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
    provider: Optional[CreateExotelPhoneNumberRequestProvider] = Field(default=None)
    agent_id: Optional[str] = Field(
        default=None, description="Agent ID to assign the phone number to"
    )
    account_sid: str = Field(description="Exotel Account SID")
    api_key: str = Field(description="Exotel API Key")
    api_token: str = Field(description="Exotel API Token")
    api_subdomain: ExotelApiSubdomain
    app_id: str = Field(description="Exotel applet identifier used in Calls/connect")
    applet_url: Optional[str] = Field(
        default=None,
        description="Optional full applet URL override. Defaults to Exotel start_voice URL derived from account SID and app ID.",
    )
