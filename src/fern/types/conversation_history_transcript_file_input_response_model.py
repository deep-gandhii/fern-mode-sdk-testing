from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConversationHistoryTranscriptFileInputResponseModel(BaseModel):
    """ConversationHistoryTranscriptFileInputResponseModel

    :param file_id: file_id
    :type file_id: str
    :param original_filename: original_filename
    :type original_filename: str
    :param mime_type: mime_type
    :type mime_type: str
    :param file_url: file_url
    :type file_url: str
    """

    file_id: str
    original_filename: str
    mime_type: str
    file_url: str
