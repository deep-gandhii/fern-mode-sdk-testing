from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .project_response import ProjectResponse


class PodcastProjectResponseModel(BaseModel):
    """PodcastProjectResponseModel

    :param project: project
    :type project: ProjectResponse
    """

    project: ProjectResponse
