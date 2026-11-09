from typing import TYPE_CHECKING

from .client import ElevenLabs, AsyncElevenLabs
from .net.environment import ElevenLabsEnvironment
from .version import __version__
from .errors import (
    BadRequestError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    TooEarlyError,
    UnauthorizedError,
    UnprocessableEntityError,
)

if TYPE_CHECKING:
    from .types import (
        ClosePayload,
        CommittedTranscriptEntitiesPayload,
        CommittedTranscriptPayload,
        CommittedTranscriptWithTimestampsPayload,
        ErrorPayload,
        FinalOutput,
        FinalOutputMulti,
        InitPayload,
        InputAudioChunkPayload,
        PartialTranscriptPayload,
        PingPayload,
        ReceiveMessage,
        ReceiveMessageMulti,
        ReceiveTextToDialogueWebsocketMessage,
        ReceiveTextToDialogueWebsocketMessageMulti,
        ReceiveTranscription,
        ScribeAuthErrorPayload,
        ScribeChunkSizeExceededErrorPayload,
        ScribeErrorPayload,
        ScribeInputErrorPayload,
        ScribeInsufficientAudioActivityErrorPayload,
        ScribeQueueOverflowErrorPayload,
        ScribeQuotaExceededErrorPayload,
        ScribeRateLimitedErrorPayload,
        ScribeResourceExhaustedErrorPayload,
        ScribeSessionTimeLimitExceededErrorPayload,
        ScribeThrottledErrorPayload,
        ScribeTranscriberErrorPayload,
        ScribeUnacceptedTermsErrorPayload,
        SendMessage,
        SendMessageMulti,
        SendTranslateStreamMessage,
        SendUpstreamMessage,
        SessionStartedPayload,
        TextToDialogueWebsocketClientMessage,
        TextToDialogueWebsocketClientMessageMulti,
        TextToDialogueWebsocketFinal,
        TextToDialogueWebsocketFinalMulti,
        TranslateAudioOutputError,
        TranslateAudioPayload,
        TranslateAuthError,
        TranslateErrorPayload,
        TranslateFinalTranscriptPayload,
        TranslateInputError,
        TranslatePartialTranscriptPayload,
        TranslateQueueOverflowError,
        TranslateRateLimitedError,
        TranslateSessionStartedPayload,
        TranslateStatusPayload,
        TranslateTranscriberError,
        TranslateTranslationError,
        TranslateTranslationPayload,
        UserTranscriptPayload,
    )
    from .play import play, save, stream
    from .realtime import (
        RealtimeEvents,
        RealtimeAudioOptions,
        RealtimeUrlOptions,
        AudioFormat,
        CommitStrategy,
        RealtimeConnection,
    )

from . import types as _models

import importlib

_LAZY_EXPORTS = {
    "play": ".play",
    "save": ".play",
    "stream": ".play",
    "RealtimeEvents": ".realtime",
    "RealtimeAudioOptions": ".realtime",
    "RealtimeUrlOptions": ".realtime",
    "AudioFormat": ".realtime",
    "CommitStrategy": ".realtime",
    "RealtimeConnection": ".realtime",
}


def __getattr__(name):
    """Falls back to the lazy ``.types`` registry for any name not re-exported above."""
    module = _LAZY_EXPORTS.get(name)
    if module is not None:
        value = getattr(importlib.import_module(module, __name__), name)
        globals()[name] = value
        return value
    try:
        return getattr(_models, name)
    except AttributeError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None


def __dir__():
    return sorted(set(globals()) | set(dir(_models)) | set(_LAZY_EXPORTS))
