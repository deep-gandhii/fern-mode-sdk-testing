from __future__ import annotations
import typing
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .guardrail_execution_mode import GuardrailExecutionMode
from .end_call_trigger_action import EndCallTriggerAction
from .retry_trigger_action import RetryTriggerAction

CustomGuardrailConfigModel = typing.Union[
    typing.Literal[
        "gemini-2.5-flash-lite",
        "gemini-2.5-flash",
        "gemini-3.1-flash-lite",
        "gemini-3.5-flash",
        "claude-haiku-4-5",
        "claude-sonnet-4-6",
        "gpt-5.4-nano",
        "gpt-5.4-mini",
    ],
    typing.Any,
]


# fernMode variant type for a shared-component member of CustomGuardrailConfigTriggerAction
class CustomGuardrailConfigTriggerAction_EndCall(EndCallTriggerAction):
    pass


# fernMode variant type for a shared-component member of CustomGuardrailConfigTriggerAction
class CustomGuardrailConfigTriggerAction_Retry(RetryTriggerAction):
    pass


# Union type for CustomGuardrailConfigTriggerAction
# Pydantic will attempt to validate against each type in order
CustomGuardrailConfigTriggerAction = Union[EndCallTriggerAction, RetryTriggerAction]
# TypeAdapter for runtime validation of CustomGuardrailConfigTriggerAction
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

CustomGuardrailConfigTriggerAction_adapter = TypeAdapter(
    CustomGuardrailConfigTriggerAction
)


class CustomGuardrailConfig(BaseModel):
    """Single custom guardrail configuration

    :param is_enabled: is_enabled, defaults to None
    :type is_enabled: bool, optional
    :param name: User-facing name for this guardrail
    :type name: str
    :param prompt: Instruction describing what to block, e.g. 'don't talk about politics'
    :type prompt: str
    :param execution_mode: execution_mode, defaults to None
    :type execution_mode: GuardrailExecutionMode, optional
    :param model: LLM model to use for custom guardrail evaluation, defaults to None
    :type model: CustomGuardrailConfigModel, optional
    :param history_message_count: How much recent history the guardrail sees before the reply it evaluates, counted in user messages (the agent replies between them are included too). The guardrail always gets a single <conversation_history> transcript ending in the evaluated reply, marked 'AGENT [current reply]:'. 0 (default) adds no prior history (just that line); 1 adds the latest user message onward., defaults to None
    :type history_message_count: int, optional
    :param trigger_action: trigger_action, defaults to None
    :type trigger_action: CustomGuardrailConfigTriggerAction, optional
    :param evaluate_full_response_only: Evaluate once against the complete non-TTS response instead of cumulative partials. Requires blocking mode., defaults to None
    :type evaluate_full_response_only: bool, optional
    """

    is_enabled: Optional[bool] = Field(default=None)
    name: str = Field(description="User-facing name for this guardrail")
    prompt: str = Field(
        description="Instruction describing what to block, e.g. 'don't talk about politics'"
    )
    execution_mode: Optional[GuardrailExecutionMode] = Field(default=None)
    model: Optional[CustomGuardrailConfigModel] = Field(
        default=None, description="LLM model to use for custom guardrail evaluation"
    )
    history_message_count: Optional[int] = Field(
        default=None,
        description="How much recent history the guardrail sees before the reply it evaluates, counted in user messages (the agent replies between them are included too). The guardrail always gets a single <conversation_history> transcript ending in the evaluated reply, marked 'AGENT [current reply]:'. 0 (default) adds no prior history (just that line); 1 adds the latest user message onward.",
    )
    trigger_action: Optional[CustomGuardrailConfigTriggerAction] = Field(default=None)
    evaluate_full_response_only: Optional[bool] = Field(
        default=None,
        description="Evaluate once against the complete non-TTS response instead of cumulative partials. Requires blocking mode.",
    )
