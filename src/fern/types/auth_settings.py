from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .allowlist_item import AllowlistItem


class AuthSettings(BaseModel):
    """AuthSettings

    :param enable_auth: If set to true, starting a conversation with an agent will require a signed token, defaults to None
    :type enable_auth: bool, optional
    :param allowlist: A list of hosts that are allowed to start conversations with the agent, defaults to None
    :type allowlist: List[AllowlistItem], optional
    :param require_origin_header: When enabled, connections with no origin header will be rejected. If the allowlist is empty, this option has no effect., defaults to None
    :type require_origin_header: bool, optional
    :param shareable_token: A shareable token that can be used to start a conversation with the agent, defaults to None
    :type shareable_token: str, optional
    """

    enable_auth: Optional[bool] = Field(
        default=None,
        description="If set to true, starting a conversation with an agent will require a signed token",
    )
    allowlist: Optional[List[AllowlistItem]] = Field(
        default=None,
        description="A list of hosts that are allowed to start conversations with the agent",
    )
    require_origin_header: Optional[bool] = Field(
        default=None,
        description="When enabled, connections with no origin header will be rejected. If the allowlist is empty, this option has no effect.",
    )
    shareable_token: Optional[str] = Field(
        default=None,
        description="A shareable token that can be used to start a conversation with the agent",
    )
