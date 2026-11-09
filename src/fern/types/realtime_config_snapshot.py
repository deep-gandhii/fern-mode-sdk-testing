from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .realtime_config_snapshot_parents import RealtimeConfigSnapshotParents
from .open_ai_session_config import OpenAiSessionConfig
from .safety_common_model_output import SafetyCommonModelOutput


class RealtimeConfigSnapshot(BaseModel):
    """RealtimeConfigSnapshot

    :param id: id
    :type id: str
    :param workspace_id: workspace_id
    :type workspace_id: str
    :param conversation_id: conversation_id
    :type conversation_id: str
    :param seq_no: seq_no
    :type seq_no: int
    :param time_in_call_secs: time_in_call_secs
    :type time_in_call_secs: int
    :param time_committed_secs: time_committed_secs
    :type time_committed_secs: int
    :param source_event_id: source_event_id, defaults to None
    :type source_event_id: int, optional
    :param parents: parents
    :type parents: RealtimeConfigSnapshotParents
    :param session_config: session_config
    :type session_config: OpenAiSessionConfig
    :param safety: Safety object that has the information of safety evaluations based on used voice.
    :type safety: SafetyCommonModelOutput
    :param changed_paths: changed_paths, defaults to None
    :type changed_paths: List[str], optional
    """

    id: str = Field(alias="_id", serialization_alias="_id")
    workspace_id: str
    conversation_id: str
    seq_no: int
    time_in_call_secs: int
    time_committed_secs: int
    source_event_id: Optional[int] = Field(default=None)
    parents: RealtimeConfigSnapshotParents
    session_config: OpenAiSessionConfig
    safety: SafetyCommonModelOutput = Field(
        description="Safety object that has the information of safety evaluations based on used voice."
    )
    changed_paths: Optional[List[str]] = Field(default=None)
