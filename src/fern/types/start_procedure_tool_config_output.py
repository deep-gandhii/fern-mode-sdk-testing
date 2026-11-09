from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .procedure_at_version_output import ProcedureAtVersionOutput

StartProcedureToolConfigOutputSystemToolType = typing.Union[
    typing.Literal["start_procedure"], typing.Any
]


class StartProcedureToolConfigOutput(BaseModel):
    """StartProcedureToolConfigOutput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: StartProcedureToolConfigOutputSystemToolType, optional
    :param procedures: procedures, defaults to None
    :type procedures: Dict[str, ProcedureAtVersionOutput], optional
    """

    system_tool_type: Optional[StartProcedureToolConfigOutputSystemToolType] = Field(
        default=None
    )
    procedures: Optional[Dict[str, ProcedureAtVersionOutput]] = Field(default=None)
