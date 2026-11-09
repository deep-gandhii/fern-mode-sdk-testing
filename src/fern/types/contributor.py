from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class Contributor(BaseModel):
    """Contributor

    :param name: name
    :type name: str
    :param role: role
    :type role: str
    :param bio: bio, defaults to None
    :type bio: str, optional
    :param profile_id: profile_id, defaults to None
    :type profile_id: str, optional
    """

    name: str
    role: str
    bio: Optional[str] = Field(default=None)
    profile_id: Optional[str] = Field(default=None)
