from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyCreateAgentTestFolderV1ConvaiAgentTestingFoldersPost(BaseModel):
    """BodyCreateAgentTestFolderV1ConvaiAgentTestingFoldersPost

    :param name: The name of the folder to create
    :type name: str
    :param parent_folder_id: The ID of the parent folder. If not provided, the folder will be created at the root level., defaults to None
    :type parent_folder_id: str, optional
    """

    name: str = Field(description="The name of the folder to create")
    parent_folder_id: Optional[str] = Field(
        default=None,
        description="The ID of the parent folder. If not provided, the folder will be created at the root level.",
    )
