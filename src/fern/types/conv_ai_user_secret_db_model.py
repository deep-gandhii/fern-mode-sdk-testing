from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConvAiUserSecretDbModel(BaseModel):
    """User-specific secret model that are not shared with other users in a workspace.

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param encrypted_value: encrypted_value
    :type encrypted_value: str
    :param nonce: nonce
    :type nonce: str
    """

    id: str
    name: str
    encrypted_value: str
    nonce: str
