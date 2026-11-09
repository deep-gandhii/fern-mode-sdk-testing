from __future__ import annotations
from enum import Enum
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class FinalOutputMultiIsFinal(Enum):
    """An enumeration representing different categories.

    :cvar TRUE: True
    :vartype TRUE: str
    """

    TRUE = True

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, FinalOutputMultiIsFinal._member_map_.values())
        )


class FinalOutputMulti(BaseModel):
    """Server payload indicating the final output for a specific context.

    :param is_final: Indicates this is the final message for the context.
    :type is_final: FinalOutputMultiIsFinal
    :param context_id: The context_id for which this is the final message., defaults to None
    :type context_id: str, optional
    """

    is_final: FinalOutputMultiIsFinal = Field(
        alias="isFinal",
        serialization_alias="isFinal",
        default=True,
        description="Indicates this is the final message for the context.",
    )
    context_id: Optional[str] = Field(
        alias="contextId",
        serialization_alias="contextId",
        default=None,
        description="The context_id for which this is the final message.",
    )
