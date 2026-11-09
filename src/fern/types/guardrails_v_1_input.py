from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .focus_guardrail import FocusGuardrail
from .prompt_injection_guardrail import PromptInjectionGuardrail
from .content_guardrail_input import ContentGuardrailInput
from .custom_guardrail_input import CustomGuardrailInput

GuardrailsV1InputVersion = typing.Union[typing.Literal["1"], typing.Any]


class GuardrailsV1Input(BaseModel):
    """GuardrailsV1Input

    :param version: version, defaults to None
    :type version: GuardrailsV1InputVersion, optional
    :param focus: focus, defaults to None
    :type focus: FocusGuardrail, optional
    :param prompt_injection: prompt_injection, defaults to None
    :type prompt_injection: PromptInjectionGuardrail, optional
    :param content: content, defaults to None
    :type content: ContentGuardrailInput, optional
    :param custom: Container for custom guardrails, matching ModerationGuardrail pattern, defaults to None
    :type custom: CustomGuardrailInput, optional
    """

    version: Optional[GuardrailsV1InputVersion] = Field(default=None)
    focus: Optional[FocusGuardrail] = Field(default=None)
    prompt_injection: Optional[PromptInjectionGuardrail] = Field(default=None)
    content: Optional[ContentGuardrailInput] = Field(default=None)
    custom: Optional[CustomGuardrailInput] = Field(
        default=None,
        description="Container for custom guardrails, matching ModerationGuardrail pattern",
    )
