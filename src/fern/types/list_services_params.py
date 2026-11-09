from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

ListServicesParamsSmbToolType = typing.Union[
    typing.Literal["list_services"], typing.Any
]


class ListServicesParams(BaseModel):
    """ListServicesParams

    :param list_kwargs: list_kwargs, defaults to None
    :type list_kwargs: Dict[str, Any], optional
    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListServicesParamsSmbToolType, optional
    """

    list_kwargs: Optional[Dict[str, Any]] = Field(default=None)
    smb_tool_type: Optional[ListServicesParamsSmbToolType] = Field(default=None)
