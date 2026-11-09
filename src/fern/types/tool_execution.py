from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

ToolExecutionTaskSupport = typing.Union[
    typing.Literal["forbidden", "optional", "required"], typing.Any
]


class ToolExecution(BaseModel):
    """Execution-related properties for a tool.

    :param task_support: task_support, defaults to None
    :type task_support: ToolExecutionTaskSupport, optional
    """

    task_support: Optional[ToolExecutionTaskSupport] = Field(
        alias="taskSupport", serialization_alias="taskSupport", default=None
    )

    def model_dump_original(self, **kwargs):
        result = super().model_dump_original(**kwargs)
        extra_fields = self.model_extra or {}
        return {**extra_fields, **result}
