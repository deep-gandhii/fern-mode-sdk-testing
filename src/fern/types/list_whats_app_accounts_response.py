from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .get_whats_app_account_response import GetWhatsAppAccountResponse


class ListWhatsAppAccountsResponse(BaseModel):
    """ListWhatsAppAccountsResponse

    :param items: items
    :type items: List[GetWhatsAppAccountResponse]
    """

    items: List[GetWhatsAppAccountResponse]
