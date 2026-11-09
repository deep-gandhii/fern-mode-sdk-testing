from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

RunSubagentToolResultSuccessModelResultType = typing.Union[
    typing.Literal["run_subagent_success"], typing.Any
]

RunSubagentToolResultSuccessModelStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


class RunSubagentToolResultSuccessModel(BaseModel):
    """RunSubagentToolResultSuccessModel

    :param result_type: result_type, defaults to None
    :type result_type: RunSubagentToolResultSuccessModelResultType, optional
    :param status: status, defaults to None
    :type status: RunSubagentToolResultSuccessModelStatus, optional
    :param query: query
    :type query: str
    :param agent_response: agent_response
    :type agent_response: str
    """

    result_type: Optional[RunSubagentToolResultSuccessModelResultType] = Field(
        default=None
    )
    status: Optional[RunSubagentToolResultSuccessModelStatus] = Field(default=None)
    query: str
    agent_response: str
