from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .procedure_list_item_response_model import ProcedureListItemResponseModel


class ListProceduresResponseModel(BaseModel):
    """ListProceduresResponseModel

    :param procedures: Procedures on the branch with their draft-aware metadata.
    :type procedures: List[ProcedureListItemResponseModel]
    """

    procedures: List[ProcedureListItemResponseModel] = Field(
        description="Procedures on the branch with their draft-aware metadata."
    )
