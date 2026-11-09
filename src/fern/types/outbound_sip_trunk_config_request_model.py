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
from .sip_trunk_credentials_request_model import SipTrunkCredentialsRequestModel
from .media_codec import MediaCodec


class OutboundSipTrunkConfigRequestModel(BaseModel):
    """OutboundSipTrunkConfigRequestModel

    :param address: Hostname or IP the SIP INVITE is sent to.
    :type address: str
    :param transport: transport, defaults to None
    :type transport: SipTrunkTransportEnum, optional
    :param media_encryption: media_encryption, defaults to None
    :type media_encryption: SipMediaEncryptionEnum, optional
    :param headers: SIP X-* headers for INVITE request. These headers are sent as-is and may help identify this call., defaults to None
    :type headers: Dict[str, str], optional
    :param attributes_to_headers: Map of dynamic variable name to header name for attributes_to_headers, defaults to None
    :type attributes_to_headers: Dict[str, str], optional
    :param credentials: Optional digest authentication credentials (username/password). If not provided, ACL authentication is assumed., defaults to None
    :type credentials: SipTrunkCredentialsRequestModel, optional
    :param enabled_codecs: Media codecs that should be offered in the SDP for outbound calls. If empty, all supported codecs are offered., defaults to None
    :type enabled_codecs: List[MediaCodec], optional
    """

    address: str = Field(description="Hostname or IP the SIP INVITE is sent to.")
    transport: Optional[SipTrunkTransportEnum] = Field(default=None)
    media_encryption: Optional[SipMediaEncryptionEnum] = Field(default=None)
    headers: Optional[Dict[str, str]] = Field(
        default=None,
        description="SIP X-* headers for INVITE request. These headers are sent as-is and may help identify this call.",
    )
    attributes_to_headers: Optional[Dict[str, str]] = Field(
        default=None,
        description="Map of dynamic variable name to header name for attributes_to_headers",
    )
    credentials: Optional[SipTrunkCredentialsRequestModel] = Field(
        default=None,
        description="Optional digest authentication credentials (username/password). If not provided, ACL authentication is assumed.",
    )
    enabled_codecs: Optional[List[MediaCodec]] = Field(
        default=None,
        description="Media codecs that should be offered in the SDP for outbound calls. If empty, all supported codecs are offered.",
    )
