from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .llm import Llm
from .llm_deprecation_config_model import LlmDeprecationConfigModel


class LlmDeprecationInfoModel(BaseModel):
    """LlmDeprecationInfoModel

    :param llm: llm
    :type llm: Llm
    :param is_deprecated: Whether this model is currently deprecated. True if the model is immediately deprecated or within the warning period.
    :type is_deprecated: bool
    :param is_in_warning_period: Whether this model is currently in the warning period before deprecation., defaults to None
    :type is_in_warning_period: bool, optional
    :param is_in_fallback_period: Whether traffic is currently being progressively routed to the replacement model., defaults to None
    :type is_in_fallback_period: bool, optional
    :param fallback_percentage: Current percentage of traffic being routed to the replacement model (0-100)., defaults to None
    :type fallback_percentage: int, optional
    :param provider_deprecation_date: The date when the model provider will deprecate this model. Null for immediately deprecated models., defaults to None
    :type provider_deprecation_date: str, optional
    :param replacement_model: The model that replaces this deprecated model. Traffic will be automatically routed to this model., defaults to None
    :type replacement_model: Llm, optional
    :param deprecation_config: Custom deprecation timing configuration for this model. Null if using the default configuration., defaults to None
    :type deprecation_config: LlmDeprecationConfigModel, optional
    """

    llm: Llm
    is_deprecated: bool = Field(
        description="Whether this model is currently deprecated. True if the model is immediately deprecated or within the warning period."
    )
    is_in_warning_period: Optional[bool] = Field(
        default=None,
        description="Whether this model is currently in the warning period before deprecation.",
    )
    is_in_fallback_period: Optional[bool] = Field(
        default=None,
        description="Whether traffic is currently being progressively routed to the replacement model.",
    )
    fallback_percentage: Optional[int] = Field(
        default=None,
        description="Current percentage of traffic being routed to the replacement model (0-100).",
    )
    provider_deprecation_date: Optional[str] = Field(
        default=None,
        description="The date when the model provider will deprecate this model. Null for immediately deprecated models.",
    )
    replacement_model: Optional[Llm] = Field(
        default=None,
        description="The model that replaces this deprecated model. Traffic will be automatically routed to this model.",
    )
    deprecation_config: Optional[LlmDeprecationConfigModel] = Field(
        default=None,
        description="Custom deprecation timing configuration for this model. Null if using the default configuration.",
    )
