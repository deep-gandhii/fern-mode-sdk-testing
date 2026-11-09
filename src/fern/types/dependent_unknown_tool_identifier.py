from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DependentUnknownToolIdentifierType = typing.Union[typing.Literal["unknown"], typing.Any]


class DependentUnknownToolIdentifier(BaseModel):
    """A model that represents an tool dependent on a knowledge base/tools to which the user has no direct access.

    :param type: type, defaults to None
    :type type: DependentUnknownToolIdentifierType, optional
    :param id: id
    :type id: str
    """

    type: Optional[DependentUnknownToolIdentifierType] = Field(default=None)
    id: str
