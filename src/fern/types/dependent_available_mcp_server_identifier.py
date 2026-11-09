from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DependentAvailableMcpServerIdentifierType = typing.Union[
    typing.Literal["available"], typing.Any
]

DependentAvailableMcpServerIdentifierAccessLevel = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class DependentAvailableMcpServerIdentifier(BaseModel):
    """DependentAvailableMcpServerIdentifier

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param type: type, defaults to None
    :type type: DependentAvailableMcpServerIdentifierType, optional
    :param created_at_unix_secs: created_at_unix_secs
    :type created_at_unix_secs: int
    :param access_level: access_level
    :type access_level: DependentAvailableMcpServerIdentifierAccessLevel
    """

    id: str
    name: str
    type: Optional[DependentAvailableMcpServerIdentifierType] = Field(default=None)
    created_at_unix_secs: int
    access_level: DependentAvailableMcpServerIdentifierAccessLevel
