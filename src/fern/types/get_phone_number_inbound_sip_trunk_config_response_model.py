from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .sip_media_encryption_enum import SipMediaEncryptionEnum


class GetPhoneNumberInboundSipTrunkConfigResponseModel(BaseModel):
    """GetPhoneNumberInboundSipTrunkConfigResponseModel

    :param allowed_addresses: List of IP addresses that are allowed to use the trunk. Each item in the list can be an individual IP address or a Classless Inter-Domain Routing notation representing a CIDR block.
    :type allowed_addresses: List[str]
    :param allowed_numbers: List of phone numbers that are allowed to use the trunk.
    :type allowed_numbers: List[str]
    :param media_encryption: media_encryption
    :type media_encryption: SipMediaEncryptionEnum
    :param has_auth_credentials: Whether authentication credentials are configured
    :type has_auth_credentials: bool
    :param username: SIP trunk username (if available), defaults to None
    :type username: str, optional
    :param remote_domains: Domains of remote SIP servers used to validate TLS certificates., defaults to None
    :type remote_domains: List[str], optional
    :param attributes_to_headers: Map of dynamic variable name to header name for attributes_to_headers, defaults to None
    :type attributes_to_headers: Dict[str, str], optional
    """

    allowed_addresses: List[str] = Field(
        description="List of IP addresses that are allowed to use the trunk. Each item in the list can be an individual IP address or a Classless Inter-Domain Routing notation representing a CIDR block."
    )
    allowed_numbers: Optional[List[str]] = Field(
        description="List of phone numbers that are allowed to use the trunk."
    )
    media_encryption: SipMediaEncryptionEnum
    has_auth_credentials: bool = Field(
        description="Whether authentication credentials are configured"
    )
    username: Optional[str] = Field(
        default=None, description="SIP trunk username (if available)"
    )
    remote_domains: Optional[List[str]] = Field(
        default=None,
        description="Domains of remote SIP servers used to validate TLS certificates.",
    )
    attributes_to_headers: Optional[Dict[str, str]] = Field(
        default=None,
        description="Map of dynamic variable name to header name for attributes_to_headers",
    )
