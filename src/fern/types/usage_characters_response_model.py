from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel


class UsageCharactersResponseModel(BaseModel):
    """UsageCharactersResponseModel

    :param time: The time axis with unix timestamps for each day.
    :type time: List[int]
    :param usage: The usage of each breakdown type along the time axis.
    :type usage: Dict[str, List[float]]
    """

    time: List[int] = Field(
        description="The time axis with unix timestamps for each day."
    )
    usage: Dict[str, List[float]] = Field(
        description="The usage of each breakdown type along the time axis."
    )
