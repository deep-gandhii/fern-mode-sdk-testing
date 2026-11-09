from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .whats_app_template_location_param_details import (
    WhatsAppTemplateLocationParamDetails,
)

WhatsAppTemplateLocationParamType = typing.Union[typing.Literal["location"], typing.Any]


class WhatsAppTemplateLocationParam(BaseModel):
    """WhatsAppTemplateLocationParam

    :param type: type, defaults to None
    :type type: WhatsAppTemplateLocationParamType, optional
    :param location: location
    :type location: WhatsAppTemplateLocationParamDetails
    """

    type: Optional[WhatsAppTemplateLocationParamType] = Field(default=None)
    location: WhatsAppTemplateLocationParamDetails
