from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .deliverable_info import DeliverableInfo


class OrderDeliverablesResponse(BaseModel):
    """OrderDeliverablesResponse

    :param deliverables: The list of delivered files for the order. Empty if the order is not yet completed.
    :type deliverables: List[DeliverableInfo]
    """

    deliverables: List[DeliverableInfo] = Field(
        description="The list of delivered files for the order. Empty if the order is not yet completed."
    )
