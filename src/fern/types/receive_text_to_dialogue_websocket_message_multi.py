from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .text_to_dialogue_websocket_audio_chunk_multi import (
    TextToDialogueWebsocketAudioChunkMulti,
)
from .text_to_dialogue_websocket_final_audio_for_turn_multi import (
    TextToDialogueWebsocketFinalAudioForTurnMulti,
)
from .text_to_dialogue_websocket_final_multi import TextToDialogueWebsocketFinalMulti
from .text_to_dialogue_websocket_error import TextToDialogueWebsocketError

# Union type for ReceiveTextToDialogueWebsocketMessageMulti
# Pydantic will attempt to validate against each type in order
ReceiveTextToDialogueWebsocketMessageMulti = Union[
    TextToDialogueWebsocketAudioChunkMulti,
    TextToDialogueWebsocketFinalAudioForTurnMulti,
    TextToDialogueWebsocketFinalMulti,
    TextToDialogueWebsocketError,
]
# TypeAdapter for runtime validation of ReceiveTextToDialogueWebsocketMessageMulti
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ReceiveTextToDialogueWebsocketMessageMulti_adapter = TypeAdapter(
    ReceiveTextToDialogueWebsocketMessageMulti
)
