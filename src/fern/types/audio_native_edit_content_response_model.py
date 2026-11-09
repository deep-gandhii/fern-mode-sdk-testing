from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AudioNativeEditContentResponseModel(BaseModel):
    """AudioNativeEditContentResponseModel

    :param project_id: The ID of the project.
    :type project_id: str
    :param converting: Whether the project is currently being converted.
    :type converting: bool
    :param publishing: Whether the project is currently being published.
    :type publishing: bool
    :param html_snippet: The HTML snippet to embed the Audio Native player.
    :type html_snippet: str
    """

    project_id: str = Field(description="The ID of the project.")
    converting: bool = Field(
        description="Whether the project is currently being converted."
    )
    publishing: bool = Field(
        description="Whether the project is currently being published."
    )
    html_snippet: str = Field(
        description="The HTML snippet to embed the Audio Native player."
    )
