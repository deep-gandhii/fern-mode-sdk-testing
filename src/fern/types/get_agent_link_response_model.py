from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_token_response_model import ConversationTokenResponseModel


class GetAgentLinkResponseModel(BaseModel):
    """GetAgentLinkResponseModel

    :param agent_id: The ID of the agent
    :type agent_id: str
    :param token: The token data for the agent, defaults to None
    :type token: ConversationTokenResponseModel, optional
    """

    agent_id: str = Field(description="The ID of the agent")
    token: Optional[ConversationTokenResponseModel] = Field(
        default=None, description="The token data for the agent"
    )
