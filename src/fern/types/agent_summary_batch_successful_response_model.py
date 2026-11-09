from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .agent_summary_response_model import AgentSummaryResponseModel

AgentSummaryBatchSuccessfulResponseModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class AgentSummaryBatchSuccessfulResponseModel(BaseModel):
    """AgentSummaryBatchSuccessfulResponseModel

    :param status: status
    :type status: AgentSummaryBatchSuccessfulResponseModelStatus
    :param data: data
    :type data: AgentSummaryResponseModel
    """

    status: AgentSummaryBatchSuccessfulResponseModelStatus = Field(default="success")
    data: AgentSummaryResponseModel
