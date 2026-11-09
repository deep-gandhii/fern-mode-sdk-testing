from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    AgentDeploymentRequest,
    AgentDeploymentResponse,
    BodyCreateOrUpdateDeploymentsV1ConvaiAgentsAgentIdDeploymentsPost,
    HttpValidationError,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class DeploymentsClient(BaseService):
    """
    Fern-style resource client for DeploymentsClient.
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
    def with_raw_response(self) -> "RawDeploymentsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawDeploymentsClient(self)

    @cast_models
    def create(
        self,
        agent_id: str,
        *,
        deployment_request: AgentDeploymentRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> AgentDeploymentResponse:
        """
        Create a new deployment for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        deployment_request : AgentDeploymentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentDeploymentResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.deployments.create(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            deployment_request={
                "requests": [
                    {
                        "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                        "deployment_strategy": {
                            "type": "percentage",
                            "traffic_percentage": 0.5
                        }
                    }
                ]
            },
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = (
            BodyCreateOrUpdateDeploymentsV1ConvaiAgentsAgentIdDeploymentsPost(
                deployment_request=deployment_request
            )
        )
        Validator(
            BodyCreateOrUpdateDeploymentsV1ConvaiAgentsAgentIdDeploymentsPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/deployments",
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
                AgentDeploymentResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AgentDeploymentResponse, response)
            )
        )


class RawDeploymentsClient:
    """
    Raw-response client for DeploymentsClient.

    Each method delegates to the matching :class:`DeploymentsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: DeploymentsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        agent_id: str,
        *,
        deployment_request: AgentDeploymentRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentDeploymentResponse]:
        data = DeploymentsClient.create(
            self._client,
            agent_id,
            deployment_request=deployment_request,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDeploymentsClient(DeploymentsClient):
    """
    Async wrapper for DeploymentsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawDeploymentsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDeploymentsClient(self)

    def create(
        self,
        agent_id: str,
        *,
        deployment_request: AgentDeploymentRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AgentDeploymentResponse]:  # type: ignore[override]
        """
        Create a new deployment for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        deployment_request : AgentDeploymentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentDeploymentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.deployments.create(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                deployment_request={
                    "requests": [
                        {
                            "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                            "deployment_strategy": {
                                "type": "percentage",
                                "traffic_percentage": 0.5
                            }
                        }
                    ]
                },
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            agent_id,
            deployment_request=deployment_request,
            request_options=request_options,
        )


class AsyncRawDeploymentsClient:
    """
    Async raw-response client for AsyncDeploymentsClient.
    """

    def __init__(self, client: AsyncDeploymentsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        agent_id: str,
        *,
        deployment_request: AgentDeploymentRequest,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentDeploymentResponse]:
        data = await AsyncDeploymentsClient.create(
            self._client,
            agent_id,
            deployment_request=deployment_request,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
