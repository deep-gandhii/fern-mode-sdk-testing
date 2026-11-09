from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CaptionStyleVerticalPlacementModelAlign = typing.Union[
    typing.Literal["top", "center", "bottom"], typing.Any
]


class CaptionStyleVerticalPlacementModel(BaseModel):
    """CaptionStyleVerticalPlacementModel

    :param align: align
    :type align: CaptionStyleVerticalPlacementModelAlign
    :param translate_pct: translate_pct
    :type translate_pct: float
    """

    align: CaptionStyleVerticalPlacementModelAlign
    translate_pct: float
