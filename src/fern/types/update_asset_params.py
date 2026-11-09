from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateAssetParamsSmbToolType = typing.Union[typing.Literal["update_asset"], typing.Any]


class UpdateAssetParams(BaseModel):
    """UpdateAssetParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateAssetParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateAssetParamsSmbToolType] = Field(default=None)
