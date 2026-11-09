from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

RetryTriggerActionType = typing.Union[typing.Literal["retry"], typing.Any]


class RetryTriggerAction(BaseModel):
    """RetryTriggerAction

    :param type: type, defaults to None
    :type type: RetryTriggerActionType, optional
    :param feedback: Custom feedback to inject into the agent when retrying after guardrail trigger., defaults to None
    :type feedback: str, optional
    """

    type: Optional[RetryTriggerActionType] = Field(default=None)
    feedback: Optional[str] = Field(
        default=None,
        description="Custom feedback to inject into the agent when retrying after guardrail trigger.",
    )
