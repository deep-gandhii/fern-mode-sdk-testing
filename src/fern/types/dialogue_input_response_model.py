from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DialogueInputResponseModel(BaseModel):
    """DialogueInputResponseModel

    :param text: The text of the dialogue input line.
    :type text: str
    :param voice_id: The ID of the voice used for this dialogue input line.
    :type voice_id: str
    :param voice_name: The name of the voice used for this dialogue input line.
    :type voice_name: str
    """

    text: str = Field(description="The text of the dialogue input line.")
    voice_id: str = Field(
        description="The ID of the voice used for this dialogue input line."
    )
    voice_name: str = Field(
        description="The name of the voice used for this dialogue input line."
    )
