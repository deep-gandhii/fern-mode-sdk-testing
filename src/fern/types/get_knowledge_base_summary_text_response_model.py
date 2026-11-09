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
from .dependent_available_agent_identifier import DependentAvailableAgentIdentifier
from .dependent_unknown_agent_identifier import DependentUnknownAgentIdentifier


# fernMode variant type for a shared-component member of GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem
class GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem_Available(
    DependentAvailableAgentIdentifier
):
    pass


# fernMode variant type for a shared-component member of GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem
class GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem_Unknown(
    DependentUnknownAgentIdentifier
):
    pass


# Union type for GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem
# Pydantic will attempt to validate against each type in order
GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem = Union[
    DependentAvailableAgentIdentifier, DependentUnknownAgentIdentifier
]
# TypeAdapter for runtime validation of GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem_adapter = TypeAdapter(
    GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem
)


GetKnowledgeBaseSummaryTextResponseModelType = typing.Union[
    typing.Literal["text"], typing.Any
]


class GetKnowledgeBaseSummaryTextResponseModel(BaseModel):
    """GetKnowledgeBaseSummaryTextResponseModel

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
    :type dependent_agents: List[GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem]
    :param type: type
    :type type: GetKnowledgeBaseSummaryTextResponseModelType
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
        GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem
    ] = Field(
        description="This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead."
    )
    type: GetKnowledgeBaseSummaryTextResponseModelType = Field(default="text")
