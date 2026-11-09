from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_simulation_specification import ConversationSimulationSpecification
from .prompt_evaluation_criteria import PromptEvaluationCriteria


class BodySimulatesAConversationStreamV1ConvaiAgentsAgentIdSimulateConversationStreamPost(
    BaseModel
):
    """BodySimulatesAConversationStreamV1ConvaiAgentsAgentIdSimulateConversationStreamPost

    :param simulation_specification: A specification that will be used to simulate a conversation between an agent and an AI user.
    :type simulation_specification: ConversationSimulationSpecification
    :param extra_evaluation_criteria: A list of evaluation criteria to test, defaults to None
    :type extra_evaluation_criteria: List[PromptEvaluationCriteria], optional
    :param new_turns_limit: Maximum number of new turns to generate in the conversation simulation, defaults to None
    :type new_turns_limit: int, optional
    """

    simulation_specification: ConversationSimulationSpecification = Field(
        description="A specification that will be used to simulate a conversation between an agent and an AI user."
    )
    extra_evaluation_criteria: Optional[List[PromptEvaluationCriteria]] = Field(
        default=None, description="A list of evaluation criteria to test"
    )
    new_turns_limit: Optional[int] = Field(
        default=None,
        description="Maximum number of new turns to generate in the conversation simulation",
    )
