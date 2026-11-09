from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .procedure_type import ProcedureType


class CreateProcedureRequestModel(BaseModel):
    """CreateProcedureRequestModel

    :param name: Procedure name, defaults to None
    :type name: str, optional
    :param content: Initial procedure content, defaults to None
    :type content: str, optional
    :param type: type, defaults to None
    :type type: ProcedureType, optional
    :param trigger: When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it. If omitted or null, the trigger is derived from the content instead. Also accepts `description` as an alias., defaults to None
    :type trigger: str, optional
    """

    name: Optional[str] = Field(default=None, description="Procedure name")
    content: Optional[str] = Field(
        default=None, description="Initial procedure content"
    )
    type: Optional[ProcedureType] = Field(default=None)
    trigger: Optional[str] = Field(
        default=None,
        description="When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it. If omitted or null, the trigger is derived from the content instead. Also accepts `description` as an alias.",
    )
