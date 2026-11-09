from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .voice_accent_response_model import VoiceAccentResponseModel


class GetVoiceAccentsResponseModel(BaseModel):
    """GetVoiceAccentsResponseModel

    :param accents: A list of available voice accents.
    :type accents: List[VoiceAccentResponseModel]
    """

    accents: List[VoiceAccentResponseModel] = Field(
        description="A list of available voice accents."
    )
