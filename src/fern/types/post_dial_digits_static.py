from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PostDialDigitsStaticType = typing.Union[typing.Literal["static"], typing.Any]


class PostDialDigitsStatic(BaseModel):
    """PostDialDigitsStatic

    :param type: type, defaults to None
    :type type: PostDialDigitsStaticType, optional
    :param value: DTMF digits to send after call connects (e.g., 'ww1234' for extension)
    :type value: str
    """

    type: Optional[PostDialDigitsStaticType] = Field(default=None)
    value: str = Field(
        description="DTMF digits to send after call connects (e.g., 'ww1234' for extension)"
    )
