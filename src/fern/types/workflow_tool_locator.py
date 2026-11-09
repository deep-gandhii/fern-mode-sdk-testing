from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class WorkflowToolLocator(BaseModel):
    """WorkflowToolLocator

    :param tool_id: tool_id
    :type tool_id: str
    """

    tool_id: str
