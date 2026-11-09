from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TextToDialogueWebsocketVoiceInput(BaseModel):
    """TextToDialogueWebsocketVoiceInput

    :param text: Text appended for this voice. Buffered with prior text until the server triggers generation.
    :type text: str
    :param voice_id: Must be one of the IDs from the initial `voices` array.
    :type voice_id: str
    :param new_turn: When `true`, the server finalizes the current pending segment (as if the speaker finished their turn) before applying this input., defaults to None
    :type new_turn: bool, optional
    """

    text: str = Field(
        description="Text appended for this voice. Buffered with prior text until the server triggers generation."
    )
    voice_id: str = Field(
        description="Must be one of the IDs from the initial `voices` array."
    )
    new_turn: Optional[bool] = Field(
        default=None,
        description="When `true`, the server finalizes the current pending segment (as if the speaker finished their turn) before applying this input.",
    )
