from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class LlmUsageCalculatorPublicRequestModel(BaseModel):
    """LlmUsageCalculatorPublicRequestModel

    :param prompt_length: Length of the prompt in characters.
    :type prompt_length: int
    :param number_of_pages: Pages of content in PDF documents or URLs in the agent's knowledge base.
    :type number_of_pages: int
    :param rag_enabled: Whether RAG is enabled.
    :type rag_enabled: bool
    """

    prompt_length: int = Field(description="Length of the prompt in characters.")
    number_of_pages: int = Field(
        description="Pages of content in PDF documents or URLs in the agent's knowledge base."
    )
    rag_enabled: bool = Field(description="Whether RAG is enabled.")
