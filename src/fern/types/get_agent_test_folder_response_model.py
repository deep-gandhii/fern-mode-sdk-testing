from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .agent_test_folder_path_segment_response_model import (
    AgentTestFolderPathSegmentResponseModel,
)


class GetAgentTestFolderResponseModel(BaseModel):
    """GetAgentTestFolderResponseModel

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param folder_path: The path from the root folder to the current folder., defaults to None
    :type folder_path: List[AgentTestFolderPathSegmentResponseModel], optional
    :param children_count: The number of direct children (tests and subfolders) in this folder, defaults to None
    :type children_count: int, optional
    """

    id: str
    name: str
    folder_path: Optional[List[AgentTestFolderPathSegmentResponseModel]] = Field(
        default=None, description="The path from the root folder to the current folder."
    )
    children_count: Optional[int] = Field(
        default=None,
        description="The number of direct children (tests and subfolders) in this folder",
    )
