from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .default_sharing_group_config import DefaultSharingGroupConfig


class BodyCreateServiceAccountV1ServiceAccountsPost(BaseModel):
    """BodyCreateServiceAccountV1ServiceAccountsPost

    :param name: name
    :type name: str
    :param default_sharing_groups: List of groups with their permission levels to share with by default. Each entry should specify a group_id and a permission_level (admin, editor, or viewer)., defaults to None
    :type default_sharing_groups: List[DefaultSharingGroupConfig], optional
    """

    name: str
    default_sharing_groups: Optional[List[DefaultSharingGroupConfig]] = Field(
        default=None,
        description="List of groups with their permission levels to share with by default. Each entry should specify a group_id and a permission_level (admin, editor, or viewer).",
    )
