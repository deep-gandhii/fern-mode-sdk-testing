from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .resource_access_info import ResourceAccessInfo
from .test_type import TestType
from .agent_test_entity_type import AgentTestEntityType
from .agent_test_folder_path_segment_response_model import (
    AgentTestFolderPathSegmentResponseModel,
)
from .conversation_initiation_source import ConversationInitiationSource


class UnitTestSummaryResponseModel(BaseModel):
    """UnitTestSummaryResponseModel

    :param id: The ID of the test
    :type id: str
    :param name: Name of the test
    :type name: str
    :param access_info: The access information of the test, defaults to None
    :type access_info: ResourceAccessInfo, optional
    :param created_at_unix_secs: Creation time of the test in unix seconds
    :type created_at_unix_secs: int
    :param last_updated_at_unix_secs: Last update time of the test in unix seconds
    :type last_updated_at_unix_secs: int
    :param type: type
    :type type: TestType
    :param entity_type: entity_type, defaults to None
    :type entity_type: AgentTestEntityType, optional
    :param folder_parent_id: The ID of the parent folder, defaults to None
    :type folder_parent_id: str, optional
    :param folder_path: The folder path segments from root to this entity, defaults to None
    :type folder_path: List[AgentTestFolderPathSegmentResponseModel], optional
    :param children_count: Number of direct children (tests and subfolders) for folders only, defaults to None
    :type children_count: int, optional
    :param conversation_initiation_source: Channel the test simulates the conversation as. Null for folders or default behavior., defaults to None
    :type conversation_initiation_source: ConversationInitiationSource, optional
    """

    id: str = Field(description="The ID of the test")
    name: str = Field(description="Name of the test")
    access_info: Optional[ResourceAccessInfo] = Field(
        default=None, description="The access information of the test"
    )
    created_at_unix_secs: int = Field(
        description="Creation time of the test in unix seconds"
    )
    last_updated_at_unix_secs: int = Field(
        description="Last update time of the test in unix seconds"
    )
    type: TestType
    entity_type: Optional[AgentTestEntityType] = Field(default=None)
    folder_parent_id: Optional[str] = Field(
        default=None, description="The ID of the parent folder"
    )
    folder_path: Optional[List[AgentTestFolderPathSegmentResponseModel]] = Field(
        default=None, description="The folder path segments from root to this entity"
    )
    children_count: Optional[int] = Field(
        default=None,
        description="Number of direct children (tests and subfolders) for folders only",
    )
    conversation_initiation_source: Optional[ConversationInitiationSource] = Field(
        default=None,
        description="Channel the test simulates the conversation as. Null for folders or default behavior.",
    )
