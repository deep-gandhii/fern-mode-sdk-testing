from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TransferToAgentToolResultErrorModelResultType = typing.Union[
    typing.Literal["transfer_to_agent_error"], typing.Any
]

TransferToAgentToolResultErrorModelStatus = typing.Union[
    typing.Literal["error"], typing.Any
]


class TransferToAgentToolResultErrorModel(BaseModel):
    """TransferToAgentToolResultErrorModel

    :param result_type: result_type, defaults to None
    :type result_type: TransferToAgentToolResultErrorModelResultType, optional
    :param status: status, defaults to None
    :type status: TransferToAgentToolResultErrorModelStatus, optional
    :param from_agent: from_agent
    :type from_agent: str
    :param error: error
    :type error: str
    """

    result_type: Optional[TransferToAgentToolResultErrorModelResultType] = Field(
        default=None
    )
    status: Optional[TransferToAgentToolResultErrorModelStatus] = Field(default=None)
    from_agent: str
    error: str
