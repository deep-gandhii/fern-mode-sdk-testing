from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .mcp_tool_approval_policy import McpToolApprovalPolicy


class McpToolAddApprovalRequestModel(BaseModel):
    """Request model for adding approval for a single MCP tool.

    :param tool_name: The name of the MCP tool
    :type tool_name: str
    :param tool_description: The description of the MCP tool
    :type tool_description: str
    :param input_schema: The input schema of the MCP tool (the schema defined on the MCP server before ElevenLabs does any extra processing), defaults to None
    :type input_schema: Dict[str, Any], optional
    :param approval_policy: Defines the tool-level approval policy., defaults to None
    :type approval_policy: McpToolApprovalPolicy, optional
    """

    tool_name: str = Field(description="The name of the MCP tool")
    tool_description: str = Field(description="The description of the MCP tool")
    input_schema: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The input schema of the MCP tool (the schema defined on the MCP server before ElevenLabs does any extra processing)",
    )
    approval_policy: Optional[McpToolApprovalPolicy] = Field(
        default=None, description="Defines the tool-level approval policy."
    )
