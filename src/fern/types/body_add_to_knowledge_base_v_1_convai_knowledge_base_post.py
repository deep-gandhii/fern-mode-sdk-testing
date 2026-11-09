from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyAddToKnowledgeBaseV1ConvaiKnowledgeBasePost(BaseModel):
    """BodyAddToKnowledgeBaseV1ConvaiKnowledgeBasePost

    :param name: A custom, human-readable name for the document., defaults to None
    :type name: str, optional
    :param url: URL to a page of documentation that the agent will have access to in order to interact with users., defaults to None
    :type url: str, optional
    :param file: Documentation that the agent will have access to in order to interact with users., defaults to None
    :type file: bytes, optional
    """

    name: Optional[str] = Field(
        default=None, description="A custom, human-readable name for the document."
    )
    url: Optional[str] = Field(
        default=None,
        description="URL to a page of documentation that the agent will have access to in order to interact with users.",
    )
    file: Optional[bytes] = Field(
        default=None,
        description="Documentation that the agent will have access to in order to interact with users.",
    )
