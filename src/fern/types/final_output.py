from __future__ import annotations
from enum import Enum
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class FinalOutputIsFinal(Enum):
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
        return list(map(lambda x: x.value, FinalOutputIsFinal._member_map_.values()))


class FinalOutput(BaseModel):
    """FinalOutput

    :param is_final: Indicates if the generation is complete. If set to `True`, `audio` will be null., defaults to None
    :type is_final: FinalOutputIsFinal, optional
    """

    is_final: Optional[FinalOutputIsFinal] = Field(
        alias="isFinal",
        serialization_alias="isFinal",
        default=None,
        description="Indicates if the generation is complete. If set to `True`, `audio` will be null.",
    )
