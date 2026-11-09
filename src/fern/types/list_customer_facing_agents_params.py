from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListCustomerFacingAgentsParamsSmbToolType = typing.Union[
    typing.Literal["list_customer_facing_agents"], typing.Any
]


class ListCustomerFacingAgentsParams(BaseModel):
    """List every customer-facing agent on the workspace. The assistant uses this whenever it needs to act on a specific customer-facing agent (rules, config edits, etc.) so it can pick the right ``agent_id`` to pass to mutating tools. Mirrors the ``list_services`` / ``list_clients`` pattern: read once, then mutate by id.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListCustomerFacingAgentsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListCustomerFacingAgentsParamsSmbToolType] = Field(
        default=None
    )
