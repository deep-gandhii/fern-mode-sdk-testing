from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .dubbing_transcript_response_model import DubbingTranscriptResponseModel

# Union type for TranscriptGetTranscriptForDubResponse
# Pydantic will attempt to validate against each type in order
TranscriptGetTranscriptForDubResponse = Union[DubbingTranscriptResponseModel, str]
# TypeAdapter for runtime validation of TranscriptGetTranscriptForDubResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

TranscriptGetTranscriptForDubResponse_adapter = TypeAdapter(
    TranscriptGetTranscriptForDubResponse
)
