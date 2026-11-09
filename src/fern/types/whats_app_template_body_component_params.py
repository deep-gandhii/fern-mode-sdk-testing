from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .whats_app_template_text_param import WhatsAppTemplateTextParam

WhatsAppTemplateBodyComponentParamsType = typing.Union[
    typing.Literal["body"], typing.Any
]


class WhatsAppTemplateBodyComponentParams(BaseModel):
    """WhatsAppTemplateBodyComponentParams

    :param type: type, defaults to None
    :type type: WhatsAppTemplateBodyComponentParamsType, optional
    :param parameters: parameters
    :type parameters: List[WhatsAppTemplateTextParam]
    """

    type: Optional[WhatsAppTemplateBodyComponentParamsType] = Field(default=None)
    parameters: List[WhatsAppTemplateTextParam]
