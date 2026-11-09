from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CaptionStyleSectionAnimationModelEnterType = typing.Union[
    typing.Literal[
        "none",
        "fade",
        "scale",
        "pop",
        "slide_up",
        "slide_down",
        "slam",
        "scale_down",
        "slide_in",
    ],
    typing.Any,
]

CaptionStyleSectionAnimationModelExitType = typing.Union[
    typing.Literal[
        "none",
        "fade",
        "scale",
        "pop",
        "slide_up",
        "slide_down",
        "slam",
        "scale_down",
        "slide_in",
    ],
    typing.Any,
]


class CaptionStyleSectionAnimationModel(BaseModel):
    """CaptionStyleSectionAnimationModel

    :param enter_type: enter_type
    :type enter_type: CaptionStyleSectionAnimationModelEnterType
    :param exit_type: exit_type
    :type exit_type: CaptionStyleSectionAnimationModelExitType
    """

    enter_type: CaptionStyleSectionAnimationModelEnterType
    exit_type: CaptionStyleSectionAnimationModelExitType
