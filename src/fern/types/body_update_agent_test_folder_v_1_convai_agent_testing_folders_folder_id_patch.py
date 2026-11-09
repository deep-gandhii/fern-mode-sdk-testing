from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyUpdateAgentTestFolderV1ConvaiAgentTestingFoldersFolderIdPatch(BaseModel):
    """BodyUpdateAgentTestFolderV1ConvaiAgentTestingFoldersFolderIdPatch

    :param name: The new name for the folder
    :type name: str
    """

    name: str = Field(description="The new name for the folder")
