from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_initiation_source import ConversationInitiationSource


class ConversationInitiationSourceInfo(BaseModel):
    """Information about the source of conversation initiation

    :param source: Source of the conversation initiation, defaults to None
    :type source: ConversationInitiationSource, optional
    :param version: The SDK version number, defaults to None
    :type version: str, optional
    """

    source: Optional[ConversationInitiationSource] = Field(
        default=None, description="Source of the conversation initiation"
    )
    version: Optional[str] = Field(default=None, description="The SDK version number")
