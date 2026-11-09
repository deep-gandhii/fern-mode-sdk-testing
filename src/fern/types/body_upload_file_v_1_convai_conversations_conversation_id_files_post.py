from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyUploadFileV1ConvaiConversationsConversationIdFilesPost(BaseModel):
    """BodyUploadFileV1ConvaiConversationsConversationIdFilesPost

    :param file: Image or PDF file to upload
    :type file: bytes
    """

    file: bytes = Field(description="Image or PDF file to upload")
