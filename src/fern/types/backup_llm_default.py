from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

BackupLlmDefaultPreference = typing.Union[typing.Literal["default"], typing.Any]


class BackupLlmDefault(BaseModel):
    """BackupLlmDefault

    :param preference: preference, defaults to None
    :type preference: BackupLlmDefaultPreference, optional
    """

    preference: Optional[BackupLlmDefaultPreference] = Field(default=None)
