from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .user_model import UserModel


class ActorModel(BaseModel):
    """OCSF Actor object - describes the entity that performed the action. Spec: https://schema.ocsf.io/1.6.0/objects/actor

    :param user: OCSF User object. Spec: https://schema.ocsf.io/1.6.0/objects/user
    :type user: UserModel
    :param app_name: Client application or service name, defaults to None
    :type app_name: str, optional
    :param app_uid: Client application unique identifier, defaults to None
    :type app_uid: str, optional
    :param session: Session information, defaults to None
    :type session: Dict[str, Any], optional
    """

    user: UserModel = Field(
        description="OCSF User object. Spec: https://schema.ocsf.io/1.6.0/objects/user"
    )
    app_name: Optional[str] = Field(
        default=None, description="Client application or service name"
    )
    app_uid: Optional[str] = Field(
        default=None, description="Client application unique identifier"
    )
    session: Optional[Dict[str, Any]] = Field(
        default=None, description="Session information"
    )
