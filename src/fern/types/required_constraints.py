from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .required_constraint import RequiredConstraint


class RequiredConstraints(BaseModel):
    """Wrapper for anyOf/allOf composition constraints scoped to required fields.

    :param any_of: any_of, defaults to None
    :type any_of: List[RequiredConstraint], optional
    :param all_of: all_of, defaults to None
    :type all_of: List[RequiredConstraint], optional
    """

    any_of: Optional[List[RequiredConstraint]] = Field(default=None)
    all_of: Optional[List[RequiredConstraint]] = Field(default=None)
