from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .procedure_at_version_output import ProcedureAtVersionOutput

EndProcedureToolConfigOutputSystemToolType = typing.Union[
    typing.Literal["end_procedure"], typing.Any
]


class EndProcedureToolConfigOutput(BaseModel):
    """EndProcedureToolConfigOutput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: EndProcedureToolConfigOutputSystemToolType, optional
    :param procedures: procedures, defaults to None
    :type procedures: Dict[str, ProcedureAtVersionOutput], optional
    """

    system_tool_type: Optional[EndProcedureToolConfigOutputSystemToolType] = Field(
        default=None
    )
    procedures: Optional[Dict[str, ProcedureAtVersionOutput]] = Field(default=None)
