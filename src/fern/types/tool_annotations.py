from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ToolAnnotations(BaseModel):
    """Additional properties describing a Tool to clients. NOTE: all properties in ToolAnnotations are **hints**. They are not guaranteed to provide a faithful description of tool behavior (including descriptive properties like `title`). Clients should never make tool use decisions based on ToolAnnotations received from untrusted servers.

    :param title: title, defaults to None
    :type title: str, optional
    :param read_only_hint: read_only_hint, defaults to None
    :type read_only_hint: bool, optional
    :param destructive_hint: destructive_hint, defaults to None
    :type destructive_hint: bool, optional
    :param idempotent_hint: idempotent_hint, defaults to None
    :type idempotent_hint: bool, optional
    :param open_world_hint: open_world_hint, defaults to None
    :type open_world_hint: bool, optional
    """

    title: Optional[str] = Field(default=None)
    read_only_hint: Optional[bool] = Field(
        alias="readOnlyHint", serialization_alias="readOnlyHint", default=None
    )
    destructive_hint: Optional[bool] = Field(
        alias="destructiveHint", serialization_alias="destructiveHint", default=None
    )
    idempotent_hint: Optional[bool] = Field(
        alias="idempotentHint", serialization_alias="idempotentHint", default=None
    )
    open_world_hint: Optional[bool] = Field(
        alias="openWorldHint", serialization_alias="openWorldHint", default=None
    )

    def model_dump_original(self, **kwargs):
        result = super().model_dump_original(**kwargs)
        extra_fields = self.model_extra or {}
        return {**extra_fields, **result}
