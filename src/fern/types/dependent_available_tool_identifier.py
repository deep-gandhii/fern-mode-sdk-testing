from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DependentAvailableToolIdentifierType = typing.Union[
    typing.Literal["available"], typing.Any
]

DependentAvailableToolIdentifierAccessLevel = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class DependentAvailableToolIdentifier(BaseModel):
    """DependentAvailableToolIdentifier

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param type: type, defaults to None
    :type type: DependentAvailableToolIdentifierType, optional
    :param created_at_unix_secs: created_at_unix_secs
    :type created_at_unix_secs: int
    :param access_level: access_level
    :type access_level: DependentAvailableToolIdentifierAccessLevel
    """

    id: str
    name: str
    type: Optional[DependentAvailableToolIdentifierType] = Field(default=None)
    created_at_unix_secs: int
    access_level: DependentAvailableToolIdentifierAccessLevel
