from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .mcp_server_response_model import McpServerResponseModel


class McpServersResponseModel(BaseModel):
    """Response model for a list of MCP Server configurations.

    :param mcp_servers: mcp_servers
    :type mcp_servers: List[McpServerResponseModel]
    """

    mcp_servers: List[McpServerResponseModel]
