from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

ListProductsParamsSmbToolType = typing.Union[
    typing.Literal["list_products"], typing.Any
]


class ListProductsParams(BaseModel):
    """ListProductsParams

    :param list_kwargs: list_kwargs, defaults to None
    :type list_kwargs: Dict[str, Any], optional
    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListProductsParamsSmbToolType, optional
    """

    list_kwargs: Optional[Dict[str, Any]] = Field(default=None)
    smb_tool_type: Optional[ListProductsParamsSmbToolType] = Field(default=None)
