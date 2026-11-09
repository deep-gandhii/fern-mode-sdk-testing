from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DoDubbingResponse(BaseModel):
    """DoDubbingResponse

    :param dubbing_id: The ID of the dubbing project.
    :type dubbing_id: str
    :param expected_duration_sec: The expected duration of the dubbing project in seconds.
    :type expected_duration_sec: float
    """

    dubbing_id: str = Field(description="The ID of the dubbing project.")
    expected_duration_sec: float = Field(
        description="The expected duration of the dubbing project in seconds."
    )
