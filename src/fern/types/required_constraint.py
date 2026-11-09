from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RequiredConstraint(BaseModel):
    """A set of fields that must all be present to satisfy this constraint.

    :param required: required
    :type required: List[str]
    """

    required: List[str]
