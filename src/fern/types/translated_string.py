from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TranslatedString(BaseModel):
    """TranslatedString

    :param value: value
    :type value: str
    """

    value: str
