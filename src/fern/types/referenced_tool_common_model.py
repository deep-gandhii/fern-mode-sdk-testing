from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ReferencedToolCommonModelType = typing.Union[
    typing.Literal[
        "system",
        "webhook",
        "client",
        "workflow",
        "api_integration_webhook",
        "mcp",
        "code",
    ],
    typing.Any,
]


class ReferencedToolCommonModel(BaseModel):
    """Reference to a tool for unit test evaluation.

    :param id: The ID of the tool
    :type id: str
    :param type: The type of the tool
    :type type: ReferencedToolCommonModelType
    """

    id: str = Field(description="The ID of the tool")
    type: ReferencedToolCommonModelType = Field(description="The type of the tool")
