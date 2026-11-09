from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

ManualSourceType = typing.Union[typing.Literal["manual"], typing.Any]


class ManualSource(BaseModel):
    """ManualSource

    :param type: type, defaults to None
    :type type: ManualSourceType, optional
    :param created_by_user_id: created_by_user_id
    :type created_by_user_id: str
    :param notes: notes, defaults to None
    :type notes: str, optional
    """

    type: Optional[ManualSourceType] = Field(default=None)
    created_by_user_id: str
    notes: Optional[str] = Field(default=None)
