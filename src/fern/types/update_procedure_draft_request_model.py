from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .procedure_type import ProcedureType


class UpdateProcedureDraftRequestModel(BaseModel):
    """UpdateProcedureDraftRequestModel

    :param name: Procedure name
    :type name: str
    :param content: Procedure content
    :type content: str
    :param type: type
    :type type: ProcedureType
    :param trigger: When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it. If omitted or null, the trigger is derived from the content instead. Also accepts `description` as an alias., defaults to None
    :type trigger: str, optional
    """

    name: str = Field(description="Procedure name")
    content: str = Field(description="Procedure content")
    type: ProcedureType
    trigger: Optional[str] = Field(
        default=None,
        description="When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it. If omitted or null, the trigger is derived from the content instead. Also accepts `description` as an alias.",
    )
