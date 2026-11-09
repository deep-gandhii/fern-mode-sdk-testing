from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DependentUnknownAgentIdentifierType = typing.Union[
    typing.Literal["unknown"], typing.Any
]


class DependentUnknownAgentIdentifier(BaseModel):
    """A model that represents an agent dependent on a knowledge base/tools to which the user has no direct access.

    :param referenced_resource_ids: If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly., defaults to None
    :type referenced_resource_ids: List[str], optional
    :param id: id
    :type id: str
    :param type: type, defaults to None
    :type type: DependentUnknownAgentIdentifierType, optional
    """

    referenced_resource_ids: Optional[List[str]] = Field(
        default=None,
        description="If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.",
    )
    id: str
    type: Optional[DependentUnknownAgentIdentifierType] = Field(default=None)
