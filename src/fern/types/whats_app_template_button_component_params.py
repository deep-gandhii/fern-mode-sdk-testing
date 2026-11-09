from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .whats_app_template_text_param import WhatsAppTemplateTextParam

WhatsAppTemplateButtonComponentParamsType = typing.Union[
    typing.Literal["button"], typing.Any
]


class WhatsAppTemplateButtonComponentParams(BaseModel):
    """WhatsAppTemplateButtonComponentParams

    :param type: type, defaults to None
    :type type: WhatsAppTemplateButtonComponentParamsType, optional
    :param parameters: parameters
    :type parameters: List[WhatsAppTemplateTextParam]
    :param index: index
    :type index: int
    :param sub_type: sub_type
    :type sub_type: str
    """

    type: Optional[WhatsAppTemplateButtonComponentParamsType] = Field(default=None)
    parameters: List[WhatsAppTemplateTextParam]
    index: int
    sub_type: str
