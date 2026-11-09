from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel


class AgentDeploymentResponse(BaseModel):
    """AgentDeploymentResponse

    :param traffic_percentage_branch_id_map: Map of branch IDs to traffic percentages, defaults to None
    :type traffic_percentage_branch_id_map: Dict[str, float], optional
    """

    traffic_percentage_branch_id_map: Optional[Dict[str, float]] = Field(
        default=None, description="Map of branch IDs to traffic percentages"
    )
