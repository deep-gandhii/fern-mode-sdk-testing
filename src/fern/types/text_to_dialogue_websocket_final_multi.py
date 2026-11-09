from __future__ import annotations
from enum import Enum
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TextToDialogueWebsocketFinalMultiIsFinal(Enum):
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
                TextToDialogueWebsocketFinalMultiIsFinal._member_map_.values(),
            )
        )


class TextToDialogueWebsocketFinalMulti(BaseModel):
    """TextToDialogueWebsocketFinalMulti

    :param is_final: Marks the end of this context's closing flush sequence.
    :type is_final: TextToDialogueWebsocketFinalMultiIsFinal
    :param context_id: The context that has been finalized., defaults to None
    :type context_id: str, optional
    """

    is_final: TextToDialogueWebsocketFinalMultiIsFinal = Field(
        default=True,
        description="Marks the end of this context's closing flush sequence.",
    )
    context_id: Optional[str] = Field(
        default=None, description="The context that has been finalized."
    )
