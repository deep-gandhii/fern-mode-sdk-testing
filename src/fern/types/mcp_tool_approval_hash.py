from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .mcp_tool_approval_policy import McpToolApprovalPolicy


class McpToolApprovalHash(BaseModel):
    """Model for storing tool approval hashes for per-tool approval.

    :param tool_name: The name of the MCP tool
    :type tool_name: str
    :param tool_hash: SHA256 hash of the tool's parameters and description
    :type tool_hash: str
    :param approval_policy: Defines the tool-level approval policy., defaults to None
    :type approval_policy: McpToolApprovalPolicy, optional
    """

    tool_name: str = Field(description="The name of the MCP tool")
    tool_hash: str = Field(
        description="SHA256 hash of the tool's parameters and description"
    )
    approval_policy: Optional[McpToolApprovalPolicy] = Field(
        default=None, description="Defines the tool-level approval policy."
    )
