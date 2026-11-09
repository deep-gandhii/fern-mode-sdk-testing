from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .project_response import ProjectResponse


class GetProjectsResponse(BaseModel):
    """GetProjectsResponse

    :param projects: A list of projects with their metadata.
    :type projects: List[ProjectResponse]
    """

    projects: List[ProjectResponse] = Field(
        description="A list of projects with their metadata."
    )
