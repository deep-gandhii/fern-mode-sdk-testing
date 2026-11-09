from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .evaluation_settings_output import EvaluationSettingsOutput
from .widget_config import WidgetConfig
from .analysis_property import AnalysisProperty
from .analysis_scope import AnalysisScope
from .agent_analysis_items_output import AgentAnalysisItemsOutput
from .conversation_initiation_client_data_config_output import (
    ConversationInitiationClientDataConfigOutput,
)
from .agent_workspace_overrides_output import AgentWorkspaceOverridesOutput
from .agent_testing_settings import AgentTestingSettings
from .guardrails_v_1_output import GuardrailsV1Output
from .auth_settings import AuthSettings
from .agent_call_limits import AgentCallLimits
from .privacy_config_output import PrivacyConfigOutput
from .agent_trust_context import AgentTrustContext
from .llm import Llm
from .topic_discovery_settings import TopicDiscoverySettings
from .sentiment_analysis_settings import SentimentAnalysisSettings
from .safety_response_model import SafetyResponseModel


class AgentPlatformSettingsResponseModel(BaseModel):
    """AgentPlatformSettingsResponseModel

    :param evaluation: Settings to evaluate an agent's performance. Agents are evaluated against a set of criteria, with success being defined as meeting some combination of those criteria., defaults to None
    :type evaluation: EvaluationSettingsOutput, optional
    :param widget: widget, defaults to None
    :type widget: WidgetConfig, optional
    :param data_collection: Data collection settings, defaults to None
    :type data_collection: Dict[str, AnalysisProperty], optional
    :param data_collection_scopes: Scope per data collection item ID. Missing keys default to conversation scope., defaults to None
    :type data_collection_scopes: Dict[str, AnalysisScope], optional
    :param analysis_items: Evaluation + data-collection items attached by reference. None means the agent has not been migrated onto analysis items yet (distinct from an empty, migrated set); reads fall back to the legacy evaluation/data_collection fields in that case., defaults to None
    :type analysis_items: AgentAnalysisItemsOutput, optional
    :param overrides: overrides, defaults to None
    :type overrides: ConversationInitiationClientDataConfigOutput, optional
    :param workspace_overrides: workspace_overrides, defaults to None
    :type workspace_overrides: AgentWorkspaceOverridesOutput, optional
    :param testing: Settings for agent testing configuration., defaults to None
    :type testing: AgentTestingSettings, optional
    :param archived: Whether the agent is archived, defaults to None
    :type archived: bool, optional
    :param guardrails: guardrails, defaults to None
    :type guardrails: GuardrailsV1Output, optional
    :param summary_language: Language for all conversation analysis outputs (summaries, titles, evaluation rationales, data collection rationales). If not set, the language will be inferred from the conversation. Must be one of the supported conversation languages., defaults to None
    :type summary_language: str, optional
    :param auto_translate_transcript_to_app_language: When enabled, a conversation transcript is automatically translated to the viewer's application language when they open the transcript page. If not set or false, transcripts are shown in their original language unless the viewer manually selects a translation., defaults to None
    :type auto_translate_transcript_to_app_language: bool, optional
    :param auth: auth, defaults to None
    :type auth: AuthSettings, optional
    :param call_limits: call_limits, defaults to None
    :type call_limits: AgentCallLimits, optional
    :param privacy: privacy, defaults to None
    :type privacy: PrivacyConfigOutput, optional
    :param trust_context: The trust context in which the agent operates. UNKNOWN: not yet classified (existing agents created before this feature). LOW: serves untrusted external participants (e.g. customer support, sales) — outputs should be vetted and tool access scoped. HIGH: serves the owner (e.g. personal assistant) — full tool access is appropriate., defaults to None
    :type trust_context: AgentTrustContext, optional
    :param analysis_llm: analysis_llm, defaults to None
    :type analysis_llm: Llm, optional
    :param topic_discovery: Per-agent topic-discovery configuration. Cadence and analysis window are managed internally; this only exposes the customer-facing on/off toggle., defaults to None
    :type topic_discovery: TopicDiscoverySettings, optional
    :param sentiment_analysis: sentiment_analysis, defaults to None
    :type sentiment_analysis: SentimentAnalysisSettings, optional
    :param safety: safety, defaults to None
    :type safety: SafetyResponseModel, optional
    """

    evaluation: Optional[EvaluationSettingsOutput] = Field(
        default=None,
        description="Settings to evaluate an agent's performance. Agents are evaluated against a set of criteria, with success being defined as meeting some combination of those criteria.",
    )
    widget: Optional[WidgetConfig] = Field(default=None)
    data_collection: Optional[Dict[str, AnalysisProperty]] = Field(
        default=None, description="Data collection settings"
    )
    data_collection_scopes: Optional[Dict[str, AnalysisScope]] = Field(
        default=None,
        description="Scope per data collection item ID. Missing keys default to conversation scope.",
    )
    analysis_items: Optional[AgentAnalysisItemsOutput] = Field(
        default=None,
        description="Evaluation + data-collection items attached by reference. None means the agent has not been migrated onto analysis items yet (distinct from an empty, migrated set); reads fall back to the legacy evaluation/data_collection fields in that case.",
    )
    overrides: Optional[ConversationInitiationClientDataConfigOutput] = Field(
        default=None
    )
    workspace_overrides: Optional[AgentWorkspaceOverridesOutput] = Field(default=None)
    testing: Optional[AgentTestingSettings] = Field(
        default=None, description="Settings for agent testing configuration."
    )
    archived: Optional[bool] = Field(
        default=None, description="Whether the agent is archived"
    )
    guardrails: Optional[GuardrailsV1Output] = Field(default=None)
    summary_language: Optional[str] = Field(
        default=None,
        description="Language for all conversation analysis outputs (summaries, titles, evaluation rationales, data collection rationales). If not set, the language will be inferred from the conversation. Must be one of the supported conversation languages.",
    )
    auto_translate_transcript_to_app_language: Optional[bool] = Field(
        default=None,
        description="When enabled, a conversation transcript is automatically translated to the viewer's application language when they open the transcript page. If not set or false, transcripts are shown in their original language unless the viewer manually selects a translation.",
    )
    auth: Optional[AuthSettings] = Field(default=None)
    call_limits: Optional[AgentCallLimits] = Field(default=None)
    privacy: Optional[PrivacyConfigOutput] = Field(default=None)
    trust_context: Optional[AgentTrustContext] = Field(
        default=None,
        description="The trust context in which the agent operates. UNKNOWN: not yet classified (existing agents created before this feature). LOW: serves untrusted external participants (e.g. customer support, sales) — outputs should be vetted and tool access scoped. HIGH: serves the owner (e.g. personal assistant) — full tool access is appropriate.",
    )
    analysis_llm: Optional[Llm] = Field(default=None)
    topic_discovery: Optional[TopicDiscoverySettings] = Field(
        default=None,
        description="Per-agent topic-discovery configuration. Cadence and analysis window are managed internally; this only exposes the customer-facing on/off toggle.",
    )
    sentiment_analysis: Optional[SentimentAnalysisSettings] = Field(default=None)
    safety: Optional[SafetyResponseModel] = Field(default=None)
