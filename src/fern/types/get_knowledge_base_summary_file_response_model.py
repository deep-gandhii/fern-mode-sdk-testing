from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .knowledge_base_document_metadata_response_model import (
    KnowledgeBaseDocumentMetadataResponseModel,
)
from .document_usage_mode_enum import DocumentUsageModeEnum
from .resource_access_info import ResourceAccessInfo
from .knowledge_base_folder_path_segment_summary_response_model import (
    KnowledgeBaseFolderPathSegmentSummaryResponseModel,
)
from .external_file_sync_info import ExternalFileSyncInfo
from .auto_sync_info import AutoSyncInfo
from .file_refresh_status import FileRefreshStatus
from .dependent_available_agent_identifier import DependentAvailableAgentIdentifier
from .dependent_unknown_agent_identifier import DependentUnknownAgentIdentifier


# fernMode variant type for a shared-component member of GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem
class GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem_Available(
    DependentAvailableAgentIdentifier
):
    pass


# fernMode variant type for a shared-component member of GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem
class GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem_Unknown(
    DependentUnknownAgentIdentifier
):
    pass


# Union type for GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem
# Pydantic will attempt to validate against each type in order
GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem = Union[
    DependentAvailableAgentIdentifier, DependentUnknownAgentIdentifier
]
# TypeAdapter for runtime validation of GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem_adapter = TypeAdapter(
    GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem
)


GetKnowledgeBaseSummaryFileResponseModelType = typing.Union[
    typing.Literal["file"], typing.Any
]


class GetKnowledgeBaseSummaryFileResponseModel(BaseModel):
    """GetKnowledgeBaseSummaryFileResponseModel

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param metadata: metadata
    :type metadata: KnowledgeBaseDocumentMetadataResponseModel
    :param supported_usages: supported_usages
    :type supported_usages: List[DocumentUsageModeEnum]
    :param access_info: access_info
    :type access_info: ResourceAccessInfo
    :param folder_parent_id: The ID of the parent folder, or null if the document is at the root level., defaults to None
    :type folder_parent_id: str, optional
    :param folder_path: The folder path segments leading to this entity, from root to parent folder., defaults to None
    :type folder_path: List[KnowledgeBaseFolderPathSegmentSummaryResponseModel], optional
    :param dependent_agents: This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead.
    :type dependent_agents: List[GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem]
    :param type: type
    :type type: GetKnowledgeBaseSummaryFileResponseModelType
    :param external_sync_info: external_sync_info, defaults to None
    :type external_sync_info: ExternalFileSyncInfo, optional
    :param auto_sync_info: auto_sync_info, defaults to None
    :type auto_sync_info: AutoSyncInfo, optional
    :param refresh_status: refresh_status, defaults to None
    :type refresh_status: FileRefreshStatus, optional
    :param is_frozen: is_frozen, defaults to None
    :type is_frozen: bool, optional
    """

    id: str
    name: str
    metadata: KnowledgeBaseDocumentMetadataResponseModel
    supported_usages: List[DocumentUsageModeEnum]
    access_info: ResourceAccessInfo
    folder_parent_id: Optional[str] = Field(
        default=None,
        description="The ID of the parent folder, or null if the document is at the root level.",
    )
    folder_path: Optional[List[KnowledgeBaseFolderPathSegmentSummaryResponseModel]] = (
        Field(
            default=None,
            description="The folder path segments leading to this entity, from root to parent folder.",
        )
    )
    dependent_agents: List[
        GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem
    ] = Field(
        description="This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead."
    )
    type: GetKnowledgeBaseSummaryFileResponseModelType = Field(default="file")
    external_sync_info: Optional[ExternalFileSyncInfo] = Field(default=None)
    auto_sync_info: Optional[AutoSyncInfo] = Field(default=None)
    refresh_status: Optional[FileRefreshStatus] = Field(default=None)
    is_frozen: Optional[bool] = Field(default=None)
