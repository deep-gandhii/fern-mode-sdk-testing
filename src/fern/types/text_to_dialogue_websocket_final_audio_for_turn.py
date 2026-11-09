from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TextToDialogueWebsocketFinalAudioForTurn(BaseModel):
    """TextToDialogueWebsocketFinalAudioForTurn

    :param is_final_audio_for_turn: Indicates that the final audio for a given turn has been sent., defaults to None
    :type is_final_audio_for_turn: bool, optional
    """

    is_final_audio_for_turn: Optional[bool] = Field(
        default=None,
        description="Indicates that the final audio for a given turn has been sent.",
    )
