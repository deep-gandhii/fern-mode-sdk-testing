from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .content_threshold_guardrail import ContentThresholdGuardrail


class ContentConfig(BaseModel):
    """ContentConfig

    :param sexual: sexual, defaults to None
    :type sexual: ContentThresholdGuardrail, optional
    :param violence: violence, defaults to None
    :type violence: ContentThresholdGuardrail, optional
    :param harassment: harassment, defaults to None
    :type harassment: ContentThresholdGuardrail, optional
    :param self_harm: self_harm, defaults to None
    :type self_harm: ContentThresholdGuardrail, optional
    :param profanity: profanity, defaults to None
    :type profanity: ContentThresholdGuardrail, optional
    :param religion_or_politics: religion_or_politics, defaults to None
    :type religion_or_politics: ContentThresholdGuardrail, optional
    :param medical_and_legal_information: medical_and_legal_information, defaults to None
    :type medical_and_legal_information: ContentThresholdGuardrail, optional
    """

    sexual: Optional[ContentThresholdGuardrail] = Field(default=None)
    violence: Optional[ContentThresholdGuardrail] = Field(default=None)
    harassment: Optional[ContentThresholdGuardrail] = Field(default=None)
    self_harm: Optional[ContentThresholdGuardrail] = Field(default=None)
    profanity: Optional[ContentThresholdGuardrail] = Field(default=None)
    religion_or_politics: Optional[ContentThresholdGuardrail] = Field(default=None)
    medical_and_legal_information: Optional[ContentThresholdGuardrail] = Field(
        default=None
    )
