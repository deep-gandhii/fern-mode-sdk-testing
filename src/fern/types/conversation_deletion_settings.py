from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ConversationDeletionSettings(BaseModel):
    """ConversationDeletionSettings

    :param deletion_time_unix_secs: deletion_time_unix_secs, defaults to None
    :type deletion_time_unix_secs: int, optional
    :param deleted_logs_at_time_unix_secs: deleted_logs_at_time_unix_secs, defaults to None
    :type deleted_logs_at_time_unix_secs: int, optional
    :param deleted_audio_at_time_unix_secs: deleted_audio_at_time_unix_secs, defaults to None
    :type deleted_audio_at_time_unix_secs: int, optional
    :param deleted_transcript_at_time_unix_secs: deleted_transcript_at_time_unix_secs, defaults to None
    :type deleted_transcript_at_time_unix_secs: int, optional
    :param delete_transcript_and_pii: delete_transcript_and_pii, defaults to None
    :type delete_transcript_and_pii: bool, optional
    :param delete_audio: delete_audio, defaults to None
    :type delete_audio: bool, optional
    """

    deletion_time_unix_secs: Optional[int] = Field(default=None)
    deleted_logs_at_time_unix_secs: Optional[int] = Field(default=None)
    deleted_audio_at_time_unix_secs: Optional[int] = Field(default=None)
    deleted_transcript_at_time_unix_secs: Optional[int] = Field(default=None)
    delete_transcript_and_pii: Optional[bool] = Field(default=None)
    delete_audio: Optional[bool] = Field(default=None)
