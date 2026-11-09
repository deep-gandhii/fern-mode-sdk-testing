from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CaptionStyleHorizontalPlacementModelAlign = typing.Union[
    typing.Literal["left", "center", "right"], typing.Any
]


class CaptionStyleHorizontalPlacementModel(BaseModel):
    """CaptionStyleHorizontalPlacementModel

    :param align: align
    :type align: CaptionStyleHorizontalPlacementModelAlign
    :param translate_pct: translate_pct
    :type translate_pct: float
    """

    align: CaptionStyleHorizontalPlacementModelAlign
    translate_pct: float
