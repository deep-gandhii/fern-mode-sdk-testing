from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConvAiFileUploadResponseModel(BaseModel):
    """ConvAiFileUploadResponseModel

    :param file_id: file_id
    :type file_id: str
    """

    file_id: str
