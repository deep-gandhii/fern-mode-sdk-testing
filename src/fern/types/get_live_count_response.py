from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class GetLiveCountResponse(BaseModel):
    """GetLiveCountResponse

    :param count: The number of active ongoing conversations.
    :type count: int
    """

    count: int = Field(description="The number of active ongoing conversations.")
