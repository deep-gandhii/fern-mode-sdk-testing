from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .procedure_at_version_input import ProcedureAtVersionInput

EndProcedureToolConfigInputSystemToolType = typing.Union[
    typing.Literal["end_procedure"], typing.Any
]


class EndProcedureToolConfigInput(BaseModel):
    """EndProcedureToolConfigInput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: EndProcedureToolConfigInputSystemToolType, optional
    :param procedures: procedures, defaults to None
    :type procedures: Dict[str, ProcedureAtVersionInput], optional
    """

    system_tool_type: Optional[EndProcedureToolConfigInputSystemToolType] = Field(
        default=None
    )
    procedures: Optional[Dict[str, ProcedureAtVersionInput]] = Field(default=None)
