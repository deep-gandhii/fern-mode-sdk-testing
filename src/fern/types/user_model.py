from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .user_type_id import UserTypeId


class UserModel(BaseModel):
    """OCSF User object. Spec: https://schema.ocsf.io/1.6.0/objects/user

    :param name: Username, defaults to None
    :type name: str, optional
    :param uid: Unique user identifier, defaults to None
    :type uid: str, optional
    :param type_id: OCSF User type IDs. Spec: https://schema.ocsf.io/1.6.0/objects/user, defaults to None
    :type type_id: UserTypeId, optional
    :param type: Account type description, defaults to None
    :type type: str, optional
    :param email_addr: User email address, defaults to None
    :type email_addr: str, optional
    :param full_name: Full name of the user, defaults to None
    :type full_name: str, optional
    :param domain: User's domain, defaults to None
    :type domain: str, optional
    """

    name: Optional[str] = Field(default=None, description="Username")
    uid: Optional[str] = Field(default=None, description="Unique user identifier")
    type_id: Optional[UserTypeId] = Field(
        default=None,
        description="OCSF User type IDs. Spec: https://schema.ocsf.io/1.6.0/objects/user",
    )
    type: Optional[str] = Field(default=None, description="Account type description")
    email_addr: Optional[str] = Field(default=None, description="User email address")
    full_name: Optional[str] = Field(default=None, description="Full name of the user")
    domain: Optional[str] = Field(default=None, description="User's domain")
