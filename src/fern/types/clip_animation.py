from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ClipAnimationEnterEffect = typing.Union[
    typing.Literal[
        "none",
        "fade",
        "float",
        "gentle_float",
        "zoom_in",
        "drop",
        "slide_left",
        "slide_right",
        "slide_up",
        "slide_down",
        "pop",
        "bounce",
        "spin",
        "slide_bounce",
    ],
    typing.Any,
]

ClipAnimationExitEffect = typing.Union[
    typing.Literal[
        "none",
        "fade",
        "float",
        "gentle_float",
        "zoom_in",
        "drop",
        "slide_left",
        "slide_right",
        "slide_up",
        "slide_down",
        "pop",
        "bounce",
        "spin",
        "slide_bounce",
    ],
    typing.Any,
]


class ClipAnimation(BaseModel):
    """ClipAnimation

    :param enter_effect: enter_effect, defaults to None
    :type enter_effect: ClipAnimationEnterEffect, optional
    :param enter_duration_ms: enter_duration_ms, defaults to None
    :type enter_duration_ms: int, optional
    :param exit_effect: exit_effect, defaults to None
    :type exit_effect: ClipAnimationExitEffect, optional
    :param exit_duration_ms: exit_duration_ms, defaults to None
    :type exit_duration_ms: int, optional
    """

    enter_effect: Optional[ClipAnimationEnterEffect] = Field(default=None)
    enter_duration_ms: Optional[int] = Field(default=None)
    exit_effect: Optional[ClipAnimationExitEffect] = Field(default=None)
    exit_duration_ms: Optional[int] = Field(default=None)
