from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AttachedTestModel(BaseModel):
    """AttachedTestModel

    :param test_id: test_id
    :type test_id: str
    :param workflow_node_id: workflow_node_id, defaults to None
    :type workflow_node_id: str, optional
    """

    test_id: str
    workflow_node_id: Optional[str] = Field(default=None)
