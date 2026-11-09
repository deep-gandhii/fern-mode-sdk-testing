from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .dialogue_text_alignment import DialogueTextAlignment


class TextToDialogueWebsocketAudioChunkMulti(BaseModel):
    """Server chunk containing encoded audio for a specific context and optional alignment metadata.

    :param audio: Base64-encoded audio bytes for the selected `output_format`., defaults to None
    :type audio: str, optional
    :param alignment: Character-level alignment data (field names use snake_case in JSON)., defaults to None
    :type alignment: DialogueTextAlignment, optional
    :param normalized_alignment: Character-level alignment data (field names use snake_case in JSON)., defaults to None
    :type normalized_alignment: DialogueTextAlignment, optional
    :param context_id: The context this audio chunk belongs to., defaults to None
    :type context_id: str, optional
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
    context_id: Optional[str] = Field(
        default=None, description="The context this audio chunk belongs to."
    )
