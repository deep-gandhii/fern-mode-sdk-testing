from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .conversational_config import ConversationalConfig
from .agent_metadata_response_model import AgentMetadataResponseModel
from .agent_platform_settings_response_model import AgentPlatformSettingsResponseModel
from .get_whats_app_account_response import GetWhatsAppAccountResponse
from .agent_workflow_response_model import AgentWorkflowResponseModel
from .resource_access_info import ResourceAccessInfo
from .get_phone_number_twilio_response_model import GetPhoneNumberTwilioResponseModel
from .get_phone_number_exotel_response_model import GetPhoneNumberExotelResponseModel
from .get_phone_number_sip_trunk_response_model import (
    GetPhoneNumberSipTrunkResponseModel,
)


# fernMode variant type for a shared-component member of GetAgentResponseModelPhoneNumbersItem
class GetAgentResponseModelPhoneNumbersItem_Twilio(GetPhoneNumberTwilioResponseModel):
    pass


# fernMode variant type for a shared-component member of GetAgentResponseModelPhoneNumbersItem
class GetAgentResponseModelPhoneNumbersItem_Exotel(GetPhoneNumberExotelResponseModel):
    pass


# fernMode variant type for a shared-component member of GetAgentResponseModelPhoneNumbersItem
class GetAgentResponseModelPhoneNumbersItem_SipTrunk(
    GetPhoneNumberSipTrunkResponseModel
):
    pass


# Union type for GetAgentResponseModelPhoneNumbersItem
# Pydantic will attempt to validate against each type in order
GetAgentResponseModelPhoneNumbersItem = Union[
    GetPhoneNumberTwilioResponseModel,
    GetPhoneNumberExotelResponseModel,
    GetPhoneNumberSipTrunkResponseModel,
]
# TypeAdapter for runtime validation of GetAgentResponseModelPhoneNumbersItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

GetAgentResponseModelPhoneNumbersItem_adapter = TypeAdapter(
    GetAgentResponseModelPhoneNumbersItem
)


class GetAgentResponseModel(BaseModel):
    """GetAgentResponseModel

    :param agent_id: The ID of the agent
    :type agent_id: str
    :param name: The name of the agent
    :type name: str
    :param conversation_config: conversation_config
    :type conversation_config: ConversationalConfig
    :param metadata: metadata
    :type metadata: AgentMetadataResponseModel
    :param platform_settings: platform_settings, defaults to None
    :type platform_settings: AgentPlatformSettingsResponseModel, optional
    :param phone_numbers: The phone numbers of the agent, defaults to None
    :type phone_numbers: List[GetAgentResponseModelPhoneNumbersItem], optional
    :param whatsapp_accounts: WhatsApp accounts assigned to the agent, defaults to None
    :type whatsapp_accounts: List[GetWhatsAppAccountResponse], optional
    :param workflow: workflow, defaults to None
    :type workflow: AgentWorkflowResponseModel, optional
    :param access_info: The access information of the agent for the user, defaults to None
    :type access_info: ResourceAccessInfo, optional
    :param tags: Agent tags used to categorize the agent, defaults to None
    :type tags: List[str], optional
    :param version_id: The ID of the version the agent is on, defaults to None
    :type version_id: str, optional
    :param branch_id: The ID of the branch the agent is on, defaults to None
    :type branch_id: str, optional
    :param main_branch_id: The ID of the main branch for this agent, defaults to None
    :type main_branch_id: str, optional
    """

    agent_id: str = Field(description="The ID of the agent")
    name: str = Field(description="The name of the agent")
    conversation_config: ConversationalConfig
    metadata: AgentMetadataResponseModel
    platform_settings: Optional[AgentPlatformSettingsResponseModel] = Field(
        default=None
    )
    phone_numbers: Optional[List[GetAgentResponseModelPhoneNumbersItem]] = Field(
        default=None, description="The phone numbers of the agent"
    )
    whatsapp_accounts: Optional[List[GetWhatsAppAccountResponse]] = Field(
        default=None, description="WhatsApp accounts assigned to the agent"
    )
    workflow: Optional[AgentWorkflowResponseModel] = Field(default=None)
    access_info: Optional[ResourceAccessInfo] = Field(
        default=None, description="The access information of the agent for the user"
    )
    tags: Optional[List[str]] = Field(
        default=None, description="Agent tags used to categorize the agent"
    )
    version_id: Optional[str] = Field(
        default=None, description="The ID of the version the agent is on"
    )
    branch_id: Optional[str] = Field(
        default=None, description="The ID of the branch the agent is on"
    )
    main_branch_id: Optional[str] = Field(
        default=None, description="The ID of the main branch for this agent"
    )
