from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AdditionalFormatResponseModel(BaseModel):
    """AdditionalFormatResponseModel

    :param requested_format: The requested format.
    :type requested_format: str
    :param file_extension: The file extension of the additional format.
    :type file_extension: str
    :param content_type: The content type of the additional format.
    :type content_type: str
    :param is_base_64_encoded: Whether the content is base64 encoded.
    :type is_base_64_encoded: bool
    :param content: The content of the additional format.
    :type content: str
    """

    requested_format: str = Field(description="The requested format.")
    file_extension: str = Field(
        description="The file extension of the additional format."
    )
    content_type: str = Field(description="The content type of the additional format.")
    is_base_64_encoded: bool = Field(
        alias="is_base64_encoded",
        serialization_alias="is_base64_encoded",
        description="Whether the content is base64 encoded.",
    )
    content: str = Field(description="The content of the additional format.")
