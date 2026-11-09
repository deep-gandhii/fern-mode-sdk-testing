from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .widget_config_response import WidgetConfigResponse


class GetAgentEmbedResponseModel(BaseModel):
    """GetAgentEmbedResponseModel

    :param agent_id: agent_id
    :type agent_id: str
    :param widget_config: widget_config
    :type widget_config: WidgetConfigResponse
    """

    agent_id: str
    widget_config: WidgetConfigResponse
