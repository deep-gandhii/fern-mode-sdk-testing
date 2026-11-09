from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

SayNodePromptMessageOutputType = typing.Union[typing.Literal["prompt"], typing.Any]


class SayNodePromptMessageOutput(BaseModel):
    """SayNodePromptMessageOutput

    :param type: type
    :type type: SayNodePromptMessageOutputType
    :param prompt: LLM prompt describing what message should be generated.
    :type prompt: str
    """

    type: SayNodePromptMessageOutputType = Field(default="prompt")
    prompt: str = Field(
        description="LLM prompt describing what message should be generated."
    )
