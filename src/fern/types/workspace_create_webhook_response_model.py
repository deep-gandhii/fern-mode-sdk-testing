from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class WorkspaceCreateWebhookResponseModel(BaseModel):
    """WorkspaceCreateWebhookResponseModel

    :param webhook_id: webhook_id
    :type webhook_id: str
    :param webhook_secret: webhook_secret, defaults to None
    :type webhook_secret: str, optional
    """

    webhook_id: str
    webhook_secret: Optional[str] = Field(default=None)
