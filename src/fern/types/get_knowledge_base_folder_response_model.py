from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .knowledge_base_document_metadata_response_model import (
    KnowledgeBaseDocumentMetadataResponseModel,
)
from .document_usage_mode_enum import DocumentUsageModeEnum
from .resource_access_info import ResourceAccessInfo
from .knowledge_base_folder_path_segment_response_model import (
    KnowledgeBaseFolderPathSegmentResponseModel,
)
from .auto_sync_info import AutoSyncInfo
from .external_folder_sync_info import ExternalFolderSyncInfo
from .kb_external_sync_job import KbExternalSyncJob

GetKnowledgeBaseFolderResponseModelType = typing.Union[
    typing.Literal["folder"], typing.Any
]


class GetKnowledgeBaseFolderResponseModel(BaseModel):
    """GetKnowledgeBaseFolderResponseModel

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
    :type folder_path: List[KnowledgeBaseFolderPathSegmentResponseModel], optional
    :param type: type
    :type type: GetKnowledgeBaseFolderResponseModelType
    :param children_count: children_count
    :type children_count: int
    :param document_count: Number of non-folder documents anywhere in this folder's subtree (recursive). Counting stops past 1000;
    :type document_count: int
    :param auto_sync_info: auto_sync_info, defaults to None
    :type auto_sync_info: AutoSyncInfo, optional
    :param external_sync_info: external_sync_info, defaults to None
    :type external_sync_info: ExternalFolderSyncInfo, optional
    :param is_frozen: is_frozen, defaults to None
    :type is_frozen: bool, optional
    :param active_sync_job: Most recent (in-flight or terminal) external sync job for this folder, if any. Used by clients to render sync progress., defaults to None
    :type active_sync_job: KbExternalSyncJob, optional
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
    folder_path: Optional[List[KnowledgeBaseFolderPathSegmentResponseModel]] = Field(
        default=None,
        description="The folder path segments leading to this entity, from root to parent folder.",
    )
    type: GetKnowledgeBaseFolderResponseModelType = Field(default="folder")
    children_count: int
    document_count: int = Field(
        description="Number of non-folder documents anywhere in this folder's subtree (recursive). Counting stops past 1000;"
    )
    auto_sync_info: Optional[AutoSyncInfo] = Field(default=None)
    external_sync_info: Optional[ExternalFolderSyncInfo] = Field(default=None)
    is_frozen: Optional[bool] = Field(default=None)
    active_sync_job: Optional[KbExternalSyncJob] = Field(
        default=None,
        description="Most recent (in-flight or terminal) external sync job for this folder, if any. Used by clients to render sync progress.",
    )
