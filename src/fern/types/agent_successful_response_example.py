from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AgentSuccessfulResponseExampleType = typing.Union[typing.Literal["success"], typing.Any]


class AgentSuccessfulResponseExample(BaseModel):
    """AgentSuccessfulResponseExample

    :param response: response
    :type response: str
    :param type: type
    :type type: AgentSuccessfulResponseExampleType
    """

    response: str
    type: AgentSuccessfulResponseExampleType = Field(default="success")
