from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .llm import Llm

BackupLlmOverridePreference = typing.Union[typing.Literal["override"], typing.Any]


class BackupLlmOverride(BaseModel):
    """BackupLlmOverride

    :param preference: preference, defaults to None
    :type preference: BackupLlmOverridePreference, optional
    :param order: order
    :type order: List[Llm]
    """

    preference: Optional[BackupLlmOverridePreference] = Field(default=None)
    order: List[Llm]
