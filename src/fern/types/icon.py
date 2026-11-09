from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class Icon(BaseModel):
    """An icon for display in user interfaces.

    :param src: src
    :type src: str
    :param mime_type: mime_type, defaults to None
    :type mime_type: str, optional
    :param sizes: sizes, defaults to None
    :type sizes: List[str], optional
    """

    src: str
    mime_type: Optional[str] = Field(
        alias="mimeType", serialization_alias="mimeType", default=None
    )
    sizes: Optional[List[str]] = Field(default=None)

    def model_dump_original(self, **kwargs):
        result = super().model_dump_original(**kwargs)
        extra_fields = self.model_extra or {}
        return {**extra_fields, **result}
