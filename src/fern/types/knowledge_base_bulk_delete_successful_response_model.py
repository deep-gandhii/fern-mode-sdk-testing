from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .knowledge_base_deleted_response_model import KnowledgeBaseDeletedResponseModel

KnowledgeBaseBulkDeleteSuccessfulResponseModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class KnowledgeBaseBulkDeleteSuccessfulResponseModel(BaseModel):
    """KnowledgeBaseBulkDeleteSuccessfulResponseModel

    :param status: status
    :type status: KnowledgeBaseBulkDeleteSuccessfulResponseModelStatus
    :param data: data
    :type data: KnowledgeBaseDeletedResponseModel
    """

    status: KnowledgeBaseBulkDeleteSuccessfulResponseModelStatus = Field(
        default="success"
    )
    data: KnowledgeBaseDeletedResponseModel
