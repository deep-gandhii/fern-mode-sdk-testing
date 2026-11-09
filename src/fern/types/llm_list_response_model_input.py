from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .llm_info_model_input import LlmInfoModelInput
from .llm_deprecation_config_model import LlmDeprecationConfigModel


class LlmListResponseModelInput(BaseModel):
    """LlmListResponseModelInput

    :param llms: List of all available LLM models that can be used with agents.
    :type llms: List[LlmInfoModelInput]
    :param default_deprecation_config: default_deprecation_config
    :type default_deprecation_config: LlmDeprecationConfigModel
    """

    llms: List[LlmInfoModelInput] = Field(
        description="List of all available LLM models that can be used with agents."
    )
    default_deprecation_config: LlmDeprecationConfigModel
