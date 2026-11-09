from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .tool import Tool


class ListMcpToolsResponseModel(BaseModel):
    """Response model for testing tools available on an MCP server.

    :param success: Indicates if the operation was successful.
    :type success: bool
    :param tools: A list of tools available on the MCP server.
    :type tools: List[Tool]
    :param error_message: Error message if the operation was not successful., defaults to None
    :type error_message: str, optional
    """

    success: bool = Field(description="Indicates if the operation was successful.")
    tools: List[Tool] = Field(
        description="A list of tools available on the MCP server."
    )
    error_message: Optional[str] = Field(
        default=None, description="Error message if the operation was not successful."
    )
