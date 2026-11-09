from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ProcedureValidationError(BaseModel):
    """ProcedureValidationError

    :param path: JSON path to the error, e.g. 'trigger', 'steps[0].instruction'
    :type path: str
    :param message: Human-readable error message
    :type message: str
    """

    path: str = Field(
        description="JSON path to the error, e.g. 'trigger', 'steps[0].instruction'"
    )
    message: str = Field(description="Human-readable error message")
