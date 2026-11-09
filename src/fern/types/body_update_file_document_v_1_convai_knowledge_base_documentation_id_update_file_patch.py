from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyUpdateFileDocumentV1ConvaiKnowledgeBaseDocumentationIdUpdateFilePatch(
    BaseModel
):
    """BodyUpdateFileDocumentV1ConvaiKnowledgeBaseDocumentationIdUpdateFilePatch

    :param file: Documentation that the agent will have access to in order to interact with users.
    :type file: bytes
    """

    file: bytes = Field(
        description="Documentation that the agent will have access to in order to interact with users."
    )
