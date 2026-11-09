from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CreateProcedureResponseModel(BaseModel):
    """CreateProcedureResponseModel

    :param procedure_id: ID of the created procedure
    :type procedure_id: str
    """

    procedure_id: str = Field(description="ID of the created procedure")
