from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .sentiment_aggregate import SentimentAggregate
from .frustrated_conversation_ref import FrustratedConversationRef


class ConversationUserResponseModel(BaseModel):
    """ConversationUserResponseModel

    :param user_id: user_id
    :type user_id: str
    :param last_contact_unix_secs: last_contact_unix_secs
    :type last_contact_unix_secs: int
    :param first_contact_unix_secs: first_contact_unix_secs
    :type first_contact_unix_secs: int
    :param conversation_count: conversation_count
    :type conversation_count: int
    :param last_contact_agent_id: last_contact_agent_id, defaults to None
    :type last_contact_agent_id: str, optional
    :param last_contact_conversation_id: last_contact_conversation_id
    :type last_contact_conversation_id: str
    :param last_contact_agent_name: last_contact_agent_name, defaults to None
    :type last_contact_agent_name: str, optional
    :param sentiment: sentiment
    :type sentiment: SentimentAggregate
    :param most_frustrated_conversations: most_frustrated_conversations, defaults to None
    :type most_frustrated_conversations: List[FrustratedConversationRef], optional
    """

    user_id: str
    last_contact_unix_secs: int
    first_contact_unix_secs: int
    conversation_count: int
    last_contact_agent_id: Optional[str] = Field(default=None)
    last_contact_conversation_id: str
    last_contact_agent_name: Optional[str] = Field(default=None)
    sentiment: SentimentAggregate
    most_frustrated_conversations: Optional[List[FrustratedConversationRef]] = Field(
        default=None
    )
