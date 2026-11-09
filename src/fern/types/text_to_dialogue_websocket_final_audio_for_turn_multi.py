from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TextToDialogueWebsocketFinalAudioForTurnMulti(BaseModel):
    """TextToDialogueWebsocketFinalAudioForTurnMulti

    :param is_final_audio_for_turn: Indicates that the final audio for a given turn of this context has been sent., defaults to None
    :type is_final_audio_for_turn: bool, optional
    :param context_id: The context whose turn has finished., defaults to None
    :type context_id: str, optional
    """

    is_final_audio_for_turn: Optional[bool] = Field(
        default=None,
        description="Indicates that the final audio for a given turn of this context has been sent.",
    )
    context_id: Optional[str] = Field(
        default=None, description="The context whose turn has finished."
    )
