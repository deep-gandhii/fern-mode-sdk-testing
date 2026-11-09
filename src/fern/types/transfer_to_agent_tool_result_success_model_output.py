from __future__ import annotations
import typing
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .transfer_branch_info_traffic_split import TransferBranchInfoTrafficSplit
from .transfer_branch_info_defaulting_to_main import TransferBranchInfoDefaultingToMain

TransferToAgentToolResultSuccessModelOutputResultType = typing.Union[
    typing.Literal["transfer_to_agent_success"], typing.Any
]

TransferToAgentToolResultSuccessModelOutputStatus = typing.Union[
    typing.Literal["success"], typing.Any
]


# fernMode variant type for a shared-component member of TransferToAgentToolResultSuccessModelOutputBranchInfo
class TransferToAgentToolResultSuccessModelOutputBranchInfo_TrafficSplit(
    TransferBranchInfoTrafficSplit
):
    pass


# fernMode variant type for a shared-component member of TransferToAgentToolResultSuccessModelOutputBranchInfo
class TransferToAgentToolResultSuccessModelOutputBranchInfo_DefaultingToMain(
    TransferBranchInfoDefaultingToMain
):
    pass


# Union type for TransferToAgentToolResultSuccessModelOutputBranchInfo
# Pydantic will attempt to validate against each type in order
TransferToAgentToolResultSuccessModelOutputBranchInfo = Union[
    TransferBranchInfoTrafficSplit, TransferBranchInfoDefaultingToMain
]
# TypeAdapter for runtime validation of TransferToAgentToolResultSuccessModelOutputBranchInfo
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

TransferToAgentToolResultSuccessModelOutputBranchInfo_adapter = TypeAdapter(
    TransferToAgentToolResultSuccessModelOutputBranchInfo
)


class TransferToAgentToolResultSuccessModelOutput(BaseModel):
    """TransferToAgentToolResultSuccessModelOutput

    :param result_type: result_type, defaults to None
    :type result_type: TransferToAgentToolResultSuccessModelOutputResultType, optional
    :param status: status, defaults to None
    :type status: TransferToAgentToolResultSuccessModelOutputStatus, optional
    :param from_agent: from_agent
    :type from_agent: str
    :param to_agent: to_agent
    :type to_agent: str
    :param to_node: to_node, defaults to None
    :type to_node: str, optional
    :param condition: condition
    :type condition: str
    :param delay_ms: delay_ms, defaults to None
    :type delay_ms: int, optional
    :param transfer_message: transfer_message, defaults to None
    :type transfer_message: str, optional
    :param enable_transferred_agent_first_message: enable_transferred_agent_first_message, defaults to None
    :type enable_transferred_agent_first_message: bool, optional
    :param branch_info: branch_info, defaults to None
    :type branch_info: TransferToAgentToolResultSuccessModelOutputBranchInfo, optional
    :param preserve_client_tts_overrides: preserve_client_tts_overrides, defaults to None
    :type preserve_client_tts_overrides: bool, optional
    """

    result_type: Optional[TransferToAgentToolResultSuccessModelOutputResultType] = (
        Field(default=None)
    )
    status: Optional[TransferToAgentToolResultSuccessModelOutputStatus] = Field(
        default=None
    )
    from_agent: str
    to_agent: str
    to_node: Optional[str] = Field(default=None)
    condition: str
    delay_ms: Optional[int] = Field(default=None)
    transfer_message: Optional[str] = Field(default=None)
    enable_transferred_agent_first_message: Optional[bool] = Field(default=None)
    branch_info: Optional[TransferToAgentToolResultSuccessModelOutputBranchInfo] = (
        Field(default=None)
    )
    preserve_client_tts_overrides: Optional[bool] = Field(default=None)
