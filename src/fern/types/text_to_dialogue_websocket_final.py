from __future__ import annotations
from enum import Enum
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TextToDialogueWebsocketFinalIsFinal(Enum):
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
            map(
                lambda x: x.value,
                TextToDialogueWebsocketFinalIsFinal._member_map_.values(),
            )
        )


class TextToDialogueWebsocketFinal(BaseModel):
    """TextToDialogueWebsocketFinal

    :param is_final: Marks the end of the closing flush sequence.
    :type is_final: TextToDialogueWebsocketFinalIsFinal
    """

    is_final: TextToDialogueWebsocketFinalIsFinal = Field(
        default=True, description="Marks the end of the closing flush sequence."
    )
