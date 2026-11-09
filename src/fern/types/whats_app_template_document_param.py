from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .whats_app_template_document_param_details import (
    WhatsAppTemplateDocumentParamDetails,
)

WhatsAppTemplateDocumentParamType = typing.Union[typing.Literal["document"], typing.Any]


class WhatsAppTemplateDocumentParam(BaseModel):
    """WhatsAppTemplateDocumentParam

    :param type: type, defaults to None
    :type type: WhatsAppTemplateDocumentParamType, optional
    :param document: document
    :type document: WhatsAppTemplateDocumentParamDetails
    """

    type: Optional[WhatsAppTemplateDocumentParamType] = Field(default=None)
    document: WhatsAppTemplateDocumentParamDetails
