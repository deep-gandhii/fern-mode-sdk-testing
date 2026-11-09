from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .agent_topic_response_model import AgentTopicResponseModel


class GetAgentTopicsResponseModel(BaseModel):
    """GetAgentTopicsResponseModel

    :param topics: topics
    :type topics: List[AgentTopicResponseModel]
    :param window_start_unix_secs: window_start_unix_secs
    :type window_start_unix_secs: int
    :param window_end_unix_secs: window_end_unix_secs
    :type window_end_unix_secs: int
    """

    topics: List[AgentTopicResponseModel]
    window_start_unix_secs: int
    window_end_unix_secs: int
