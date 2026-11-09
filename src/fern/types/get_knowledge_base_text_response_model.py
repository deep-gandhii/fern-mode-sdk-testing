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

GetKnowledgeBaseTextResponseModelType = typing.Union[typing.Literal["text"], typing.Any]


class GetKnowledgeBaseTextResponseModel(BaseModel):
    """GetKnowledgeBaseTextResponseModel

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
    :type type: GetKnowledgeBaseTextResponseModelType
    :param extracted_inner_html: extracted_inner_html
    :type extracted_inner_html: str
    :param content_format: Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML., defaults to None
    :type content_format: ContentFormat, optional
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
    type: GetKnowledgeBaseTextResponseModelType = Field(default="text")
    extracted_inner_html: str
    content_format: Optional[ContentFormat] = Field(
        default=None,
        description="Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML.",
    )
