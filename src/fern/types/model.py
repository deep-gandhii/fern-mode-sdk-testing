from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .language_response import LanguageResponse
from .model_rates_response_model import ModelRatesResponseModel


class Model(BaseModel):
    """Model

    :param model_id: The unique identifier of the model.
    :type model_id: str
    :param name: The name of the model., defaults to None
    :type name: str, optional
    :param can_be_finetuned: Whether the model can be finetuned., defaults to None
    :type can_be_finetuned: bool, optional
    :param can_do_text_to_speech: Whether the model can do text-to-speech., defaults to None
    :type can_do_text_to_speech: bool, optional
    :param can_do_voice_conversion: Whether the model can do voice conversion., defaults to None
    :type can_do_voice_conversion: bool, optional
    :param can_use_style: Whether the model can use style., defaults to None
    :type can_use_style: bool, optional
    :param can_use_speaker_boost: Whether the model can use speaker boost., defaults to None
    :type can_use_speaker_boost: bool, optional
    :param serves_pro_voices: Whether the model serves pro voices., defaults to None
    :type serves_pro_voices: bool, optional
    :param token_cost_factor: The cost factor for the model., defaults to None
    :type token_cost_factor: float, optional
    :param description: The description of the model., defaults to None
    :type description: str, optional
    :param requires_alpha_access: Whether the model requires alpha access., defaults to None
    :type requires_alpha_access: bool, optional
    :param max_characters_request_free_user: The maximum number of characters that can be requested by a free user., defaults to None
    :type max_characters_request_free_user: int, optional
    :param max_characters_request_subscribed_user: The maximum number of characters that can be requested by a subscribed user., defaults to None
    :type max_characters_request_subscribed_user: int, optional
    :param maximum_text_length_per_request: The maximum length of text that can be requested for this model., defaults to None
    :type maximum_text_length_per_request: int, optional
    :param languages: The languages supported by the model., defaults to None
    :type languages: List[LanguageResponse], optional
    :param model_rates: model_rates, defaults to None
    :type model_rates: ModelRatesResponseModel, optional
    :param concurrency_group: The concurrency group for the model., defaults to None
    :type concurrency_group: str, optional
    """

    model_id: str = Field(description="The unique identifier of the model.")
    name: Optional[str] = Field(default=None, description="The name of the model.")
    can_be_finetuned: Optional[bool] = Field(
        default=None, description="Whether the model can be finetuned."
    )
    can_do_text_to_speech: Optional[bool] = Field(
        default=None, description="Whether the model can do text-to-speech."
    )
    can_do_voice_conversion: Optional[bool] = Field(
        default=None, description="Whether the model can do voice conversion."
    )
    can_use_style: Optional[bool] = Field(
        default=None, description="Whether the model can use style."
    )
    can_use_speaker_boost: Optional[bool] = Field(
        default=None, description="Whether the model can use speaker boost."
    )
    serves_pro_voices: Optional[bool] = Field(
        default=None, description="Whether the model serves pro voices."
    )
    token_cost_factor: Optional[float] = Field(
        default=None, description="The cost factor for the model."
    )
    description: Optional[str] = Field(
        default=None, description="The description of the model."
    )
    requires_alpha_access: Optional[bool] = Field(
        default=None, description="Whether the model requires alpha access."
    )
    max_characters_request_free_user: Optional[int] = Field(
        default=None,
        description="The maximum number of characters that can be requested by a free user.",
    )
    max_characters_request_subscribed_user: Optional[int] = Field(
        default=None,
        description="The maximum number of characters that can be requested by a subscribed user.",
    )
    maximum_text_length_per_request: Optional[int] = Field(
        default=None,
        description="The maximum length of text that can be requested for this model.",
    )
    languages: Optional[List[LanguageResponse]] = Field(
        default=None, description="The languages supported by the model."
    )
    model_rates: Optional[ModelRatesResponseModel] = Field(default=None)
    concurrency_group: Optional[str] = Field(
        default=None, description="The concurrency group for the model."
    )
