from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .voice import Voice


class GetVoicesResponse(BaseModel):
    """GetVoicesResponse

    :param voices: A list of available voices.
    :type voices: List[Voice]
    """

    voices: List[Voice] = Field(description="A list of available voices.")
