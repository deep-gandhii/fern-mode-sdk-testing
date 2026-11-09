from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .session_started_payload import SessionStartedPayload
from .partial_transcript_payload import PartialTranscriptPayload
from .final_transcript import FinalTranscript
from .final_transcript_with_timestamps import FinalTranscriptWithTimestamps
from .committed_transcript_payload import CommittedTranscriptPayload
from .committed_transcript_with_timestamps_payload import (
    CommittedTranscriptWithTimestampsPayload,
)
from .committed_transcript_entities_payload import CommittedTranscriptEntitiesPayload
from .scribe_error_payload import ScribeErrorPayload
from .scribe_auth_error_payload import ScribeAuthErrorPayload
from .scribe_quota_exceeded_error_payload import ScribeQuotaExceededErrorPayload
from .scribe_throttled_error_payload import ScribeThrottledErrorPayload
from .scribe_unaccepted_terms_error_payload import ScribeUnacceptedTermsErrorPayload
from .scribe_rate_limited_error_payload import ScribeRateLimitedErrorPayload
from .scribe_queue_overflow_error_payload import ScribeQueueOverflowErrorPayload
from .scribe_resource_exhausted_error_payload import ScribeResourceExhaustedErrorPayload
from .scribe_session_time_limit_exceeded_error_payload import (
    ScribeSessionTimeLimitExceededErrorPayload,
)
from .scribe_input_error_payload import ScribeInputErrorPayload
from .scribe_chunk_size_exceeded_error_payload import (
    ScribeChunkSizeExceededErrorPayload,
)
from .scribe_insufficient_audio_activity_error_payload import (
    ScribeInsufficientAudioActivityErrorPayload,
)
from .scribe_transcriber_error_payload import ScribeTranscriberErrorPayload

# Union type for ReceiveTranscription
# Pydantic will attempt to validate against each type in order
ReceiveTranscription = Union[
    SessionStartedPayload,
    PartialTranscriptPayload,
    FinalTranscript,
    FinalTranscriptWithTimestamps,
    CommittedTranscriptPayload,
    CommittedTranscriptWithTimestampsPayload,
    CommittedTranscriptEntitiesPayload,
    ScribeErrorPayload,
    ScribeAuthErrorPayload,
    ScribeQuotaExceededErrorPayload,
    ScribeThrottledErrorPayload,
    ScribeUnacceptedTermsErrorPayload,
    ScribeRateLimitedErrorPayload,
    ScribeQueueOverflowErrorPayload,
    ScribeResourceExhaustedErrorPayload,
    ScribeSessionTimeLimitExceededErrorPayload,
    ScribeInputErrorPayload,
    ScribeChunkSizeExceededErrorPayload,
    ScribeInsufficientAudioActivityErrorPayload,
    ScribeTranscriberErrorPayload,
]
# TypeAdapter for runtime validation of ReceiveTranscription
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ReceiveTranscription_adapter = TypeAdapter(ReceiveTranscription)
