from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

BatchFailureResponseModelStatus = typing.Union[typing.Literal["failure"], typing.Any]


class BatchFailureResponseModel(BaseModel):
    """BatchFailureResponseModel

    :param status: status
    :type status: BatchFailureResponseModelStatus
    :param error_code: error_code
    :type error_code: int
    :param error_status: error_status
    :type error_status: str
    :param error_message: error_message
    :type error_message: str
    """

    status: BatchFailureResponseModelStatus = Field(default="failure")
    error_code: int
    error_status: str
    error_message: str
