from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AddVoiceResponseModel(BaseModel):
    """AddVoiceResponseModel

    :param voice_id: The ID of the voice.
    :type voice_id: str
    """

    voice_id: str = Field(description="The ID of the voice.")
