from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AgentTransferOpPopType = typing.Union[typing.Literal["pop"], typing.Any]


class AgentTransferOpPop(BaseModel):
    """AgentTransferOpPop

    :param type: type, defaults to None
    :type type: AgentTransferOpPopType, optional
    """

    type: Optional[AgentTransferOpPopType] = Field(default=None)
