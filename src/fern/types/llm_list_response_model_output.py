from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .llm_info_model_output import LlmInfoModelOutput
from .llm_deprecation_config_model import LlmDeprecationConfigModel


class LlmListResponseModelOutput(BaseModel):
    """LlmListResponseModelOutput

    :param llms: List of all available LLM models that can be used with agents.
    :type llms: List[LlmInfoModelOutput]
    :param default_deprecation_config: default_deprecation_config
    :type default_deprecation_config: LlmDeprecationConfigModel
    """

    llms: List[LlmInfoModelOutput] = Field(
        description="List of all available LLM models that can be used with agents."
    )
    default_deprecation_config: LlmDeprecationConfigModel
