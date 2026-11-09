from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyCreateFolderV1ConvaiKnowledgeBaseFolderPost(BaseModel):
    """BodyCreateFolderV1ConvaiKnowledgeBaseFolderPost

    :param name: A custom, human-readable name for the document.
    :type name: str
    :param parent_folder_id: If set, the created document or folder will be placed inside the given folder., defaults to None
    :type parent_folder_id: str, optional
    :param enable_auto_sync: Whether to enable auto-sync for this URL document., defaults to None
    :type enable_auto_sync: bool, optional
    :param auto_remove: Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled., defaults to None
    :type auto_remove: bool, optional
    """

    name: str = Field(description="A custom, human-readable name for the document.")
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
