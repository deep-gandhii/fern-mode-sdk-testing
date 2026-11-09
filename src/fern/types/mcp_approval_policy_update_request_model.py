from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .mcp_approval_policy import McpApprovalPolicy


class McpApprovalPolicyUpdateRequestModel(BaseModel):
    """Request model for updating MCP Server approval mode.

    :param approval_policy: Defines the MCP server-level approval policy for tool execution.
    :type approval_policy: McpApprovalPolicy
    """

    approval_policy: McpApprovalPolicy = Field(
        description="Defines the MCP server-level approval policy for tool execution."
    )
