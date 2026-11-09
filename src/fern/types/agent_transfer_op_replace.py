from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AgentTransferOpReplaceType = typing.Union[typing.Literal["replace"], typing.Any]


class AgentTransferOpReplace(BaseModel):
    """AgentTransferOpReplace

    :param type: type, defaults to None
    :type type: AgentTransferOpReplaceType, optional
    """

    type: Optional[AgentTransferOpReplaceType] = Field(default=None)
