from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ManualVerificationFileResponse(BaseModel):
    """ManualVerificationFileResponse

    :param file_id: The ID of the file.
    :type file_id: str
    :param file_name: The name of the file.
    :type file_name: str
    :param mime_type: The MIME type of the file.
    :type mime_type: str
    :param size_bytes: The size of the file in bytes.
    :type size_bytes: int
    :param upload_date_unix: The date of the file in Unix time.
    :type upload_date_unix: int
    """

    file_id: str = Field(description="The ID of the file.")
    file_name: str = Field(description="The name of the file.")
    mime_type: str = Field(description="The MIME type of the file.")
    size_bytes: int = Field(description="The size of the file in bytes.")
    upload_date_unix: int = Field(description="The date of the file in Unix time.")
