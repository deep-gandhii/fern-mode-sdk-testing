from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .rag_document_index_response_model import RagDocumentIndexResponseModel

RagIndexBatchSuccessfulResponseModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class RagIndexBatchSuccessfulResponseModel(BaseModel):
    """RagIndexBatchSuccessfulResponseModel

    :param status: status
    :type status: RagIndexBatchSuccessfulResponseModelStatus
    :param data: data
    :type data: RagDocumentIndexResponseModel
    """

    status: RagIndexBatchSuccessfulResponseModelStatus = Field(default="success")
    data: RagDocumentIndexResponseModel
