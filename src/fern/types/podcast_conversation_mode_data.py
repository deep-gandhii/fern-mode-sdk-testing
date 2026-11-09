from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PodcastConversationModeData(BaseModel):
    """PodcastConversationModeData

    :param host_voice_id: The ID of the host voice.
    :type host_voice_id: str
    :param guest_voice_id: The ID of the guest voice.
    :type guest_voice_id: str
    """

    host_voice_id: str = Field(description="The ID of the host voice.")
    guest_voice_id: str = Field(description="The ID of the guest voice.")
