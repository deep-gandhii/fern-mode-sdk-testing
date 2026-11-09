from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class OpenAiToolChoiceFunctionInner(BaseModel):
    """OpenAiToolChoiceFunctionInner

    :param name: name
    :type name: str
    """

    name: str
