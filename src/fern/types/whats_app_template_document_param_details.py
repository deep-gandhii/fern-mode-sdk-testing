from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class WhatsAppTemplateDocumentParamDetails(BaseModel):
    """WhatsAppTemplateDocumentParamDetails

    :param link: link
    :type link: str
    :param filename: filename, defaults to None
    :type filename: str, optional
    """

    link: str
    filename: Optional[str] = Field(default=None)
