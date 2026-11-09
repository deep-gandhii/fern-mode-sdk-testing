from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

LlmSchemaOverrideSource = typing.Union[typing.Literal["llm"], typing.Any]


class LlmSchemaOverride(BaseModel):
    """LlmSchemaOverride

    :param source: source, defaults to None
    :type source: LlmSchemaOverrideSource, optional
    :param prompt: Prompt override for the LLM. If not provided, the original schema description is used., defaults to None
    :type prompt: str, optional
    """

    source: Optional[LlmSchemaOverrideSource] = Field(default=None)
    prompt: Optional[str] = Field(
        default=None,
        description="Prompt override for the LLM. If not provided, the original schema description is used.",
    )
