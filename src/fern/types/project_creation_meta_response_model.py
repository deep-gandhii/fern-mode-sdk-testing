from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .project_creation_meta_type import ProjectCreationMetaType

ProjectCreationMetaResponseModelStatus = typing.Union[
    typing.Literal["draft", "pending", "creating", "finished", "failed"], typing.Any
]


class ProjectCreationMetaResponseModel(BaseModel):
    """ProjectCreationMetaResponseModel

    :param creation_progress: The progress of the project creation.
    :type creation_progress: float
    :param status: The status of the project creation action.
    :type status: ProjectCreationMetaResponseModelStatus
    :param type: type
    :type type: ProjectCreationMetaType
    """

    creation_progress: float = Field(
        description="The progress of the project creation."
    )
    status: ProjectCreationMetaResponseModelStatus = Field(
        description="The status of the project creation action."
    )
    type: ProjectCreationMetaType
