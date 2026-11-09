from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .recording_response import RecordingResponse


class VerificationAttemptResponse(BaseModel):
    """VerificationAttemptResponse

    :param text: The text of the verification attempt.
    :type text: str
    :param date_unix: The date of the verification attempt in Unix time.
    :type date_unix: int
    :param accepted: Whether the verification attempt was accepted.
    :type accepted: bool
    :param similarity: The similarity of the verification attempt.
    :type similarity: float
    :param levenshtein_distance: The Levenshtein distance of the verification attempt.
    :type levenshtein_distance: float
    :param recording: The recording of the verification attempt., defaults to None
    :type recording: RecordingResponse, optional
    """

    text: str = Field(description="The text of the verification attempt.")
    date_unix: int = Field(
        description="The date of the verification attempt in Unix time."
    )
    accepted: bool = Field(description="Whether the verification attempt was accepted.")
    similarity: float = Field(description="The similarity of the verification attempt.")
    levenshtein_distance: float = Field(
        description="The Levenshtein distance of the verification attempt."
    )
    recording: Optional[RecordingResponse] = Field(
        default=None, description="The recording of the verification attempt."
    )
