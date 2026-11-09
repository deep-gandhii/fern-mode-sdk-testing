from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .translate_input_audio_chunk_payload import TranslateInputAudioChunkPayload
from .translate_end_of_stream_payload import TranslateEndOfStreamPayload

# Union type for SendTranslateStreamMessage
# Pydantic will attempt to validate against each type in order
SendTranslateStreamMessage = Union[
    TranslateInputAudioChunkPayload, TranslateEndOfStreamPayload
]
# TypeAdapter for runtime validation of SendTranslateStreamMessage
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SendTranslateStreamMessage_adapter = TypeAdapter(SendTranslateStreamMessage)
