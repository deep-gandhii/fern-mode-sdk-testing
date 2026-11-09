from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .llm import Llm


class OpenerConfig(BaseModel):
    """OpenerConfig

    :param llm: llm
    :type llm: Llm
    """

    llm: Llm
