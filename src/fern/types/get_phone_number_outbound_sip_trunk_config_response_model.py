from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .sip_trunk_transport_enum import SipTrunkTransportEnum
from .sip_media_encryption_enum import SipMediaEncryptionEnum
from .media_codec import MediaCodec


class GetPhoneNumberOutboundSipTrunkConfigResponseModel(BaseModel):
    """SIP Trunk configuration details for a phone number

    :param address: Hostname or IP the SIP INVITE is sent to
    :type address: str
    :param transport: transport
    :type transport: SipTrunkTransportEnum
    :param media_encryption: media_encryption
    :type media_encryption: SipMediaEncryptionEnum
    :param headers: SIP headers for INVITE request, defaults to None
    :type headers: Dict[str, str], optional
    :param attributes_to_headers: Map of dynamic variable name to header name for attributes_to_headers, defaults to None
    :type attributes_to_headers: Dict[str, str], optional
    :param has_auth_credentials: Whether authentication credentials are configured
    :type has_auth_credentials: bool
    :param username: SIP trunk username (if available), defaults to None
    :type username: str, optional
    :param has_outbound_trunk: Whether a LiveKit SIP outbound trunk is configured, defaults to None
    :type has_outbound_trunk: bool, optional
    :param enabled_codecs: Media codecs that are offered in the SDP for outbound calls. If empty, all supported codecs are offered., defaults to None
    :type enabled_codecs: List[MediaCodec], optional
    """

    address: str = Field(description="Hostname or IP the SIP INVITE is sent to")
    transport: SipTrunkTransportEnum
    media_encryption: SipMediaEncryptionEnum
    headers: Optional[Dict[str, str]] = Field(
        default=None, description="SIP headers for INVITE request"
    )
    attributes_to_headers: Optional[Dict[str, str]] = Field(
        default=None,
        description="Map of dynamic variable name to header name for attributes_to_headers",
    )
    has_auth_credentials: bool = Field(
        description="Whether authentication credentials are configured"
    )
    username: Optional[str] = Field(
        default=None, description="SIP trunk username (if available)"
    )
    has_outbound_trunk: Optional[bool] = Field(
        default=None, description="Whether a LiveKit SIP outbound trunk is configured"
    )
    enabled_codecs: Optional[List[MediaCodec]] = Field(
        default=None,
        description="Media codecs that are offered in the SDP for outbound calls. If empty, all supported codecs are offered.",
    )
