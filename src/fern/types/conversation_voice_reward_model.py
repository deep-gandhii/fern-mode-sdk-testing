from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConversationVoiceRewardModel(BaseModel):
    """ConversationVoiceRewardModel

    :param voice_id: voice_id
    :type voice_id: str
    :param reward_usd_cents: reward_usd_cents
    :type reward_usd_cents: float
    """

    voice_id: str
    reward_usd_cents: float
