from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .text_to_dialogue_websocket_audio_chunk import TextToDialogueWebsocketAudioChunk
from .text_to_dialogue_websocket_final_audio_for_turn import (
    TextToDialogueWebsocketFinalAudioForTurn,
)
from .text_to_dialogue_websocket_final import TextToDialogueWebsocketFinal
from .text_to_dialogue_websocket_error import TextToDialogueWebsocketError

# Union type for ReceiveTextToDialogueWebsocketMessage
# Pydantic will attempt to validate against each type in order
ReceiveTextToDialogueWebsocketMessage = Union[
    TextToDialogueWebsocketAudioChunk,
    TextToDialogueWebsocketFinalAudioForTurn,
    TextToDialogueWebsocketFinal,
    TextToDialogueWebsocketError,
]
# TypeAdapter for runtime validation of ReceiveTextToDialogueWebsocketMessage
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ReceiveTextToDialogueWebsocketMessage_adapter = TypeAdapter(
    ReceiveTextToDialogueWebsocketMessage
)
