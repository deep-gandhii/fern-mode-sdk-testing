from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

SubmitBusinessInfoParamsSmbToolType = typing.Union[
    typing.Literal["submit_business_info"], typing.Any
]


class SubmitBusinessInfoParams(BaseModel):
    """Finalize the onboarding interview: create a text knowledge source and mark done.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: SubmitBusinessInfoParamsSmbToolType, optional
    """

    smb_tool_type: Optional[SubmitBusinessInfoParamsSmbToolType] = Field(default=None)
