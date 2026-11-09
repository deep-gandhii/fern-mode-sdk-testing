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
from .tts_conversational_config_workflow_override_output import (
    TtsConversationalConfigWorkflowOverrideOutput,
)
from .conversation_config_workflow_override_output import (
    ConversationConfigWorkflowOverrideOutput,
)
from .language_preset_output import LanguagePresetOutput
from .vad_config_workflow_override import VadConfigWorkflowOverride
from .agent_config_api_model_workflow_override_output import (
    AgentConfigApiModelWorkflowOverrideOutput,
)


class ConversationalConfigApiModelWorkflowOverrideOutput(BaseModel):
    """ConversationalConfigApiModelWorkflowOverrideOutput

    :param asr: Configuration for conversational transcription, defaults to None
    :type asr: AsrConversationalConfigWorkflowOverride, optional
    :param turn: Configuration for turn detection, defaults to None
    :type turn: TurnConfigWorkflowOverride, optional
    :param tts: Configuration for conversational text to speech, defaults to None
    :type tts: TtsConversationalConfigWorkflowOverrideOutput, optional
    :param conversation: Configuration for conversational events, defaults to None
    :type conversation: ConversationConfigWorkflowOverrideOutput, optional
    :param language_presets: Language presets for conversations, defaults to None
    :type language_presets: Dict[str, LanguagePresetOutput], optional
    :param vad: Configuration for voice activity detection, defaults to None
    :type vad: VadConfigWorkflowOverride, optional
    :param agent: Agent specific configuration, defaults to None
    :type agent: AgentConfigApiModelWorkflowOverrideOutput, optional
    """

    asr: Optional[AsrConversationalConfigWorkflowOverride] = Field(
        default=None, description="Configuration for conversational transcription"
    )
    turn: Optional[TurnConfigWorkflowOverride] = Field(
        default=None, description="Configuration for turn detection"
    )
    tts: Optional[TtsConversationalConfigWorkflowOverrideOutput] = Field(
        default=None, description="Configuration for conversational text to speech"
    )
    conversation: Optional[ConversationConfigWorkflowOverrideOutput] = Field(
        default=None, description="Configuration for conversational events"
    )
    language_presets: Optional[Dict[str, LanguagePresetOutput]] = Field(
        default=None, description="Language presets for conversations"
    )
    vad: Optional[VadConfigWorkflowOverride] = Field(
        default=None, description="Configuration for voice activity detection"
    )
    agent: Optional[AgentConfigApiModelWorkflowOverrideOutput] = Field(
        default=None, description="Agent specific configuration"
    )
