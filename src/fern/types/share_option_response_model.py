from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ShareOptionResponseModelType = typing.Union[
    typing.Literal["user", "group", "key"], typing.Any
]


class ShareOptionResponseModel(BaseModel):
    """ShareOptionResponseModel

    :param name: The name of the principal.
    :type name: str
    :param id: The ID of the principal.
    :type id: str
    :param type: The type of the principal: user, group, or service account (under 'key').
    :type type: ShareOptionResponseModelType
    """

    name: str = Field(description="The name of the principal.")
    id: str = Field(description="The ID of the principal.")
    type: ShareOptionResponseModelType = Field(
        description="The type of the principal: user, group, or service account (under 'key')."
    )
