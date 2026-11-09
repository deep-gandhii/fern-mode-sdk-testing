from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SpeechEngineConversationInitiationClientDataConfig(BaseModel):
    """SpeechEngineConversationInitiationClientDataConfig

    :param first_message: Whether the first message can be overridden by the client, defaults to None
    :type first_message: bool, optional
    """

    first_message: Optional[bool] = Field(
        default=None,
        description="Whether the first message can be overridden by the client",
    )
