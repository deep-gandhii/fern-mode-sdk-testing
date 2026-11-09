from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class KnowledgeBaseSourceFileUrlResponseModel(BaseModel):
    """KnowledgeBaseSourceFileUrlResponseModel

    :param signed_url: Signed URL to download the source file directly
    :type signed_url: str
    """

    signed_url: str = Field(
        description="Signed URL to download the source file directly"
    )
