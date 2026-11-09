from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

OpenAiFunctionToolType = typing.Union[typing.Literal["function"], typing.Any]


class OpenAiFunctionTool(BaseModel):
    """OpenAiFunctionTool

    :param type: type, defaults to None
    :type type: OpenAiFunctionToolType, optional
    :param name: name
    :type name: str
    :param description: description, defaults to None
    :type description: str, optional
    :param parameters: parameters, defaults to None
    :type parameters: Dict[str, Any], optional
    """

    type: Optional[OpenAiFunctionToolType] = Field(default=None)
    name: str
    description: Optional[str] = Field(default=None)
    parameters: Optional[Dict[str, Any]] = Field(default=None)
