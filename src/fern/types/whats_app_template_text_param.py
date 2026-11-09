from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

WhatsAppTemplateTextParamType = typing.Union[typing.Literal["text"], typing.Any]


class WhatsAppTemplateTextParam(BaseModel):
    """WhatsAppTemplateTextParam

    :param parameter_name: parameter_name, defaults to None
    :type parameter_name: str, optional
    :param type: type, defaults to None
    :type type: WhatsAppTemplateTextParamType, optional
    :param text: text
    :type text: str
    """

    parameter_name: Optional[str] = Field(default=None)
    type: Optional[WhatsAppTemplateTextParamType] = Field(default=None)
    text: str
