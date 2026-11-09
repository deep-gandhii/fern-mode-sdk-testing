from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .procedure_type import ProcedureType


class ProcedureDraftResponseModel(BaseModel):
    """ProcedureDraftResponseModel

    :param procedure_id: Procedure ID
    :type procedure_id: str
    :param name: Procedure name
    :type name: str
    :param content: Procedure content
    :type content: str
    :param type: type, defaults to None
    :type type: ProcedureType, optional
    :param trigger: When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it., defaults to None
    :type trigger: str, optional
    """

    procedure_id: str = Field(description="Procedure ID")
    name: str = Field(description="Procedure name")
    content: str = Field(description="Procedure content")
    type: Optional[ProcedureType] = Field(default=None)
    trigger: Optional[str] = Field(
        default=None,
        description="When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it.",
    )
