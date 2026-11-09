from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TestToolResultModelResultType = typing.Union[
    typing.Literal["testing_tool_result"], typing.Any
]

TestToolResultModelStatus = typing.Union[typing.Literal["success"], typing.Any]


class TestToolResultModel(BaseModel):
    """TestToolResultModel

    :param result_type: result_type, defaults to None
    :type result_type: TestToolResultModelResultType, optional
    :param status: status, defaults to None
    :type status: TestToolResultModelStatus, optional
    :param reason: reason, defaults to None
    :type reason: str, optional
    """

    result_type: Optional[TestToolResultModelResultType] = Field(default=None)
    status: Optional[TestToolResultModelStatus] = Field(default=None)
    reason: Optional[str] = Field(default=None)
