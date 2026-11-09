from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyDeleteExistingInvitationV1WorkspaceInvitesDelete(BaseModel):
    """BodyDeleteExistingInvitationV1WorkspaceInvitesDelete

    :param email: The email of the customer
    :type email: str
    """

    email: str = Field(description="The email of the customer")
