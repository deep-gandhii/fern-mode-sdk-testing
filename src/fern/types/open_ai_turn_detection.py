from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .turn_detection_type import TurnDetectionType
from .eagerness import Eagerness


class OpenAiTurnDetection(BaseModel):
    """OpenAiTurnDetection

    :param type: type, defaults to None
    :type type: TurnDetectionType, optional
    :param eagerness: eagerness, defaults to None
    :type eagerness: Eagerness, optional
    :param create_response: create_response, defaults to None
    :type create_response: bool, optional
    :param interrupt_response: interrupt_response, defaults to None
    :type interrupt_response: bool, optional
    :param threshold: threshold, defaults to None
    :type threshold: float, optional
    :param prefix_padding_ms: prefix_padding_ms, defaults to None
    :type prefix_padding_ms: int, optional
    :param silence_duration_ms: silence_duration_ms, defaults to None
    :type silence_duration_ms: int, optional
    """

    type: Optional[TurnDetectionType] = Field(default=None)
    eagerness: Optional[Eagerness] = Field(default=None)
    create_response: Optional[bool] = Field(default=None)
    interrupt_response: Optional[bool] = Field(default=None)
    threshold: Optional[float] = Field(default=None)
    prefix_padding_ms: Optional[int] = Field(default=None)
    silence_duration_ms: Optional[int] = Field(default=None)
