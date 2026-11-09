from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RagDocumentIndexUsage(BaseModel):
    """RagDocumentIndexUsage

    :param used_bytes: used_bytes
    :type used_bytes: int
    """

    used_bytes: int
