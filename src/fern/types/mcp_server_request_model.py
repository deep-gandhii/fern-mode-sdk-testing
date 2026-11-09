from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .mcp_server_config_input import McpServerConfigInput


class McpServerRequestModel(BaseModel):
    """Request model for creating/updating an MCP Server configuration.

    :param config: config
    :type config: McpServerConfigInput
    """

    config: McpServerConfigInput
