from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ReadLegalTerms(BaseModel):
    """ReadLegalTerms

    :param terms: terms, defaults to None
    :type terms: str, optional
    :param start_date: start_date, defaults to None
    :type start_date: str, optional
    :param end_date: end_date, defaults to None
    :type end_date: str, optional
    """

    terms: Optional[str] = Field(default=None)
    start_date: Optional[str] = Field(default=None)
    end_date: Optional[str] = Field(default=None)
