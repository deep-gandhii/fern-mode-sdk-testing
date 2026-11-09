from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .llm import Llm
from .knowledge_base_locator import KnowledgeBaseLocator


class PromptAgentApiModelOverrideOutput(BaseModel):
    """PromptAgentApiModelOverrideOutput

    :param prompt: The prompt for the agent, defaults to None
    :type prompt: str, optional
    :param llm: The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment, defaults to None
    :type llm: Llm, optional
    :param tool_ids: A list of IDs of tools used by the agent, defaults to None
    :type tool_ids: List[str], optional
    :param native_mcp_server_ids: A list of Native MCP server ids to be used by the agent, defaults to None
    :type native_mcp_server_ids: List[str], optional
    :param knowledge_base: A list of knowledge bases to be used by the agent, defaults to None
    :type knowledge_base: List[KnowledgeBaseLocator], optional
    """

    prompt: Optional[str] = Field(default=None, description="The prompt for the agent")
    llm: Optional[Llm] = Field(
        default=None,
        description="The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment",
    )
    tool_ids: Optional[List[str]] = Field(
        default=None, description="A list of IDs of tools used by the agent"
    )
    native_mcp_server_ids: Optional[List[str]] = Field(
        default=None,
        description="A list of Native MCP server ids to be used by the agent",
    )
    knowledge_base: Optional[List[KnowledgeBaseLocator]] = Field(
        default=None, description="A list of knowledge bases to be used by the agent"
    )
