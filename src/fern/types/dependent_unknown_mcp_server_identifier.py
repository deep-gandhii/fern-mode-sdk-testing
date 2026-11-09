from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DependentUnknownMcpServerIdentifierType = typing.Union[
    typing.Literal["unknown"], typing.Any
]


class DependentUnknownMcpServerIdentifier(BaseModel):
    """DependentUnknownMcpServerIdentifier

    :param id: id
    :type id: str
    :param type: type, defaults to None
    :type type: DependentUnknownMcpServerIdentifierType, optional
    """

    id: str
    type: Optional[DependentUnknownMcpServerIdentifierType] = Field(default=None)
