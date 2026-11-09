from __future__ import annotations
import typing
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel

ThresholdOne = typing.Union[typing.Literal["low", "medium", "high"], typing.Any]


# Union type for ContentThresholdGuardrailThreshold
# Pydantic will attempt to validate against each type in order
ContentThresholdGuardrailThreshold = Union[float, str]
# TypeAdapter for runtime validation of ContentThresholdGuardrailThreshold
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ContentThresholdGuardrailThreshold_adapter = TypeAdapter(
    ContentThresholdGuardrailThreshold
)


class ContentThresholdGuardrail(BaseModel):
    """ContentThresholdGuardrail

    :param is_enabled: is_enabled, defaults to None
    :type is_enabled: bool, optional
    :param threshold: threshold, defaults to None
    :type threshold: ContentThresholdGuardrailThreshold, optional
    """

    is_enabled: Optional[bool] = Field(default=None)
    threshold: Optional[ContentThresholdGuardrailThreshold] = Field(default=None)
