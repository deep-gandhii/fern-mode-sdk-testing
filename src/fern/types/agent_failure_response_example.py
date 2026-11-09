from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AgentFailureResponseExampleType = typing.Union[typing.Literal["failure"], typing.Any]


class AgentFailureResponseExample(BaseModel):
    """AgentFailureResponseExample

    :param response: response
    :type response: str
    :param type: type
    :type type: AgentFailureResponseExampleType
    """

    response: str
    type: AgentFailureResponseExampleType = Field(default="failure")
