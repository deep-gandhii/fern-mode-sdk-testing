from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .transcript_message import TranscriptMessage

UserTranscriptPayloadType = typing.Union[typing.Literal["user_transcript"], typing.Any]


class UserTranscriptPayload(BaseModel):
    """Payload containing the full conversation history sent by ElevenLabs each time the user finishes speaking.

    :param type: The message type identifier.
    :type type: UserTranscriptPayloadType
    :param user_transcript: Full conversation history up to and including the latest user turn, ordered chronologically. Contains both `user` and `agent` turns.
    :type user_transcript: List[TranscriptMessage]
    :param event_id: Monotonically increasing identifier for this transcript event. Pass this value back in every `agent_response` message so ElevenLabs can correlate responses and discard any that belong to an interrupted turn., defaults to None
    :type event_id: int, optional
    """

    type: UserTranscriptPayloadType = Field(
        default="user_transcript", description="The message type identifier."
    )
    user_transcript: List[TranscriptMessage] = Field(
        description="Full conversation history up to and including the latest user turn, ordered chronologically. Contains both `user` and `agent` turns."
    )
    event_id: Optional[int] = Field(
        default=None,
        description="Monotonically increasing identifier for this transcript event. Pass this value back in every `agent_response` message so ElevenLabs can correlate responses and discard any that belong to an interrupted turn.",
    )
