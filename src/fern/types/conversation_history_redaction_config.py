from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .config_entity_type import ConfigEntityType


class ConversationHistoryRedactionConfig(BaseModel):
    """ConversationHistoryRedactionConfig

    :param enabled: Whether conversation history redaction is enabled, defaults to None
    :type enabled: bool, optional
    :param entities: The entities to redact from the conversation transcript, audio and analysis. Use top-level types like 'name', 'email_address', or dot notation for specific subtypes like 'name.full_name'., defaults to None
    :type entities: List[ConfigEntityType], optional
    """

    enabled: Optional[bool] = Field(
        default=None, description="Whether conversation history redaction is enabled"
    )
    entities: Optional[List[ConfigEntityType]] = Field(
        default=None,
        description="The entities to redact from the conversation transcript, audio and analysis. Use top-level types like 'name', 'email_address', or dot notation for specific subtypes like 'name.full_name'.",
    )
