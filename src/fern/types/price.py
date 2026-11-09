from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .currency import Currency


class Price(BaseModel):
    """Currency/amount pair.

    :param amount: amount
    :type amount: str
    :param currency: currency
    :type currency: Currency
    """

    amount: str
    currency: Currency
