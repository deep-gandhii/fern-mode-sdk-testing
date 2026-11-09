from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .detected_entity import DetectedEntity

CommittedTranscriptEntitiesPayloadMessageType = typing.Union[
    typing.Literal["committed_transcript_entities"], typing.Any
]


class CommittedTranscriptEntitiesPayload(BaseModel):
    """Payload for detected entities on a committed transcript.

    :param message_type: The message type identifier.
    :type message_type: CommittedTranscriptEntitiesPayloadMessageType
    :param text: The committed transcript text the entities were detected in.
    :type text: str
    :param entities: Detected entities. Empty if none were found.
    :type entities: List[DetectedEntity]
    """

    message_type: CommittedTranscriptEntitiesPayloadMessageType = Field(
        default="committed_transcript_entities",
        description="The message type identifier.",
    )
    text: str = Field(
        description="The committed transcript text the entities were detected in."
    )
    entities: List[DetectedEntity] = Field(
        description="Detected entities. Empty if none were found."
    )
