from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RecordingResponse(BaseModel):
    """RecordingResponse

    :param recording_id: The ID of the recording.
    :type recording_id: str
    :param mime_type: The MIME type of the recording.
    :type mime_type: str
    :param size_bytes: The size of the recording in bytes.
    :type size_bytes: int
    :param upload_date_unix: The date of the recording in Unix time.
    :type upload_date_unix: int
    :param transcription: The transcription of the recording.
    :type transcription: str
    """

    recording_id: str = Field(description="The ID of the recording.")
    mime_type: str = Field(description="The MIME type of the recording.")
    size_bytes: int = Field(description="The size of the recording in bytes.")
    upload_date_unix: int = Field(description="The date of the recording in Unix time.")
    transcription: str = Field(description="The transcription of the recording.")
