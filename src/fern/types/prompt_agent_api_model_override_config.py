from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PromptAgentApiModelOverrideConfig(BaseModel):
    """PromptAgentApiModelOverrideConfig

    :param prompt: Whether to allow overriding the prompt field., defaults to None
    :type prompt: bool, optional
    :param llm: Whether to allow overriding the llm field., defaults to None
    :type llm: bool, optional
    :param tool_ids: Whether to allow overriding the tool_ids field., defaults to None
    :type tool_ids: bool, optional
    :param native_mcp_server_ids: Whether to allow overriding the native_mcp_server_ids field., defaults to None
    :type native_mcp_server_ids: bool, optional
    :param knowledge_base: Whether to allow overriding the knowledge_base field., defaults to None
    :type knowledge_base: bool, optional
    """

    prompt: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the prompt field."
    )
    llm: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the llm field."
    )
    tool_ids: Optional[bool] = Field(
        default=None, description="Whether to allow overriding the tool_ids field."
    )
    native_mcp_server_ids: Optional[bool] = Field(
        default=None,
        description="Whether to allow overriding the native_mcp_server_ids field.",
    )
    knowledge_base: Optional[bool] = Field(
        default=None,
        description="Whether to allow overriding the knowledge_base field.",
    )
