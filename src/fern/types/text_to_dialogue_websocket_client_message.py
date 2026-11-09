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


class TextToDialogueWebsocketClientMessage(BaseModel):
    """All fields are optional unless noted for the **first** message. **First message requirements** - `voices`: non-empty array of voice IDs (maximum 10 for `eleven_v3`; exactly 1 for `eleven_v3_conversational`). - Credentials if not supplied via `xi-api-key` / `Authorization` headers or `single_use_token` query parameter. **Subsequent messages** - Do not resend `voices`, `pronunciation_dictionary_locators`, or credential fields.

    :param inputs: Dialogue lines to append for synthesis., defaults to None
    :type inputs: List[TextToDialogueWebsocketVoiceInput], optional
    :param flush: Force generation of buffered text without closing the connection., defaults to None
    :type flush: bool, optional
    :param close_socket: Flush buffers, emit remaining audio, send `is_final`, and close the WebSocket., defaults to None
    :type close_socket: bool, optional
    :param keep_alive: Resets the 20s inactivity timer; performs no synthesis., defaults to None
    :type keep_alive: bool, optional
    :param xi_api_key: API key for the first message if not provided via the `xi-api-key` header., defaults to None
    :type xi_api_key: str, optional
    :param authorization: Bearer token for the first message if not provided via the `Authorization` header., defaults to None
    :type authorization: str, optional
    :param single_use_token: Single-use token for the first message if not provided via the `single_use_token` query parameter., defaults to None
    :type single_use_token: str, optional
    :param voices: Voice IDs to load for the session (first message only, required on first message)., defaults to None
    :type voices: List[str], optional
    :param voice_settings: Voice settings for dialogue generation. Only `stability` is supported for `eleven_v3` dialogue models., defaults to None
    :type voice_settings: TextToDialogueWebsocketVoiceSettings, optional
    :param pronunciation_dictionary_locators: Optional pronunciation dictionaries (first message only)., defaults to None
    :type pronunciation_dictionary_locators: List[PronunciationDictionaryLocator], optional
    """

    inputs: Optional[List[TextToDialogueWebsocketVoiceInput]] = Field(
        default=None, description="Dialogue lines to append for synthesis."
    )
    flush: Optional[bool] = Field(
        default=None,
        description="Force generation of buffered text without closing the connection.",
    )
    close_socket: Optional[bool] = Field(
        default=None,
        description="Flush buffers, emit remaining audio, send `is_final`, and close the WebSocket.",
    )
    keep_alive: Optional[bool] = Field(
        default=None,
        description="Resets the 20s inactivity timer; performs no synthesis.",
    )
    xi_api_key: Optional[str] = Field(
        default=None,
        description="API key for the first message if not provided via the `xi-api-key` header.",
    )
    authorization: Optional[str] = Field(
        default=None,
        description="Bearer token for the first message if not provided via the `Authorization` header.",
    )
    single_use_token: Optional[str] = Field(
        default=None,
        description="Single-use token for the first message if not provided via the `single_use_token` query parameter.",
    )
    voices: Optional[List[str]] = Field(
        default=None,
        description="Voice IDs to load for the session (first message only, required on first message).",
    )
    voice_settings: Optional[TextToDialogueWebsocketVoiceSettings] = Field(
        default=None,
        description="Voice settings for dialogue generation. Only `stability` is supported for `eleven_v3` dialogue models.",
    )
    pronunciation_dictionary_locators: Optional[
        List[PronunciationDictionaryLocator]
    ] = Field(
        default=None,
        description="Optional pronunciation dictionaries (first message only).",
    )
