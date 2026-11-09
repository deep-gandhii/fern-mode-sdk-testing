from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .inbound_sip_trunk_config_request_model import InboundSipTrunkConfigRequestModel
from .outbound_sip_trunk_config_request_model import OutboundSipTrunkConfigRequestModel
from .livekit_stack_type import LivekitStackType


class UpdatePhoneNumberRequest(BaseModel):
    """UpdatePhoneNumberRequest

    :param agent_id: agent_id, defaults to None
    :type agent_id: str, optional
    :param label: label, defaults to None
    :type label: str, optional
    :param inbound_trunk_config: inbound_trunk_config, defaults to None
    :type inbound_trunk_config: InboundSipTrunkConfigRequestModel, optional
    :param outbound_trunk_config: outbound_trunk_config, defaults to None
    :type outbound_trunk_config: OutboundSipTrunkConfigRequestModel, optional
    :param livekit_stack: livekit_stack, defaults to None
    :type livekit_stack: LivekitStackType, optional
    :param store_sip_messages: store_sip_messages, defaults to None
    :type store_sip_messages: bool, optional
    :param environment: Environment to use for resolving environment variables on calls to this number., defaults to None
    :type environment: str, optional
    :param branch_id: Agent branch to use for calls to this number., defaults to None
    :type branch_id: str, optional
    """

    agent_id: Optional[str] = Field(default=None)
    label: Optional[str] = Field(default=None)
    inbound_trunk_config: Optional[InboundSipTrunkConfigRequestModel] = Field(
        default=None
    )
    outbound_trunk_config: Optional[OutboundSipTrunkConfigRequestModel] = Field(
        default=None
    )
    livekit_stack: Optional[LivekitStackType] = Field(default=None)
    store_sip_messages: Optional[bool] = Field(default=None)
    environment: Optional[str] = Field(
        default=None,
        description="Environment to use for resolving environment variables on calls to this number.",
    )
    branch_id: Optional[str] = Field(
        default=None, description="Agent branch to use for calls to this number."
    )
