from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

SipUriTransferDestinationType = typing.Union[typing.Literal["sip_uri"], typing.Any]


class SipUriTransferDestination(BaseModel):
    """SipUriTransferDestination

    :param type: type, defaults to None
    :type type: SipUriTransferDestinationType, optional
    :param sip_uri: sip_uri
    :type sip_uri: str
    """

    type: Optional[SipUriTransferDestinationType] = Field(default=None)
    sip_uri: str
