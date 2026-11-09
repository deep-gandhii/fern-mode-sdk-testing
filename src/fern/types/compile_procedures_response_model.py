from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .agent_workflow_response_model import AgentWorkflowResponseModel


class CompileProceduresResponseModel(BaseModel):
    """CompileProceduresResponseModel

    :param workflow: workflow
    :type workflow: AgentWorkflowResponseModel
    """

    workflow: AgentWorkflowResponseModel
