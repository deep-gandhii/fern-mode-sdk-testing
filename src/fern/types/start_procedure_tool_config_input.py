from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .procedure_at_version_input import ProcedureAtVersionInput

StartProcedureToolConfigInputSystemToolType = typing.Union[
    typing.Literal["start_procedure"], typing.Any
]


class StartProcedureToolConfigInput(BaseModel):
    """StartProcedureToolConfigInput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: StartProcedureToolConfigInputSystemToolType, optional
    :param procedures: procedures, defaults to None
    :type procedures: Dict[str, ProcedureAtVersionInput], optional
    """

    system_tool_type: Optional[StartProcedureToolConfigInputSystemToolType] = Field(
        default=None
    )
    procedures: Optional[Dict[str, ProcedureAtVersionInput]] = Field(default=None)
