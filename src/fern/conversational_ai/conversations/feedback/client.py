from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types import (
    ConversationFeedbackRequestModel,
    HttpValidationError,
    UserFeedbackScore,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class FeedbackClient(BaseService):
    """
    Fern-style resource client for FeedbackClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    @property
    def with_raw_response(self) -> "RawFeedbackClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawFeedbackClient(self)

    @cast_models
    def create(
        self,
        conversation_id: str,
        *,
        feedback: Optional[UserFeedbackScore] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Send the feedback for the given conversation

        Parameters
        ----------
        conversation_id : str
            The id of the conversation you're taking the action on.

        feedback : typing.Optional[UserFeedbackScore]
            Either 'like' or 'dislike' to indicate the feedback for the conversation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.feedback.create(
            conversation_id="21m00Tcm4TlvDq8ikWAM",
            feedback="like",
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = ConversationFeedbackRequestModel(
            **dict[str, Any](
                {k: v for k, v in {"feedback": feedback}.items() if v is not SENTINEL}
            )
        )
        Validator(ConversationFeedbackRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}/feedback",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("conversation_id", conversation_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawFeedbackClient:
    """
    Raw-response client for FeedbackClient.

    Each method delegates to the matching :class:`FeedbackClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: FeedbackClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        conversation_id: str,
        *,
        feedback: Optional[UserFeedbackScore] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = FeedbackClient.create(
            self._client,
            conversation_id,
            **dict[str, Any](
                {k: v for k, v in {"feedback": feedback}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncFeedbackClient(FeedbackClient):
    """
    Async wrapper for FeedbackClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawFeedbackClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawFeedbackClient(self)

    def create(
        self,
        conversation_id: str,
        *,
        feedback: Optional[UserFeedbackScore] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Send the feedback for the given conversation

        Parameters
        ----------
        conversation_id : str
            The id of the conversation you're taking the action on.

        feedback : typing.Optional[UserFeedbackScore]
            Either 'like' or 'dislike' to indicate the feedback for the conversation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.feedback.create(
                conversation_id="21m00Tcm4TlvDq8ikWAM",
                feedback="like",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            conversation_id,
            **dict[str, Any](
                {k: v for k, v in {"feedback": feedback}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )


class AsyncRawFeedbackClient:
    """
    Async raw-response client for AsyncFeedbackClient.
    """

    def __init__(self, client: AsyncFeedbackClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        conversation_id: str,
        *,
        feedback: Optional[UserFeedbackScore] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncFeedbackClient.create(
            self._client,
            conversation_id,
            **dict[str, Any](
                {k: v for k, v in {"feedback": feedback}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
