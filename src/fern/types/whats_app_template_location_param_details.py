from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class WhatsAppTemplateLocationParamDetails(BaseModel):
    """WhatsAppTemplateLocationParamDetails

    :param latitude: latitude
    :type latitude: str
    :param longitude: longitude
    :type longitude: str
    :param name: name
    :type name: str
    :param address: address
    :type address: str
    """

    latitude: str
    longitude: str
    name: str
    address: str
