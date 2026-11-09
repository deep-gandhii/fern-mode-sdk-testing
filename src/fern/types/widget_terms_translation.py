from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class WidgetTermsTranslation(BaseModel):
    """WidgetTermsTranslation

    :param source_hash: source_hash
    :type source_hash: str
    :param text: text
    :type text: str
    """

    source_hash: str
    text: str
