from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SoftTimeoutConfig(BaseModel):
    """Configuration for soft timeout functionality during LLM response generation.

    :param timeout_seconds: Time in seconds before showing the predefined message while waiting for LLM response. Set to -1 to disable., defaults to None
    :type timeout_seconds: float, optional
    :param message: Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., {{system__time}}, {{custom_variable}})., defaults to None
    :type message: str, optional
    :param additional_soft_timeout_messages: Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used., defaults to None
    :type additional_soft_timeout_messages: List[str], optional
    :param use_llm_generated_message: If enabled, the soft timeout message will be generated dynamically instead of using the static message., defaults to None
    :type use_llm_generated_message: bool, optional
    :param randomize_fillers: If enabled, shuffle the order of static soft timeout messages once at the start of each turn. Only applies when use_llm_generated_message is false., defaults to None
    :type randomize_fillers: bool, optional
    :param max_soft_timeouts_per_generation: Maximum filler messages while waiting for a single LLM response. Fires every timeout_seconds until the LLM streams content or this limit is reached., defaults to None
    :type max_soft_timeouts_per_generation: int, optional
    :param llm_generated_message_prompt_override: Custom prompt for generating the soft timeout filler message when use_llm_generated_message is enabled. Recent conversation context is provided as a separate user message. If not set, the default prompt will be used. Supports dynamic variables (e.g., {{system__time}}, {{custom_variable}})., defaults to None
    :type llm_generated_message_prompt_override: str, optional
    """

    timeout_seconds: Optional[float] = Field(
        default=None,
        description="Time in seconds before showing the predefined message while waiting for LLM response. Set to -1 to disable.",
    )
    message: Optional[str] = Field(
        default=None,
        description="Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., {{system__time}}, {{custom_variable}}).",
    )
    additional_soft_timeout_messages: Optional[List[str]] = Field(
        default=None,
        description="Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.",
    )
    use_llm_generated_message: Optional[bool] = Field(
        default=None,
        description="If enabled, the soft timeout message will be generated dynamically instead of using the static message.",
    )
    randomize_fillers: Optional[bool] = Field(
        default=None,
        description="If enabled, shuffle the order of static soft timeout messages once at the start of each turn. Only applies when use_llm_generated_message is false.",
    )
    max_soft_timeouts_per_generation: Optional[int] = Field(
        default=None,
        description="Maximum filler messages while waiting for a single LLM response. Fires every timeout_seconds until the LLM streams content or this limit is reached.",
    )
    llm_generated_message_prompt_override: Optional[str] = Field(
        default=None,
        description="Custom prompt for generating the soft timeout filler message when use_llm_generated_message is enabled. Recent conversation context is provided as a separate user message. If not set, the default prompt will be used. Supports dynamic variables (e.g., {{system__time}}, {{custom_variable}}).",
    )
