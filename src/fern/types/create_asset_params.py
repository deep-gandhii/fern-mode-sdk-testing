from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateAssetParamsSmbToolType = typing.Union[typing.Literal["create_asset"], typing.Any]


class CreateAssetParams(BaseModel):
    """CreateAssetParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CreateAssetParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CreateAssetParamsSmbToolType] = Field(default=None)
