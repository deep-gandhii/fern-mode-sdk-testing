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
from .content_format import ContentFormat
from .external_file_sync_info import ExternalFileSyncInfo
from .auto_sync_info import AutoSyncInfo
from .file_refresh_status import FileRefreshStatus

GetKnowledgeBaseFileResponseModelType = typing.Union[typing.Literal["file"], typing.Any]


class GetKnowledgeBaseFileResponseModel(BaseModel):
    """GetKnowledgeBaseFileResponseModel

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
    :type type: GetKnowledgeBaseFileResponseModelType
    :param extracted_inner_html: extracted_inner_html
    :type extracted_inner_html: str
    :param content_format: Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML., defaults to None
    :type content_format: ContentFormat, optional
    :param filename: filename
    :type filename: str
    :param external_sync_info: external_sync_info, defaults to None
    :type external_sync_info: ExternalFileSyncInfo, optional
    :param auto_sync_info: auto_sync_info, defaults to None
    :type auto_sync_info: AutoSyncInfo, optional
    :param refresh_status: In-flight or last refresh state for an externally-synced file. Used by clients to render sync progress and disable re-sync while a refresh is queued or processing., defaults to None
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
    folder_path: Optional[List[KnowledgeBaseFolderPathSegmentResponseModel]] = Field(
        default=None,
        description="The folder path segments leading to this entity, from root to parent folder.",
    )
    type: GetKnowledgeBaseFileResponseModelType = Field(default="file")
    extracted_inner_html: str
    content_format: Optional[ContentFormat] = Field(
        default=None,
        description="Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML.",
    )
    filename: str
    external_sync_info: Optional[ExternalFileSyncInfo] = Field(default=None)
    auto_sync_info: Optional[AutoSyncInfo] = Field(default=None)
    refresh_status: Optional[FileRefreshStatus] = Field(
        default=None,
        description="In-flight or last refresh state for an externally-synced file. Used by clients to render sync progress and disable re-sync while a refresh is queued or processing.",
    )
    is_frozen: Optional[bool] = Field(default=None)
