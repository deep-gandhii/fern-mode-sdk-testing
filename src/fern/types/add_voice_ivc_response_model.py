from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AddVoiceIvcResponseModel(BaseModel):
    """AddVoiceIvcResponseModel

    :param voice_id: The ID of the newly created voice.
    :type voice_id: str
    :param requires_verification: Whether the voice requires verification
    :type requires_verification: bool
    """

    voice_id: str = Field(description="The ID of the newly created voice.")
    requires_verification: bool = Field(
        description="Whether the voice requires verification"
    )
