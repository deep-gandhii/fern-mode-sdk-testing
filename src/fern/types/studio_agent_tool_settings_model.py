from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class StudioAgentToolSettingsModel(BaseModel):
    """StudioAgentToolSettingsModel

    :param skip_confirmation: skip_confirmation, defaults to None
    :type skip_confirmation: bool, optional
    """

    skip_confirmation: Optional[bool] = Field(default=None)
