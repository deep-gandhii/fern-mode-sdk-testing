from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .whats_app_template_image_param_details import WhatsAppTemplateImageParamDetails

WhatsAppTemplateImageParamType = typing.Union[typing.Literal["image"], typing.Any]


class WhatsAppTemplateImageParam(BaseModel):
    """WhatsAppTemplateImageParam

    :param type: type, defaults to None
    :type type: WhatsAppTemplateImageParamType, optional
    :param image: image
    :type image: WhatsAppTemplateImageParamDetails
    """

    type: Optional[WhatsAppTemplateImageParamType] = Field(default=None)
    image: WhatsAppTemplateImageParamDetails
