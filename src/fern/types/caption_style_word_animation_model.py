from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CaptionStyleWordAnimationModelEnterType = typing.Union[
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

CaptionStyleWordAnimationModelExitType = typing.Union[
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


class CaptionStyleWordAnimationModel(BaseModel):
    """CaptionStyleWordAnimationModel

    :param enter_type: enter_type
    :type enter_type: CaptionStyleWordAnimationModelEnterType
    :param exit_type: exit_type
    :type exit_type: CaptionStyleWordAnimationModelExitType
    """

    enter_type: CaptionStyleWordAnimationModelEnterType
    exit_type: CaptionStyleWordAnimationModelExitType
