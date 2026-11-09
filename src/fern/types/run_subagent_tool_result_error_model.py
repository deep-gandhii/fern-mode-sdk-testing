from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

RunSubagentToolResultErrorModelResultType = typing.Union[
    typing.Literal["run_subagent_error"], typing.Any
]

RunSubagentToolResultErrorModelStatus = typing.Union[
    typing.Literal["error"], typing.Any
]


class RunSubagentToolResultErrorModel(BaseModel):
    """RunSubagentToolResultErrorModel

    :param result_type: result_type, defaults to None
    :type result_type: RunSubagentToolResultErrorModelResultType, optional
    :param status: status, defaults to None
    :type status: RunSubagentToolResultErrorModelStatus, optional
    :param error: error
    :type error: str
    """

    result_type: Optional[RunSubagentToolResultErrorModelResultType] = Field(
        default=None
    )
    status: Optional[RunSubagentToolResultErrorModelStatus] = Field(default=None)
    error: str
