from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .focus_guardrail import FocusGuardrail
from .prompt_injection_guardrail import PromptInjectionGuardrail
from .content_guardrail_output import ContentGuardrailOutput
from .custom_guardrail_output import CustomGuardrailOutput

GuardrailsV1OutputVersion = typing.Union[typing.Literal["1"], typing.Any]


class GuardrailsV1Output(BaseModel):
    """GuardrailsV1Output

    :param version: version, defaults to None
    :type version: GuardrailsV1OutputVersion, optional
    :param focus: focus, defaults to None
    :type focus: FocusGuardrail, optional
    :param prompt_injection: prompt_injection, defaults to None
    :type prompt_injection: PromptInjectionGuardrail, optional
    :param content: content, defaults to None
    :type content: ContentGuardrailOutput, optional
    :param custom: Container for custom guardrails, matching ModerationGuardrail pattern, defaults to None
    :type custom: CustomGuardrailOutput, optional
    """

    version: Optional[GuardrailsV1OutputVersion] = Field(default=None)
    focus: Optional[FocusGuardrail] = Field(default=None)
    prompt_injection: Optional[PromptInjectionGuardrail] = Field(default=None)
    content: Optional[ContentGuardrailOutput] = Field(default=None)
    custom: Optional[CustomGuardrailOutput] = Field(
        default=None,
        description="Container for custom guardrails, matching ModerationGuardrail pattern",
    )
