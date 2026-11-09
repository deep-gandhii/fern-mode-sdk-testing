from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .speech_to_text_chunk_response_model import SpeechToTextChunkResponseModel
from .multichannel_speech_to_text_response_model import (
    MultichannelSpeechToTextResponseModel,
)
from .speech_to_text_webhook_response_model import SpeechToTextWebhookResponseModel

# Union type for SpeechToTextConvertResponse
# Pydantic will attempt to validate against each type in order
SpeechToTextConvertResponse = Union[
    SpeechToTextChunkResponseModel,
    MultichannelSpeechToTextResponseModel,
    SpeechToTextWebhookResponseModel,
]
# TypeAdapter for runtime validation of SpeechToTextConvertResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SpeechToTextConvertResponse_adapter = TypeAdapter(SpeechToTextConvertResponse)
