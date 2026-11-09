from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

SipUriDynamicVariableTransferDestinationType = typing.Union[
    typing.Literal["sip_uri_dynamic_variable"], typing.Any
]


class SipUriDynamicVariableTransferDestination(BaseModel):
    """SipUriDynamicVariableTransferDestination

    :param type: type, defaults to None
    :type type: SipUriDynamicVariableTransferDestinationType, optional
    :param sip_uri: sip_uri
    :type sip_uri: str
    """

    type: Optional[SipUriDynamicVariableTransferDestinationType] = Field(default=None)
    sip_uri: str
