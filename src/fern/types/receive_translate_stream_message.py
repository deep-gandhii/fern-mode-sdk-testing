from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .translate_session_started_payload import TranslateSessionStartedPayload
from .translate_status_payload import TranslateStatusPayload
from .translate_partial_transcript_payload import TranslatePartialTranscriptPayload
from .translate_final_transcript_payload import TranslateFinalTranscriptPayload
from .translate_translation_payload import TranslateTranslationPayload
from .translate_audio_payload import TranslateAudioPayload
from .translate_error_payload import TranslateErrorPayload
from .translate_auth_error import TranslateAuthError
from .translate_rate_limited_error import TranslateRateLimitedError
from .translate_queue_overflow_error import TranslateQueueOverflowError
from .translate_input_error import TranslateInputError
from .translate_transcriber_error import TranslateTranscriberError
from .translate_translation_error import TranslateTranslationError
from .translate_audio_output_error import TranslateAudioOutputError

# Union type for ReceiveTranslateStreamMessage
# Pydantic will attempt to validate against each type in order
ReceiveTranslateStreamMessage = Union[
    TranslateSessionStartedPayload,
    TranslateStatusPayload,
    TranslatePartialTranscriptPayload,
    TranslateFinalTranscriptPayload,
    TranslateTranslationPayload,
    TranslateAudioPayload,
    TranslateErrorPayload,
    TranslateAuthError,
    TranslateRateLimitedError,
    TranslateQueueOverflowError,
    TranslateInputError,
    TranslateTranscriberError,
    TranslateTranslationError,
    TranslateAudioOutputError,
]
# TypeAdapter for runtime validation of ReceiveTranslateStreamMessage
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ReceiveTranslateStreamMessage_adapter = TypeAdapter(ReceiveTranslateStreamMessage)
