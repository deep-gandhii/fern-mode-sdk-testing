from __future__ import annotations
import typing
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .get_knowledge_base_summary_url_response_model import (
    GetKnowledgeBaseSummaryUrlResponseModel,
)
from .get_knowledge_base_summary_file_response_model import (
    GetKnowledgeBaseSummaryFileResponseModel,
)
from .get_knowledge_base_summary_text_response_model import (
    GetKnowledgeBaseSummaryTextResponseModel,
)
from .get_knowledge_base_summary_folder_response_model import (
    GetKnowledgeBaseSummaryFolderResponseModel,
)

KnowledgeBaseSummaryBatchSuccessfulResponseModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


# fernMode variant type for a shared-component member of KnowledgeBaseSummaryBatchSuccessfulResponseModelData
class KnowledgeBaseSummaryBatchSuccessfulResponseModelData_Url(
    GetKnowledgeBaseSummaryUrlResponseModel
):
    pass


# fernMode variant type for a shared-component member of KnowledgeBaseSummaryBatchSuccessfulResponseModelData
class KnowledgeBaseSummaryBatchSuccessfulResponseModelData_File(
    GetKnowledgeBaseSummaryFileResponseModel
):
    pass


# fernMode variant type for a shared-component member of KnowledgeBaseSummaryBatchSuccessfulResponseModelData
class KnowledgeBaseSummaryBatchSuccessfulResponseModelData_Text(
    GetKnowledgeBaseSummaryTextResponseModel
):
    pass


# fernMode variant type for a shared-component member of KnowledgeBaseSummaryBatchSuccessfulResponseModelData
class KnowledgeBaseSummaryBatchSuccessfulResponseModelData_Folder(
    GetKnowledgeBaseSummaryFolderResponseModel
):
    pass


# Union type for KnowledgeBaseSummaryBatchSuccessfulResponseModelData
# Pydantic will attempt to validate against each type in order
KnowledgeBaseSummaryBatchSuccessfulResponseModelData = Union[
    GetKnowledgeBaseSummaryUrlResponseModel,
    GetKnowledgeBaseSummaryFileResponseModel,
    GetKnowledgeBaseSummaryTextResponseModel,
    GetKnowledgeBaseSummaryFolderResponseModel,
]
# TypeAdapter for runtime validation of KnowledgeBaseSummaryBatchSuccessfulResponseModelData
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

KnowledgeBaseSummaryBatchSuccessfulResponseModelData_adapter = TypeAdapter(
    KnowledgeBaseSummaryBatchSuccessfulResponseModelData
)


class KnowledgeBaseSummaryBatchSuccessfulResponseModel(BaseModel):
    """KnowledgeBaseSummaryBatchSuccessfulResponseModel

    :param status: status
    :type status: KnowledgeBaseSummaryBatchSuccessfulResponseModelStatus
    :param data: data
    :type data: KnowledgeBaseSummaryBatchSuccessfulResponseModelData
    """

    status: KnowledgeBaseSummaryBatchSuccessfulResponseModelStatus = Field(
        default="success"
    )
    data: KnowledgeBaseSummaryBatchSuccessfulResponseModelData
