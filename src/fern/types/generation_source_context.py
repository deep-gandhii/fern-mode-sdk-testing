from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .reference_video import ReferenceVideo

GenerationSourceContextSourceType = typing.Union[
    typing.Literal["generation"], typing.Any
]


class GenerationSourceContext(BaseModel):
    """GenerationSourceContext

    :param source_type: source_type, defaults to None
    :type source_type: GenerationSourceContextSourceType, optional
    :param generation_id: generation_id
    :type generation_id: str
    :param prompt: prompt, defaults to None
    :type prompt: str, optional
    :param model_id: model_id
    :type model_id: str
    :param model_provider: model_provider, defaults to None
    :type model_provider: str, optional
    :param generation_session_id: generation_session_id, defaults to None
    :type generation_session_id: str, optional
    :param session_iteration_id: session_iteration_id, defaults to None
    :type session_iteration_id: str, optional
    :param model_parameters: model_parameters, defaults to None
    :type model_parameters: Dict[str, Any], optional
    :param extend_video: extend_video, defaults to None
    :type extend_video: ReferenceVideo, optional
    """

    source_type: Optional[GenerationSourceContextSourceType] = Field(default=None)
    generation_id: str
    prompt: Optional[str] = Field(default=None)
    model_id: str
    model_provider: Optional[str] = Field(default=None)
    generation_session_id: Optional[str] = Field(default=None)
    session_iteration_id: Optional[str] = Field(default=None)
    model_parameters: Optional[Dict[str, Any]] = Field(default=None)
    extend_video: Optional[ReferenceVideo] = Field(default=None)
