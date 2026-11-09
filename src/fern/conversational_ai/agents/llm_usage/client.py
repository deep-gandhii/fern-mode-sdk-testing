from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    HttpValidationError,
    LlmUsageCalculatorRequestModel,
    LlmUsageCalculatorResponseModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class LlmUsageClient(BaseService):
    """
    Fern-style resource client for LlmUsageClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._calculate_config: SdkConfig = {}

    def set_calculate_config(self, config: SdkConfig):
        """
        Sets method-level configuration for calculate.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._calculate_config = config
        return self

    @property
    def with_raw_response(self) -> "RawLlmUsageClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawLlmUsageClient(self)

    @cast_models
    def calculate(
        self,
        agent_id: str,
        *,
        prompt_length: Union[int, None] = SENTINEL,
        number_of_pages: Union[int, None] = SENTINEL,
        rag_enabled: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> LlmUsageCalculatorResponseModel:
        """
        Calculates expected number of LLM tokens needed for the specified agent.

        Parameters
        ----------
        agent_id : str

        prompt_length : typing.Optional[int]
            Length of the prompt in characters.

        number_of_pages : typing.Optional[int]
            Pages of content in pdf documents OR urls in agent's Knowledge Base.

        rag_enabled : typing.Optional[bool]
            Whether RAG is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LlmUsageCalculatorResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.llm_usage.calculate(
            agent_id="agent_id",
            prompt_length=5,
            number_of_pages=1,
            rag_enabled=False,
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._calculate_config, request_options
        )

        request_body = LlmUsageCalculatorRequestModel(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt_length": prompt_length,
                        "number_of_pages": number_of_pages,
                        "rag_enabled": rag_enabled,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(LlmUsageCalculatorRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent/{{agent_id}}/llm-usage/calculate",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                LlmUsageCalculatorResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(LlmUsageCalculatorResponseModel, response)
            )
        )


class RawLlmUsageClient:
    """
    Raw-response client for LlmUsageClient.

    Each method delegates to the matching :class:`LlmUsageClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: LlmUsageClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def calculate(
        self,
        agent_id: str,
        *,
        prompt_length: Union[int, None] = SENTINEL,
        number_of_pages: Union[int, None] = SENTINEL,
        rag_enabled: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[LlmUsageCalculatorResponseModel]:
        data = LlmUsageClient.calculate(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt_length": prompt_length,
                        "number_of_pages": number_of_pages,
                        "rag_enabled": rag_enabled,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncLlmUsageClient(LlmUsageClient):
    """
    Async wrapper for LlmUsageClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawLlmUsageClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawLlmUsageClient(self)

    def calculate(
        self,
        agent_id: str,
        *,
        prompt_length: Union[int, None] = SENTINEL,
        number_of_pages: Union[int, None] = SENTINEL,
        rag_enabled: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[LlmUsageCalculatorResponseModel]:  # type: ignore[override]
        """
        Calculates expected number of LLM tokens needed for the specified agent.

        Parameters
        ----------
        agent_id : str

        prompt_length : typing.Optional[int]
            Length of the prompt in characters.

        number_of_pages : typing.Optional[int]
            Pages of content in pdf documents OR urls in agent's Knowledge Base.

        rag_enabled : typing.Optional[bool]
            Whether RAG is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LlmUsageCalculatorResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.llm_usage.calculate(
                agent_id="agent_id",
                prompt_length=5,
                number_of_pages=1,
                rag_enabled=False,
            )


        asyncio.run(main())
        """
        return to_async(super().calculate)(
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt_length": prompt_length,
                        "number_of_pages": number_of_pages,
                        "rag_enabled": rag_enabled,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawLlmUsageClient:
    """
    Async raw-response client for AsyncLlmUsageClient.
    """

    def __init__(self, client: AsyncLlmUsageClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def calculate(
        self,
        agent_id: str,
        *,
        prompt_length: Union[int, None] = SENTINEL,
        number_of_pages: Union[int, None] = SENTINEL,
        rag_enabled: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[LlmUsageCalculatorResponseModel]:
        data = await AsyncLlmUsageClient.calculate(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "prompt_length": prompt_length,
                        "number_of_pages": number_of_pages,
                        "rag_enabled": rag_enabled,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
