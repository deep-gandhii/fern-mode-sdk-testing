from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

WorkflowToolEdgeStepModelType = typing.Union[typing.Literal["edge"], typing.Any]


class WorkflowToolEdgeStepModel(BaseModel):
    """WorkflowToolEdgeStepModel

    :param step_latency_secs: step_latency_secs
    :type step_latency_secs: float
    :param type: type, defaults to None
    :type type: WorkflowToolEdgeStepModelType, optional
    :param edge_id: edge_id
    :type edge_id: str
    :param target_node_id: target_node_id
    :type target_node_id: str
    """

    step_latency_secs: float
    type: Optional[WorkflowToolEdgeStepModelType] = Field(default=None)
    edge_id: str
    target_node_id: str
