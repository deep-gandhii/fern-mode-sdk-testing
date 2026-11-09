from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AudioNativeCreateProjectResponseModel(BaseModel):
    """AudioNativeCreateProjectResponseModel

    :param project_id: The ID of the created Audio Native project.
    :type project_id: str
    :param converting: Whether the project is currently being converted.
    :type converting: bool
    :param html_snippet: The HTML snippet to embed the Audio Native player.
    :type html_snippet: str
    """

    project_id: str = Field(description="The ID of the created Audio Native project.")
    converting: bool = Field(
        description="Whether the project is currently being converted."
    )
    html_snippet: str = Field(
        description="The HTML snippet to embed the Audio Native player."
    )
