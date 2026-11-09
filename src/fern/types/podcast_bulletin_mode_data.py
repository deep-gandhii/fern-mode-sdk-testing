from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PodcastBulletinModeData(BaseModel):
    """PodcastBulletinModeData

    :param host_voice_id: The ID of the host voice.
    :type host_voice_id: str
    """

    host_voice_id: str = Field(description="The ID of the host voice.")
