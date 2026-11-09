from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_config_client_override_output import (
    ConversationConfigClientOverrideOutput,
)
from .language_preset_translation import LanguagePresetTranslation


class LanguagePresetOutput(BaseModel):
    """LanguagePresetOutput

    :param overrides: overrides
    :type overrides: ConversationConfigClientOverrideOutput
    :param first_message_translation: The translation of the first message, defaults to None
    :type first_message_translation: LanguagePresetTranslation, optional
    :param soft_timeout_translation: The translation of the soft timeout message, defaults to None
    :type soft_timeout_translation: LanguagePresetTranslation, optional
    """

    overrides: ConversationConfigClientOverrideOutput
    first_message_translation: Optional[LanguagePresetTranslation] = Field(
        default=None, description="The translation of the first message"
    )
    soft_timeout_translation: Optional[LanguagePresetTranslation] = Field(
        default=None, description="The translation of the soft timeout message"
    )
