from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DialogueInput(BaseModel):
    """DialogueInput

    :param text: The text to be converted into speech.
    :type text: str
    :param voice_id: The ID of the voice to be used for the generation.
    :type voice_id: str
    """

    text: str = Field(description="The text to be converted into speech.")
    voice_id: str = Field(
        description="The ID of the voice to be used for the generation."
    )
