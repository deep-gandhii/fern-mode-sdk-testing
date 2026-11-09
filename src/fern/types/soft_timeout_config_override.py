from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SoftTimeoutConfigOverride(BaseModel):
    """SoftTimeoutConfigOverride

    :param message: Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., {{system__time}}, {{custom_variable}})., defaults to None
    :type message: str, optional
    """

    message: Optional[str] = Field(
        default=None,
        description="Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., {{system__time}}, {{custom_variable}}).",
    )
