from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

EndCallTriggerActionType = typing.Union[typing.Literal["end_call"], typing.Any]


class EndCallTriggerAction(BaseModel):
    """EndCallTriggerAction

    :param type: type, defaults to None
    :type type: EndCallTriggerActionType, optional
    """

    type: Optional[EndCallTriggerActionType] = Field(default=None)
