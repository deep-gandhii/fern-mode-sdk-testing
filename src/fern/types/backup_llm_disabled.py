from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

BackupLlmDisabledPreference = typing.Union[typing.Literal["disabled"], typing.Any]


class BackupLlmDisabled(BaseModel):
    """BackupLlmDisabled

    :param preference: preference, defaults to None
    :type preference: BackupLlmDisabledPreference, optional
    """

    preference: Optional[BackupLlmDisabledPreference] = Field(default=None)
