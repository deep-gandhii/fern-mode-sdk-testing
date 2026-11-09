from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .text_to_dialogue_websocket_voice_input import TextToDialogueWebsocketVoiceInput
from .text_to_dialogue_websocket_voice_settings import (
    TextToDialogueWebsocketVoiceSettings,
)
from .pronunciation_dictionary_locator import PronunciationDictionaryLocator


class TextToDialogueWebsocketClientMessageMulti(BaseModel):
    """All fields are optional unless noted for a context's **first** message. **Every message** - `context_id` is required, except on a message containing only `close_socket`. **First message for a context** - `voices`: non-empty array of voice IDs (maximum 10 per context for `eleven_v3`; exactly 1 for `eleven_v3_conversational`). - Credentials if not supplied via `xi-api-key` / `Authorization` headers or `single_use_token` query parameter (accepted on the first message of the connection only). **Subsequent messages for a context** - Do not resend `voices`, `voice_settings`, `pronunciation_dictionary_locators`, or credential fields.

    :param context_id: Identifier for an independent dialogue stream within the socket. The first message with a new `context_id` creates that context. Required on every message except one containing only `close_socket`., defaults to None
    :type context_id: str, optional
    :param inputs: Dialogue lines to append to this context for synthesis. Each `voice_id` must be registered for this context., defaults to None
    :type inputs: List[TextToDialogueWebsocketVoiceInput], optional
    :param flush: Force generation of this context's buffered text without closing it., defaults to None
    :type flush: bool, optional
    :param close_context: Flush this context's remaining audio, emit its `is_final` message, and close it. Other contexts stay open., defaults to None
    :type close_context: bool, optional
    :param close_socket: Flush all contexts, emit their remaining audio and `is_final` messages, and close the WebSocket., defaults to None
    :type close_socket: bool, optional
    :param keep_alive: Resets this context's 20s inactivity timer; performs no synthesis., defaults to None
    :type keep_alive: bool, optional
    :param xi_api_key: API key for the first message of the connection if not provided via the `xi-api-key` header., defaults to None
    :type xi_api_key: str, optional
    :param authorization: Bearer token for the first message of the connection if not provided via the `Authorization` header., defaults to None
    :type authorization: str, optional
    :param single_use_token: Single-use token for the first message of the connection if not provided via the `single_use_token` query parameter., defaults to None
    :type single_use_token: str, optional
    :param voices: Voice IDs to load for this context (first message for the context only, required on that message)., defaults to None
    :type voices: List[str], optional
    :param voice_settings: Voice settings for dialogue generation. Only `stability` is supported for `eleven_v3` dialogue models., defaults to None
    :type voice_settings: TextToDialogueWebsocketVoiceSettings, optional
    :param pronunciation_dictionary_locators: Optional pronunciation dictionaries for this context (first message for the context only)., defaults to None
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryLocator], optional
    """

    context_id: Optional[str] = Field(
        default=None,
        description="Identifier for an independent dialogue stream within the socket. The first message with a new `context_id` creates that context. Required on every message except one containing only `close_socket`.",
    )
    inputs: Optional[List[TextToDialogueWebsocketVoiceInput]] = Field(
        default=None,
        description="Dialogue lines to append to this context for synthesis. Each `voice_id` must be registered for this context.",
    )
    flush: Optional[bool] = Field(
        default=None,
        description="Force generation of this context's buffered text without closing it.",
    )
    close_context: Optional[bool] = Field(
        default=None,
        description="Flush this context's remaining audio, emit its `is_final` message, and close it. Other contexts stay open.",
    )
    close_socket: Optional[bool] = Field(
        default=None,
        description="Flush all contexts, emit their remaining audio and `is_final` messages, and close the WebSocket.",
    )
    keep_alive: Optional[bool] = Field(
        default=None,
        description="Resets this context's 20s inactivity timer; performs no synthesis.",
    )
    xi_api_key: Optional[str] = Field(
        default=None,
        description="API key for the first message of the connection if not provided via the `xi-api-key` header.",
    )
    authorization: Optional[str] = Field(
        default=None,
        description="Bearer token for the first message of the connection if not provided via the `Authorization` header.",
    )
    single_use_token: Optional[str] = Field(
        default=None,
        description="Single-use token for the first message of the connection if not provided via the `single_use_token` query parameter.",
    )
    voices: Optional[List[str]] = Field(
        default=None,
        description="Voice IDs to load for this context (first message for the context only, required on that message).",
    )
    voice_settings: Optional[TextToDialogueWebsocketVoiceSettings] = Field(
        default=None,
        description="Voice settings for dialogue generation. Only `stability` is supported for `eleven_v3` dialogue models.",
    )
    pronunciation_dictionary_locators: Optional[
        List[PronunciationDictionaryLocator]
    ] = Field(
        default=None,
        description="Optional pronunciation dictionaries for this context (first message for the context only).",
    )
