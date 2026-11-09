from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListClientInteractionsParamsSmbToolType = typing.Union[
    typing.Literal["list_client_interactions"], typing.Any
]


class ListClientInteractionsParams(BaseModel):
    """ListClientInteractionsParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListClientInteractionsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListClientInteractionsParamsSmbToolType] = Field(
        default=None
    )
