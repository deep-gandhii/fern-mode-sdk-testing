from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from typing import List
from .utils.base_error import BaseError
from .utils.base_model import BaseModel
from .procedure_validation_error import ProcedureValidationError


# Pydantic validation model for CompileProceduresValidationErrorResponseModel
class CompileProceduresValidationErrorResponseModelData(BaseModel):
    """CompileProceduresValidationErrorResponseModel

    :param errors: Validation errors keyed by procedure ID.
    :type errors: Dict[str, List[ProcedureValidationError]]
    """

    errors: Dict[str, List[ProcedureValidationError]] = Field(
        description="Validation errors keyed by procedure ID."
    )


# Error exception class
class CompileProceduresValidationErrorResponseModel(BaseError):
    """CompileProceduresValidationErrorResponseModel

    :param errors: Validation errors keyed by procedure ID.
    :type errors: Dict[str, List[ProcedureValidationError]]
    """

    _model_class = CompileProceduresValidationErrorResponseModelData
