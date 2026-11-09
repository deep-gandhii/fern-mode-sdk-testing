from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .conversation_config_client_override_config_output import (
    ConversationConfigClientOverrideConfigOutput,
)


class ConversationInitiationClientDataConfigOutput(BaseModel):
    """ConversationInitiationClientDataConfigOutput

    :param conversation_config_override: conversation_config_override, defaults to None
    :type conversation_config_override: ConversationConfigClientOverrideConfigOutput, optional
    :param custom_llm_extra_body: Whether to include custom LLM extra body, defaults to None
    :type custom_llm_extra_body: bool, optional
    :param enable_conversation_initiation_client_data_from_webhook: Whether to enable conversation initiation client data from webhooks, defaults to None
    :type enable_conversation_initiation_client_data_from_webhook: bool, optional
    :param enable_starting_workflow_node_id_from_client: Whether clients may pass starting_workflow_node_id in initiation client data; if false, sending it fails conversation start., defaults to None
    :type enable_starting_workflow_node_id_from_client: bool, optional
    """

    conversation_config_override: Optional[
        ConversationConfigClientOverrideConfigOutput
    ] = Field(default=None)
    custom_llm_extra_body: Optional[bool] = Field(
        default=None, description="Whether to include custom LLM extra body"
    )
    enable_conversation_initiation_client_data_from_webhook: Optional[bool] = Field(
        default=None,
        description="Whether to enable conversation initiation client data from webhooks",
    )
    enable_starting_workflow_node_id_from_client: Optional[bool] = Field(
        default=None,
        description="Whether clients may pass starting_workflow_node_id in initiation client data; if false, sending it fails conversation start.",
    )
