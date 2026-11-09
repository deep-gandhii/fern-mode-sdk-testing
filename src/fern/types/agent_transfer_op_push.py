from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

AgentTransferOpPushType = typing.Union[typing.Literal["push"], typing.Any]


class AgentTransferOpPush(BaseModel):
    """AgentTransferOpPush

    :param type: type, defaults to None
    :type type: AgentTransferOpPushType, optional
    :param return_node_id: return_node_id, defaults to None
    :type return_node_id: str, optional
    """

    type: Optional[AgentTransferOpPushType] = Field(default=None)
    return_node_id: Optional[str] = Field(default=None)
