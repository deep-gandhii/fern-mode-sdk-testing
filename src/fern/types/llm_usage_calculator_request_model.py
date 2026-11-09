from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class LlmUsageCalculatorRequestModel(BaseModel):
    """LlmUsageCalculatorRequestModel

    :param prompt_length: Length of the prompt in characters., defaults to None
    :type prompt_length: int, optional
    :param number_of_pages: Pages of content in pdf documents OR urls in agent's Knowledge Base., defaults to None
    :type number_of_pages: int, optional
    :param rag_enabled: Whether RAG is enabled., defaults to None
    :type rag_enabled: bool, optional
    """

    prompt_length: Optional[int] = Field(
        default=None, description="Length of the prompt in characters."
    )
    number_of_pages: Optional[int] = Field(
        default=None,
        description="Pages of content in pdf documents OR urls in agent's Knowledge Base.",
    )
    rag_enabled: Optional[bool] = Field(
        default=None, description="Whether RAG is enabled."
    )
