from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

UuiTransferConfigProtocolDiscriminatorMode = typing.Union[
    typing.Literal["prefix", "pd_parameter"], typing.Any
]


class UuiTransferConfig(BaseModel):
    """User-to-User Information envelope for SIP REFER transfers (RFC 7433). Outbound payloads are hex-encoded (the only encoding RFC 7433 defines). The protocol discriminator axis lets per-platform formats (Talkdesk, Genesys, ...) be expressed by configuration rather than scattered transfer flags. Further axes (ASCII encoding, header name, purpose/content parameters) can be added here without touching the transfer model.

    :param data: UUI payload to send on SIP REFER transfers. Supports inline dynamic variables and is hex-encoded at transfer time.
    :type data: str
    :param protocol_discriminator: Optional one-octet protocol discriminator (two hex digits, e.g. '00'). Required by platforms such as Genesys Cloud, which otherwise strip the first octet of the payload. Leave unset for platforms like Talkdesk that expect a bare hex payload., defaults to None
    :type protocol_discriminator: str, optional
    :param protocol_discriminator_mode: How to attach protocol_discriminator. 'prefix' prepends the octet to the hex payload (User-to-User=XX<hex>;encoding=hex). 'pd_parameter' sends it as a separate parameter (User-to-User=<hex>;pd=XX;encoding=hex). Ignored when protocol_discriminator is unset., defaults to None
    :type protocol_discriminator_mode: UuiTransferConfigProtocolDiscriminatorMode, optional
    """

    data: str = Field(
        description="UUI payload to send on SIP REFER transfers. Supports inline dynamic variables and is hex-encoded at transfer time."
    )
    protocol_discriminator: Optional[str] = Field(
        default=None,
        description="Optional one-octet protocol discriminator (two hex digits, e.g. '00'). Required by platforms such as Genesys Cloud, which otherwise strip the first octet of the payload. Leave unset for platforms like Talkdesk that expect a bare hex payload.",
    )
    protocol_discriminator_mode: Optional[
        UuiTransferConfigProtocolDiscriminatorMode
    ] = Field(
        default=None,
        description="How to attach protocol_discriminator. 'prefix' prepends the octet to the hex payload (User-to-User=XX<hex>;encoding=hex). 'pd_parameter' sends it as a separate parameter (User-to-User=<hex>;pd=XX;encoding=hex). Ignored when protocol_discriminator is unset.",
    )
