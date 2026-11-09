from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ReaderResourceResponseModelResourceType = typing.Union[
    typing.Literal["read", "collection"], typing.Any
]


class ReaderResourceResponseModel(BaseModel):
    """ReaderResourceResponseModel

    :param resource_type: The type of resource.
    :type resource_type: ReaderResourceResponseModelResourceType
    :param resource_id: The ID of the resource.
    :type resource_id: str
    """

    resource_type: ReaderResourceResponseModelResourceType = Field(
        description="The type of resource."
    )
    resource_id: str = Field(description="The ID of the resource.")
