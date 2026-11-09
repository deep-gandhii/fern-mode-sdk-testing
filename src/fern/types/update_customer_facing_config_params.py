from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateCustomerFacingConfigParamsSmbToolType = typing.Union[
    typing.Literal["update_customer_facing_config"], typing.Any
]


class UpdateCustomerFacingConfigParams(BaseModel):
    """UpdateCustomerFacingConfigParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateCustomerFacingConfigParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateCustomerFacingConfigParamsSmbToolType] = Field(
        default=None
    )
