from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

OmitSchemaOverrideSource = typing.Union[typing.Literal["omit"], typing.Any]


class OmitSchemaOverride(BaseModel):
    """OmitSchemaOverride

    :param source: source, defaults to None
    :type source: OmitSchemaOverrideSource, optional
    """

    source: Optional[OmitSchemaOverrideSource] = Field(default=None)
