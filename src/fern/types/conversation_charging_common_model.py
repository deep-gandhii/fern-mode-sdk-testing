from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .llm_category_usage import LlmCategoryUsage
from .platform_usage import PlatformUsage
from .conversation_tts_usage_model import ConversationTtsUsageModel
from .conversation_asr_usage_model import ConversationAsrUsageModel


class ConversationChargingCommonModel(BaseModel):
    """ConversationChargingCommonModel

    :param dev_discount: dev_discount, defaults to None
    :type dev_discount: bool, optional
    :param is_burst: is_burst, defaults to None
    :type is_burst: bool, optional
    :param tier: tier, defaults to None
    :type tier: str, optional
    :param llm_usage: llm_usage, defaults to None
    :type llm_usage: LlmCategoryUsage, optional
    :param llm_price: llm_price, defaults to None
    :type llm_price: float, optional
    :param llm_charge: llm_charge, defaults to None
    :type llm_charge: int, optional
    :param call_charge: call_charge, defaults to None
    :type call_charge: int, optional
    :param platform_charge: platform_charge, defaults to None
    :type platform_charge: int, optional
    :param platform_usage: Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``)., defaults to None
    :type platform_usage: PlatformUsage, optional
    :param platform_price: platform_price, defaults to None
    :type platform_price: float, optional
    :param free_minutes_consumed: free_minutes_consumed, defaults to None
    :type free_minutes_consumed: float, optional
    :param free_llm_dollars_consumed: free_llm_dollars_consumed, defaults to None
    :type free_llm_dollars_consumed: float, optional
    :param tts_usage: tts_usage, defaults to None
    :type tts_usage: ConversationTtsUsageModel, optional
    :param asr_usage: asr_usage, defaults to None
    :type asr_usage: ConversationAsrUsageModel, optional
    """

    dev_discount: Optional[bool] = Field(default=None)
    is_burst: Optional[bool] = Field(default=None)
    tier: Optional[str] = Field(default=None)
    llm_usage: Optional[LlmCategoryUsage] = Field(default=None)
    llm_price: Optional[float] = Field(default=None)
    llm_charge: Optional[int] = Field(default=None)
    call_charge: Optional[int] = Field(default=None)
    platform_charge: Optional[int] = Field(default=None)
    platform_usage: Optional[PlatformUsage] = Field(
        default=None,
        description="Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``).",
    )
    platform_price: Optional[float] = Field(default=None)
    free_minutes_consumed: Optional[float] = Field(default=None)
    free_llm_dollars_consumed: Optional[float] = Field(default=None)
    tts_usage: Optional[ConversationTtsUsageModel] = Field(default=None)
    asr_usage: Optional[ConversationAsrUsageModel] = Field(default=None)
