from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel

# Union type for ValidationErrorLocItem
# Pydantic will attempt to validate against each type in order
ValidationErrorLocItem = Union[str, int]
# TypeAdapter for runtime validation of ValidationErrorLocItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ValidationErrorLocItem_adapter = TypeAdapter(ValidationErrorLocItem)


class ValidationError(BaseModel):
    """ValidationError

    :param loc: loc
    :type loc: List[ValidationErrorLocItem]
    :param msg: msg
    :type msg: str
    :param type: type
    :type type: str
    """

    loc: List[ValidationErrorLocItem]
    msg: str
    type: str
