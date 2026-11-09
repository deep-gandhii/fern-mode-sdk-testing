from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_history_transcript_response_model import (
    ConversationHistoryTranscriptResponseModel,
)
from .conversation_history_analysis_common_model import (
    ConversationHistoryAnalysisCommonModel,
)


class AgentSimulatedChatTestResponseModel(BaseModel):
    """AgentSimulatedChatTestResponseModel

    :param simulated_conversation: simulated_conversation
    :type simulated_conversation: List[ConversationHistoryTranscriptResponseModel]
    :param analysis: analysis
    :type analysis: ConversationHistoryAnalysisCommonModel
    """

    simulated_conversation: List[ConversationHistoryTranscriptResponseModel]
    analysis: ConversationHistoryAnalysisCommonModel
