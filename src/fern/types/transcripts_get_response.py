from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .speech_to_text_chunk_response_model import SpeechToTextChunkResponseModel
from .multichannel_speech_to_text_response_model import (
    MultichannelSpeechToTextResponseModel,
)

# Union type for TranscriptsGetResponse
# Pydantic will attempt to validate against each type in order
TranscriptsGetResponse = Union[
    SpeechToTextChunkResponseModel, MultichannelSpeechToTextResponseModel
]
# TypeAdapter for runtime validation of TranscriptsGetResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

TranscriptsGetResponse_adapter = TypeAdapter(TranscriptsGetResponse)
