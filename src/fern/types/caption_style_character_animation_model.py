from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CaptionStyleCharacterAnimationModelEnterType = typing.Union[
    typing.Literal["none", "fade", "typewriter"], typing.Any
]

CaptionStyleCharacterAnimationModelExitType = typing.Union[
    typing.Literal["none", "fade"], typing.Any
]


class CaptionStyleCharacterAnimationModel(BaseModel):
    """CaptionStyleCharacterAnimationModel

    :param enter_type: enter_type
    :type enter_type: CaptionStyleCharacterAnimationModelEnterType
    :param exit_type: exit_type
    :type exit_type: CaptionStyleCharacterAnimationModelExitType
    """

    enter_type: CaptionStyleCharacterAnimationModelEnterType
    exit_type: CaptionStyleCharacterAnimationModelExitType
