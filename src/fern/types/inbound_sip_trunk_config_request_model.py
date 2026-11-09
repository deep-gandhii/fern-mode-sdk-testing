from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .sip_media_encryption_enum import SipMediaEncryptionEnum
from .sip_trunk_credentials_request_model import SipTrunkCredentialsRequestModel


class InboundSipTrunkConfigRequestModel(BaseModel):
    """InboundSipTrunkConfigRequestModel

    :param allowed_addresses: List of IP addresses that are allowed to use the trunk. Each item in the list can be an individual IP address or a Classless Inter-Domain Routing notation representing a CIDR block., defaults to None
    :type allowed_addresses: List[str], optional
    :param allowed_numbers: List of phone numbers that are allowed to use the trunk., defaults to None
    :type allowed_numbers: List[str], optional
    :param media_encryption: media_encryption, defaults to None
    :type media_encryption: SipMediaEncryptionEnum, optional
    :param credentials: Optional digest authentication credentials (username/password)., defaults to None
    :type credentials: SipTrunkCredentialsRequestModel, optional
    :param remote_domains: Domains of remote SIP servers used to validate TLS certificates., defaults to None
    :type remote_domains: List[str], optional
    :param attributes_to_headers: Map of dynamic variable name to header name for attributes_to_headers, defaults to None
    :type attributes_to_headers: Dict[str, str], optional
    """

    allowed_addresses: Optional[List[str]] = Field(
        default=None,
        description="List of IP addresses that are allowed to use the trunk. Each item in the list can be an individual IP address or a Classless Inter-Domain Routing notation representing a CIDR block.",
    )
    allowed_numbers: Optional[List[str]] = Field(
        default=None,
        description="List of phone numbers that are allowed to use the trunk.",
    )
    media_encryption: Optional[SipMediaEncryptionEnum] = Field(default=None)
    credentials: Optional[SipTrunkCredentialsRequestModel] = Field(
        default=None,
        description="Optional digest authentication credentials (username/password).",
    )
    remote_domains: Optional[List[str]] = Field(
        default=None,
        description="Domains of remote SIP servers used to validate TLS certificates.",
    )
    attributes_to_headers: Optional[Dict[str, str]] = Field(
        default=None,
        description="Map of dynamic variable name to header name for attributes_to_headers",
    )
