from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

SfxSourceContextSourceType = typing.Union[typing.Literal["sfx"], typing.Any]


class SfxSourceContext(BaseModel):
    """Context for sound effect clips.

    :param source_type: source_type, defaults to None
    :type source_type: SfxSourceContextSourceType, optional
    :param sound_generation_history_item_id: sound_generation_history_item_id, defaults to None
    :type sound_generation_history_item_id: str, optional
    :param text: text, defaults to None
    :type text: str, optional
    :param generation_config: generation_config, defaults to None
    :type generation_config: Dict[str, Any], optional
    """

    source_type: Optional[SfxSourceContextSourceType] = Field(default=None)
    sound_generation_history_item_id: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    generation_config: Optional[Dict[str, Any]] = Field(default=None)
