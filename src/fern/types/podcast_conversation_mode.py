from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .podcast_conversation_mode_data import PodcastConversationModeData

PodcastConversationModeType = typing.Union[typing.Literal["conversation"], typing.Any]


class PodcastConversationMode(BaseModel):
    """PodcastConversationMode

    :param type: The type of podcast to create.
    :type type: PodcastConversationModeType
    :param conversation: conversation
    :type conversation: PodcastConversationModeData
    """

    type: PodcastConversationModeType = Field(
        default="conversation", description="The type of podcast to create."
    )
    conversation: PodcastConversationModeData
