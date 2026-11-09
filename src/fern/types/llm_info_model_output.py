from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .llm import Llm
from .llm_reasoning_effort import LlmReasoningEffort
from .llm_deprecation_info_model import LlmDeprecationInfoModel
from .regional_processing_surcharge_info import RegionalProcessingSurchargeInfo


class LlmInfoModelOutput(BaseModel):
    """LlmInfoModelOutput

    :param llm: llm
    :type llm: Llm
    :param is_checkpoint: Whether this is a pinned checkpoint version of a model rather than a top-level alias.
    :type is_checkpoint: bool
    :param max_tokens_limit: Maximum number of output tokens the model can generate.
    :type max_tokens_limit: int
    :param max_context_limit: Maximum number of input context tokens the model supports.
    :type max_context_limit: int
    :param supports_image_input: Whether the model supports image file inputs during conversations.
    :type supports_image_input: bool
    :param supports_document_input: Whether the model supports document (PDF) file inputs during conversations.
    :type supports_document_input: bool
    :param supports_parallel_tool_calls: Whether the model supports calling multiple tools in parallel.
    :type supports_parallel_tool_calls: bool
    :param available_reasoning_efforts: Available reasoning effort levels for this model. Null if the model does not support configurable reasoning., defaults to None
    :type available_reasoning_efforts: List[LlmReasoningEffort], optional
    :param deprecation_info: Deprecation information if this model is deprecated or scheduled for deprecation. Null if the model is not affected., defaults to None
    :type deprecation_info: LlmDeprecationInfoModel, optional
    :param regional_processing_surcharge: Regional processing surcharge details if this model has additional costs in the current deployment region. Null if no surcharge applies., defaults to None
    :type regional_processing_surcharge: RegionalProcessingSurchargeInfo, optional
    """

    llm: Llm
    is_checkpoint: bool = Field(
        description="Whether this is a pinned checkpoint version of a model rather than a top-level alias."
    )
    max_tokens_limit: int = Field(
        description="Maximum number of output tokens the model can generate."
    )
    max_context_limit: int = Field(
        description="Maximum number of input context tokens the model supports."
    )
    supports_image_input: bool = Field(
        description="Whether the model supports image file inputs during conversations."
    )
    supports_document_input: bool = Field(
        description="Whether the model supports document (PDF) file inputs during conversations."
    )
    supports_parallel_tool_calls: bool = Field(
        description="Whether the model supports calling multiple tools in parallel."
    )
    available_reasoning_efforts: Optional[List[LlmReasoningEffort]] = Field(
        default=None,
        description="Available reasoning effort levels for this model. Null if the model does not support configurable reasoning.",
    )
    deprecation_info: Optional[LlmDeprecationInfoModel] = Field(
        default=None,
        description="Deprecation information if this model is deprecated or scheduled for deprecation. Null if the model is not affected.",
    )
    regional_processing_surcharge: Optional[RegionalProcessingSurchargeInfo] = Field(
        default=None,
        description="Regional processing surcharge details if this model has additional costs in the current deployment region. Null if no surcharge applies.",
    )
