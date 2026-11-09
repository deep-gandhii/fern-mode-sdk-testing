from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel
from .studio_agent_tool_settings_model import StudioAgentToolSettingsModel


class StudioAgentSettingsModel(BaseModel):
    """StudioAgentSettingsModel

    :param tool_settings: tool_settings, defaults to None
    :type tool_settings: Dict[str, StudioAgentToolSettingsModel], optional
    """

    tool_settings: Optional[Dict[str, StudioAgentToolSettingsModel]] = Field(
        default=None
    )
