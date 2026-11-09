from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

SayNodePromptMessageInputType = typing.Union[typing.Literal["prompt"], typing.Any]


class SayNodePromptMessageInput(BaseModel):
    """SayNodePromptMessageInput

    :param type: type, defaults to None
    :type type: SayNodePromptMessageInputType, optional
    :param prompt: LLM prompt describing what message should be generated.
    :type prompt: str
    """

    type: Optional[SayNodePromptMessageInputType] = Field(default=None)
    prompt: str = Field(
        description="LLM prompt describing what message should be generated."
    )
