from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AutoGenerationMetadata(BaseModel):
    """Metadata for an automatically generated simulation test. Tracks the origin and context of tests that were auto-generated from conversations, including the source conversation, topic, and evaluation criteria the test covers.

    :param agent_id: Agent whose simulation library this test belongs to.
    :type agent_id: str
    :param stable_topic_id: Stable topic id (from topic discovery) this test covers.
    :type stable_topic_id: str
    :param criteria_id: Evaluation criterion id this test targets.
    :type criteria_id: str
    :param topic_label: Human-readable topic label at generation time.
    :type topic_label: str
    :param source_conversation_id: Conversation the test was generated from.
    :type source_conversation_id: str
    :param generated_at_unix: Unix timestamp (seconds) when the test was generated.
    :type generated_at_unix: int
    """

    agent_id: str = Field(
        description="Agent whose simulation library this test belongs to."
    )
    stable_topic_id: str = Field(
        description="Stable topic id (from topic discovery) this test covers."
    )
    criteria_id: str = Field(description="Evaluation criterion id this test targets.")
    topic_label: str = Field(
        description="Human-readable topic label at generation time."
    )
    source_conversation_id: str = Field(
        description="Conversation the test was generated from."
    )
    generated_at_unix: int = Field(
        description="Unix timestamp (seconds) when the test was generated."
    )
