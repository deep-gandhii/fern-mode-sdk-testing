from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SingleTestRunRequestModel(BaseModel):
    """SingleTestRunRequestModel

    :param test_id: ID of the test to run
    :type test_id: str
    :param workflow_node_id: ID of the workflow node to run the test on. If not provided, the test will be run on the agent's default workflow node., defaults to None
    :type workflow_node_id: str, optional
    :param root_folder_id: ID of the root folder to run the test on. If not provided, the test will be run on the agent's default folder., defaults to None
    :type root_folder_id: str, optional
    :param root_folder_name: Name of the root folder to run the test on. If not provided, the test will be run on the agent's default folder., defaults to None
    :type root_folder_name: str, optional
    """

    test_id: str = Field(description="ID of the test to run")
    workflow_node_id: Optional[str] = Field(
        default=None,
        description="ID of the workflow node to run the test on. If not provided, the test will be run on the agent's default workflow node.",
    )
    root_folder_id: Optional[str] = Field(
        default=None,
        description="ID of the root folder to run the test on. If not provided, the test will be run on the agent's default folder.",
    )
    root_folder_name: Optional[str] = Field(
        default=None,
        description="Name of the root folder to run the test on. If not provided, the test will be run on the agent's default folder.",
    )
