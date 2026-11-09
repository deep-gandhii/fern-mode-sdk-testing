from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ListResponseMeta(BaseModel):
    """ListResponseMeta

    :param total: total, defaults to None
    :type total: int, optional
    :param page: page, defaults to None
    :type page: int, optional
    :param page_size: page_size, defaults to None
    :type page_size: int, optional
    """

    total: Optional[int] = Field(default=None)
    page: Optional[int] = Field(default=None)
    page_size: Optional[int] = Field(default=None)
