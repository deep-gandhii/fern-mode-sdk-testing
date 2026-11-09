from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .asr_conversational_config_workflow_override import (
    AsrConversationalConfigWorkflowOverride,
)
from .turn_config_workflow_override import TurnConfigWorkflowOverride
from .tts_conversational_config_workflow_override_input import (
    TtsConversationalConfigWorkflowOverrideInput,
)
from .conversation_config_workflow_override_input import (
    ConversationConfigWorkflowOverrideInput,
)
from .language_preset_input import LanguagePresetInput
from .vad_config_workflow_override import VadConfigWorkflowOverride
from .agent_config_api_model_workflow_override_input import (
    AgentConfigApiModelWorkflowOverrideInput,
)


class ConversationalConfigApiModelWorkflowOverrideInput(BaseModel):
    """ConversationalConfigApiModelWorkflowOverrideInput

    :param asr: Configuration for conversational transcription, defaults to None
    :type asr: AsrConversationalConfigWorkflowOverride, optional
    :param turn: Configuration for turn detection, defaults to None
    :type turn: TurnConfigWorkflowOverride, optional
    :param tts: Configuration for conversational text to speech, defaults to None
    :type tts: TtsConversationalConfigWorkflowOverrideInput, optional
    :param conversation: Configuration for conversational events, defaults to None
    :type conversation: ConversationConfigWorkflowOverrideInput, optional
    :param language_presets: Language presets for conversations, defaults to None
    :type language_presets: Dict[str, LanguagePresetInput], optional
    :param vad: Configuration for voice activity detection, defaults to None
    :type vad: VadConfigWorkflowOverride, optional
    :param agent: Agent specific configuration, defaults to None
    :type agent: AgentConfigApiModelWorkflowOverrideInput, optional
    """

    asr: Optional[AsrConversationalConfigWorkflowOverride] = Field(
        default=None, description="Configuration for conversational transcription"
    )
    turn: Optional[TurnConfigWorkflowOverride] = Field(
        default=None, description="Configuration for turn detection"
    )
    tts: Optional[TtsConversationalConfigWorkflowOverrideInput] = Field(
        default=None, description="Configuration for conversational text to speech"
    )
    conversation: Optional[ConversationConfigWorkflowOverrideInput] = Field(
        default=None, description="Configuration for conversational events"
    )
    language_presets: Optional[Dict[str, LanguagePresetInput]] = Field(
        default=None, description="Language presets for conversations"
    )
    vad: Optional[VadConfigWorkflowOverride] = Field(
        default=None, description="Configuration for voice activity detection"
    )
    agent: Optional[AgentConfigApiModelWorkflowOverrideInput] = Field(
        default=None, description="Agent specific configuration"
    )
