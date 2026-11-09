from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_token_purpose import ConversationTokenPurpose


class ConversationTokenResponseModel(BaseModel):
    """ConversationTokenResponseModel

    :param agent_id: The ID of the agent
    :type agent_id: str
    :param conversation_token: The token for the agent
    :type conversation_token: str
    :param expiration_time_unix_secs: The expiration time of the token in unix seconds, defaults to None
    :type expiration_time_unix_secs: int, optional
    :param conversation_id: The ID of the conversation, defaults to None
    :type conversation_id: str, optional
    :param purpose: purpose
    :type purpose: ConversationTokenPurpose
    :param token_requester_user_id: The user ID of the entity who requested the token, defaults to None
    :type token_requester_user_id: str, optional
    """

    agent_id: str = Field(description="The ID of the agent")
    conversation_token: str = Field(description="The token for the agent")
    expiration_time_unix_secs: Optional[int] = Field(
        default=None, description="The expiration time of the token in unix seconds"
    )
    conversation_id: Optional[str] = Field(
        default=None, description="The ID of the conversation"
    )
    purpose: ConversationTokenPurpose
    token_requester_user_id: Optional[str] = Field(
        default=None, description="The user ID of the entity who requested the token"
    )
