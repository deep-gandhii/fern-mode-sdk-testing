from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .init_payload import InitPayload
from .user_transcript_payload import UserTranscriptPayload
from .ping_payload import PingPayload
from .close_payload import ClosePayload
from .error_payload import ErrorPayload

# Union type for ReceiveUpstreamMessage
# Pydantic will attempt to validate against each type in order
ReceiveUpstreamMessage = Union[
    InitPayload, UserTranscriptPayload, PingPayload, ClosePayload, ErrorPayload
]
# TypeAdapter for runtime validation of ReceiveUpstreamMessage
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ReceiveUpstreamMessage_adapter = TypeAdapter(ReceiveUpstreamMessage)
