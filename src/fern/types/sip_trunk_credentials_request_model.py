from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SipTrunkCredentialsRequestModel(BaseModel):
    """SipTrunkCredentialsRequestModel

    :param username: SIP trunk username
    :type username: str
    :param password: SIP trunk password - if not specified, then remain unchanged, defaults to None
    :type password: str, optional
    """

    username: str = Field(description="SIP trunk username")
    password: Optional[str] = Field(
        default=None,
        description="SIP trunk password - if not specified, then remain unchanged",
    )
