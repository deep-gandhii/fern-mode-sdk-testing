from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AgentResponsePayloadType = typing.Union[typing.Literal["agent_response"], typing.Any]


class AgentResponsePayload(BaseModel):
    """Text chunk sent from your server to ElevenLabs for speech synthesis. Stream LLM output by sending multiple messages with `is_final: false`, then terminate the response with a message where `is_final: true` and `content` is an empty string.

    :param type: The message type identifier.
    :type type: AgentResponsePayloadType
    :param content: The text to synthesize. For streaming responses, send incremental chunks here. The final message in a response must have an empty string (`""`).
    :type content: str
    :param event_id: The `event_id` from the `user_transcript` this response addresses. ElevenLabs uses this to discard responses that belong to an interrupted turn., defaults to None
    :type event_id: int, optional
    :param is_final: Set to `true` on the last message of a response (with an empty `content`). Set to `false` on all preceding chunks.
    :type is_final: bool
    """

    type: AgentResponsePayloadType = Field(
        default="agent_response", description="The message type identifier."
    )
    content: str = Field(
        description='The text to synthesize. For streaming responses, send incremental chunks here. The final message in a response must have an empty string (`""`).'
    )
    event_id: Optional[int] = Field(
        default=None,
        description="The `event_id` from the `user_transcript` this response addresses. ElevenLabs uses this to discard responses that belong to an interrupted turn.",
    )
    is_final: bool = Field(
        description="Set to `true` on the last message of a response (with an empty `content`). Set to `false` on all preceding chunks."
    )
