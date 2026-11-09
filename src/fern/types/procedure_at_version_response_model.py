from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .procedure_type import ProcedureType


class ProcedureAtVersionResponseModel(BaseModel):
    """ProcedureAtVersionResponseModel

    :param procedure_id: Procedure ID
    :type procedure_id: str
    :param version_id: Version ID of a version of the procedure. None for a procedure never versioned., defaults to None
    :type version_id: str, optional
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
    version_id: Optional[str] = Field(
        default=None,
        description="Version ID of a version of the procedure. None for a procedure never versioned.",
    )
    name: str = Field(description="Procedure name")
    content: str = Field(description="Procedure content")
    type: Optional[ProcedureType] = Field(default=None)
    trigger: Optional[str] = Field(
        default=None,
        description="When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it.",
    )
