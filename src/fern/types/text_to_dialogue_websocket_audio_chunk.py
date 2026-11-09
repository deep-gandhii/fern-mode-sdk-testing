from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .dialogue_text_alignment import DialogueTextAlignment


class TextToDialogueWebsocketAudioChunk(BaseModel):
    """Server chunk containing encoded audio and optional alignment metadata.

    :param audio: Base64-encoded audio bytes for the selected `output_format`., defaults to None
    :type audio: str, optional
    :param alignment: Character-level alignment data (field names use snake_case in JSON)., defaults to None
    :type alignment: DialogueTextAlignment, optional
    :param normalized_alignment: Character-level alignment data (field names use snake_case in JSON)., defaults to None
    :type normalized_alignment: DialogueTextAlignment, optional
    """

    audio: Optional[str] = Field(
        default=None,
        description="Base64-encoded audio bytes for the selected `output_format`.",
    )
    alignment: Optional[DialogueTextAlignment] = Field(
        default=None,
        description="Character-level alignment data (field names use snake_case in JSON).",
    )
    normalized_alignment: Optional[DialogueTextAlignment] = Field(
        default=None,
        description="Character-level alignment data (field names use snake_case in JSON).",
    )
