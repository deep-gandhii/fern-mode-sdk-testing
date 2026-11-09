from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    AnalysisScope,
    GetConversationResponseModel,
    HttpValidationError,
    RunConversationEvaluationsRequest,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class AnalysisClient(BaseService):
    """
    Fern-style resource client for AnalysisClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._run_config: SdkConfig = {}
        self._run_evaluation_config: SdkConfig = {}

    def set_run_config(self, config: SdkConfig):
        """
        Sets method-level configuration for run.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._run_config = config
        return self

    def set_run_evaluation_config(self, config: SdkConfig):
        """
        Sets method-level configuration for run_evaluation.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._run_evaluation_config = config
        return self

    @property
    def with_raw_response(self) -> "RawAnalysisClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAnalysisClient(self)

    @cast_models
    def run(
        self, conversation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetConversationResponseModel:
        """
        Run the analysis for a conversation using the agent's current evaluation criteria and data collection settings.

        Parameters
        ----------
        conversation_id : str
            ID of the conversation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.analysis.run(
            conversation_id="conversation_id",
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")

        resolved_config = self._get_resolved_config(self._run_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}/analysis/run",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("conversation_id", conversation_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetConversationResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConversationResponseModel, response)
            )
        )

    @cast_models
    def run_evaluation(
        self,
        conversation_id: str,
        *,
        evaluation_id: str,
        scope: Optional[AnalysisScope] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetConversationResponseModel:
        """
        Rerun a specific evaluation for a conversation.

        Parameters
        ----------
        conversation_id : str
            ID of the conversation

        evaluation_id : str
            ID of the single evaluation criterion to rerun.

        scope : typing.Optional[AnalysisScope]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.analysis.run_evaluation(
            conversation_id="conversation_id",
            evaluation_id="evaluation_id",
            scope="conversation",
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")

        resolved_config = self._get_resolved_config(
            self._run_evaluation_config, request_options
        )

        request_body = RunConversationEvaluationsRequest(
            evaluation_id=evaluation_id,
            **dict[str, Any](
                {k: v for k, v in {"scope": scope}.items() if v is not SENTINEL}
            ),
        )
        Validator(RunConversationEvaluationsRequest).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}/analysis/evaluations/run",
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
        return (
            None
            if response in (b"", "")
            else (
                GetConversationResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConversationResponseModel, response)
            )
        )


class RawAnalysisClient:
    """
    Raw-response client for AnalysisClient.

    Each method delegates to the matching :class:`AnalysisClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AnalysisClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def run(
        self, conversation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetConversationResponseModel]:
        data = AnalysisClient.run(
            self._client, conversation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def run_evaluation(
        self,
        conversation_id: str,
        *,
        evaluation_id: str,
        scope: Optional[AnalysisScope] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationResponseModel]:
        data = AnalysisClient.run_evaluation(
            self._client,
            conversation_id,
            evaluation_id=evaluation_id,
            **dict[str, Any](
                {k: v for k, v in {"scope": scope}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncAnalysisClient(AnalysisClient):
    """
    Async wrapper for AnalysisClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAnalysisClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAnalysisClient(self)

    def run(
        self, conversation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetConversationResponseModel]:  # type: ignore[override]
        """
        Run the analysis for a conversation using the agent's current evaluation criteria and data collection settings.

        Parameters
        ----------
        conversation_id : str
            ID of the conversation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.analysis.run(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        return to_async(super().run)(conversation_id, request_options=request_options)

    def run_evaluation(
        self,
        conversation_id: str,
        *,
        evaluation_id: str,
        scope: Optional[AnalysisScope] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetConversationResponseModel]:  # type: ignore[override]
        """
        Rerun a specific evaluation for a conversation.

        Parameters
        ----------
        conversation_id : str
            ID of the conversation

        evaluation_id : str
            ID of the single evaluation criterion to rerun.

        scope : typing.Optional[AnalysisScope]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.analysis.run_evaluation(
                conversation_id="conversation_id",
                evaluation_id="evaluation_id",
                scope="conversation",
            )


        asyncio.run(main())
        """
        return to_async(super().run_evaluation)(
            conversation_id,
            evaluation_id=evaluation_id,
            **dict[str, Any](
                {k: v for k, v in {"scope": scope}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )


class AsyncRawAnalysisClient:
    """
    Async raw-response client for AsyncAnalysisClient.
    """

    def __init__(self, client: AsyncAnalysisClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def run(
        self, conversation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetConversationResponseModel]:
        data = await AsyncAnalysisClient.run(
            self._client, conversation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def run_evaluation(
        self,
        conversation_id: str,
        *,
        evaluation_id: str,
        scope: Optional[AnalysisScope] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationResponseModel]:
        data = await AsyncAnalysisClient.run_evaluation(
            self._client,
            conversation_id,
            evaluation_id=evaluation_id,
            **dict[str, Any](
                {k: v for k, v in {"scope": scope}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
