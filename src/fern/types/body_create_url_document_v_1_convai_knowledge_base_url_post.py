from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyCreateUrlDocumentV1ConvaiKnowledgeBaseUrlPost(BaseModel):
    """BodyCreateUrlDocumentV1ConvaiKnowledgeBaseUrlPost

    :param url: URL to a page of documentation that the agent will have access to in order to interact with users.
    :type url: str
    :param name: A custom, human-readable name for the document., defaults to None
    :type name: str, optional
    :param parent_folder_id: If set, the created document or folder will be placed inside the given folder., defaults to None
    :type parent_folder_id: str, optional
    :param enable_auto_sync: Whether to enable auto-sync for this URL document., defaults to None
    :type enable_auto_sync: bool, optional
    :param auto_remove: Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled., defaults to None
    :type auto_remove: bool, optional
    """

    url: str = Field(
        description="URL to a page of documentation that the agent will have access to in order to interact with users."
    )
    name: Optional[str] = Field(
        default=None, description="A custom, human-readable name for the document."
    )
    parent_folder_id: Optional[str] = Field(
        default=None,
        description="If set, the created document or folder will be placed inside the given folder.",
    )
    enable_auto_sync: Optional[bool] = Field(
        default=None, description="Whether to enable auto-sync for this URL document."
    )
    auto_remove: Optional[bool] = Field(
        default=None,
        description="Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled.",
    )
