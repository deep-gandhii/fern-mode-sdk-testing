from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConvAiSecretLocator(BaseModel):
    """Used to reference a secret from the agent's secret store.

    :param secret_id: secret_id
    :type secret_id: str
    """

    secret_id: str
