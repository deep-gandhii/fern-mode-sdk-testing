from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel

ConversationHistoryTranscriptToolCallMcpDetailsType = typing.Union[
    typing.Literal["mcp"], typing.Any
]


class ConversationHistoryTranscriptToolCallMcpDetails(BaseModel):
    """ConversationHistoryTranscriptToolCallMcpDetails

    :param type: type, defaults to None
    :type type: ConversationHistoryTranscriptToolCallMcpDetailsType, optional
    :param mcp_server_id: mcp_server_id
    :type mcp_server_id: str
    :param mcp_server_name: mcp_server_name
    :type mcp_server_name: str
    :param integration_type: integration_type
    :type integration_type: str
    :param parameters: parameters, defaults to None
    :type parameters: Dict[str, str], optional
    :param approval_policy: approval_policy
    :type approval_policy: str
    :param requires_approval: requires_approval, defaults to None
    :type requires_approval: bool, optional
    :param mcp_tool_name: mcp_tool_name, defaults to None
    :type mcp_tool_name: str, optional
    :param mcp_tool_description: mcp_tool_description, defaults to None
    :type mcp_tool_description: str, optional
    """

    type: Optional[ConversationHistoryTranscriptToolCallMcpDetailsType] = Field(
        default=None
    )
    mcp_server_id: str
    mcp_server_name: str
    integration_type: str
    parameters: Optional[Dict[str, str]] = Field(default=None)
    approval_policy: str
    requires_approval: Optional[bool] = Field(default=None)
    mcp_tool_name: Optional[str] = Field(default=None)
    mcp_tool_description: Optional[str] = Field(default=None)
