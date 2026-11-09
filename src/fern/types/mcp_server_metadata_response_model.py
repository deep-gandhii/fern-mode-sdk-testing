from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class McpServerMetadataResponseModel(BaseModel):
    """McpServerMetadataResponseModel

    :param created_at: created_at
    :type created_at: int
    :param owner_user_id: owner_user_id, defaults to None
    :type owner_user_id: str, optional
    """

    created_at: int
    owner_user_id: Optional[str] = Field(default=None)
