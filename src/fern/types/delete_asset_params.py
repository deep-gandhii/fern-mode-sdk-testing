from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteAssetParamsSmbToolType = typing.Union[typing.Literal["delete_asset"], typing.Any]


class DeleteAssetParams(BaseModel):
    """DeleteAssetParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteAssetParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteAssetParamsSmbToolType] = Field(default=None)
