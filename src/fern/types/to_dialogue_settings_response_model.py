from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ToDialogueSettingsResponseModel(BaseModel):
    """ToDialogueSettingsResponseModel

    :param stability: Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion., defaults to None
    :type stability: float, optional
    :param speed: speed, defaults to None
    :type speed: float, optional
    """

    stability: Optional[float] = Field(
        default=None,
        description="Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.",
    )
    speed: Optional[float] = Field(default=None)
