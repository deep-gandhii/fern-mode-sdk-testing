from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .turn_eagerness import TurnEagerness
from .spelling_patience import SpellingPatience
from .turn_model import TurnModel
from .soft_timeout_config_workflow_override import SoftTimeoutConfigWorkflowOverride


class TurnConfigWorkflowOverride(BaseModel):
    """TurnConfigWorkflowOverride

    :param turn_timeout: Maximum wait time for the user's reply before re-engaging the user, defaults to None
    :type turn_timeout: float, optional
    :param initial_wait_time: How long the agent will wait for the user to start the conversation if the first message is empty. If not set, uses the regular turn_timeout., defaults to None
    :type initial_wait_time: float, optional
    :param silence_end_call_timeout: Maximum wait time since the user last spoke before terminating the call, defaults to None
    :type silence_end_call_timeout: float, optional
    :param turn_eagerness: Controls how eager the agent is to respond. Low = less eager (waits longer), Standard = default eagerness, High = more eager (responds sooner), defaults to None
    :type turn_eagerness: TurnEagerness, optional
    :param spelling_patience: Controls if the agent should be more patient when user is spelling numbers and named entities. Auto = model based, Off = never wait extra, defaults to None
    :type spelling_patience: SpellingPatience, optional
    :param speculative_turn: When enabled, starts generating LLM responses during silence before full turn confidence is reached, reducing perceived latency. May increase LLM costs., defaults to None
    :type speculative_turn: bool, optional
    :param retranscribe_on_turn_timeout: When enabled, if VAD detects no speech, attempts to re-transcribe accumulated audio at turn timeout. Disables silence discount billing for affected turns., defaults to None
    :type retranscribe_on_turn_timeout: bool, optional
    :param turn_model: Version of the turn detection model to use., defaults to None
    :type turn_model: TurnModel, optional
    :param interruption_ignore_terms: List of terms that should not trigger an interruption when spoken by the user (e.g. 'gotcha', 'understood'). Uses case-insensitive exact matching., defaults to None
    :type interruption_ignore_terms: List[str], optional
    :param interruption_ignore_term_languages: Language codes for which preset ignore-term categories have been activated. Stored explicitly so display is not inferred from term overlap., defaults to None
    :type interruption_ignore_term_languages: List[str], optional
    :param transcribe_on_disabled_interruptions: When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn., defaults to None
    :type transcribe_on_disabled_interruptions: bool, optional
    :param soft_timeout_config: Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses., defaults to None
    :type soft_timeout_config: SoftTimeoutConfigWorkflowOverride, optional
    """

    turn_timeout: Optional[float] = Field(
        default=None,
        description="Maximum wait time for the user's reply before re-engaging the user",
    )
    initial_wait_time: Optional[float] = Field(
        default=None,
        description="How long the agent will wait for the user to start the conversation if the first message is empty. If not set, uses the regular turn_timeout.",
    )
    silence_end_call_timeout: Optional[float] = Field(
        default=None,
        description="Maximum wait time since the user last spoke before terminating the call",
    )
    turn_eagerness: Optional[TurnEagerness] = Field(
        default=None,
        description="Controls how eager the agent is to respond. Low = less eager (waits longer), Standard = default eagerness, High = more eager (responds sooner)",
    )
    spelling_patience: Optional[SpellingPatience] = Field(
        default=None,
        description="Controls if the agent should be more patient when user is spelling numbers and named entities. Auto = model based, Off = never wait extra",
    )
    speculative_turn: Optional[bool] = Field(
        default=None,
        description="When enabled, starts generating LLM responses during silence before full turn confidence is reached, reducing perceived latency. May increase LLM costs.",
    )
    retranscribe_on_turn_timeout: Optional[bool] = Field(
        default=None,
        description="When enabled, if VAD detects no speech, attempts to re-transcribe accumulated audio at turn timeout. Disables silence discount billing for affected turns.",
    )
    turn_model: Optional[TurnModel] = Field(
        default=None, description="Version of the turn detection model to use."
    )
    interruption_ignore_terms: Optional[List[str]] = Field(
        default=None,
        description="List of terms that should not trigger an interruption when spoken by the user (e.g. 'gotcha', 'understood'). Uses case-insensitive exact matching.",
    )
    interruption_ignore_term_languages: Optional[List[str]] = Field(
        default=None,
        description="Language codes for which preset ignore-term categories have been activated. Stored explicitly so display is not inferred from term overlap.",
    )
    transcribe_on_disabled_interruptions: Optional[bool] = Field(
        default=None,
        description="When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.",
    )
    soft_timeout_config: Optional[SoftTimeoutConfigWorkflowOverride] = Field(
        default=None,
        description="Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.",
    )
