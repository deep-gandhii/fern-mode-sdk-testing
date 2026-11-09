from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .agent_response_payload import AgentResponsePayload
from .pong_payload import PongPayload

# Union type for SendUpstreamMessage
# Pydantic will attempt to validate against each type in order
SendUpstreamMessage = Union[AgentResponsePayload, PongPayload]
# TypeAdapter for runtime validation of SendUpstreamMessage
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SendUpstreamMessage_adapter = TypeAdapter(SendUpstreamMessage)
