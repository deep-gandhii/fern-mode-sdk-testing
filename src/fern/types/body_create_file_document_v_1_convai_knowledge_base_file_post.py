from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyCreateFileDocumentV1ConvaiKnowledgeBaseFilePost(BaseModel):
    """BodyCreateFileDocumentV1ConvaiKnowledgeBaseFilePost

    :param file: Documentation that the agent will have access to in order to interact with users.
    :type file: bytes
    :param name: A custom, human-readable name for the document., defaults to None
    :type name: str, optional
    :param parent_folder_id: If set, the created document or folder will be placed inside the given folder., defaults to None
    :type parent_folder_id: str, optional
    """

    file: bytes = Field(
        description="Documentation that the agent will have access to in order to interact with users."
    )
    name: Optional[str] = Field(
        default=None, description="A custom, human-readable name for the document."
    )
    parent_folder_id: Optional[str] = Field(
        default=None,
        description="If set, the created document or folder will be placed inside the given folder.",
    )
