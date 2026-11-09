from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types import (
    AgentWorkflowRequestModel,
    BodyCreateAgentDraftV1ConvaiAgentsAgentIdDraftsPost,
    HttpValidationError,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class DraftsClient(BaseService):
    """
    Fern-style resource client for DraftsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    @property
    def with_raw_response(self) -> "RawDraftsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawDraftsClient(self)

    @cast_models
    def create(
        self,
        agent_id: str,
        *,
        conversation_config: dict,
        platform_settings: dict,
        workflow: AgentWorkflowRequestModel,
        name: str,
        branch_id: str,
        tags: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Create a new draft for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        conversation_config : typing.Dict[str, typing.Optional[typing.Any]]
            Conversation config for the draft

        platform_settings : typing.Dict[str, typing.Optional[typing.Any]]
            Platform settings for the draft

        workflow : AgentWorkflowRequestModel

        name : str
            Name for the draft

        branch_id : str
            The ID of the agent branch to use

        tags : typing.Optional[typing.Sequence[str]]
            Tags to help classify and filter the agent

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
        client.conversational_ai.agents.drafts.create(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
            conversation_config={},
            platform_settings={},
            workflow={
                "edges": {},
                "nodes": {},
                "prevent_subagent_loops": True
            },
            name="name",
            tags=[
                "tags"
            ],
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateAgentDraftV1ConvaiAgentsAgentIdDraftsPost(
            conversation_config=conversation_config,
            platform_settings=platform_settings,
            workflow=workflow,
            name=name,
            **dict[str, Any](
                {k: v for k, v in {"tags": tags}.items() if v is not SENTINEL}
            ),
        )
        Validator(BodyCreateAgentDraftV1ConvaiAgentsAgentIdDraftsPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/drafts",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_query("branch_id", branch_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def delete(
        self,
        agent_id: str,
        *,
        branch_id: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Delete a draft for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            The ID of the agent branch to use

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
        client.conversational_ai.agents.drafts.delete(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/drafts",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_query("branch_id", branch_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawDraftsClient:
    """
    Raw-response client for DraftsClient.

    Each method delegates to the matching :class:`DraftsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: DraftsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        agent_id: str,
        *,
        conversation_config: dict,
        platform_settings: dict,
        workflow: AgentWorkflowRequestModel,
        name: str,
        branch_id: str,
        tags: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = DraftsClient.create(
            self._client,
            agent_id,
            conversation_config=conversation_config,
            platform_settings=platform_settings,
            workflow=workflow,
            name=name,
            branch_id=branch_id,
            **dict[str, Any](
                {k: v for k, v in {"tags": tags}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        agent_id: str,
        *,
        branch_id: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = DraftsClient.delete(
            self._client, agent_id, branch_id=branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDraftsClient(DraftsClient):
    """
    Async wrapper for DraftsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawDraftsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDraftsClient(self)

    def create(
        self,
        agent_id: str,
        *,
        conversation_config: dict,
        platform_settings: dict,
        workflow: AgentWorkflowRequestModel,
        name: str,
        branch_id: str,
        tags: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Create a new draft for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        conversation_config : typing.Dict[str, typing.Optional[typing.Any]]
            Conversation config for the draft

        platform_settings : typing.Dict[str, typing.Optional[typing.Any]]
            Platform settings for the draft

        workflow : AgentWorkflowRequestModel

        name : str
            Name for the draft

        branch_id : str
            The ID of the agent branch to use

        tags : typing.Optional[typing.Sequence[str]]
            Tags to help classify and filter the agent

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
            await client.conversational_ai.agents.drafts.create(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                conversation_config={},
                platform_settings={},
                workflow={
                    "edges": {},
                    "nodes": {},
                    "prevent_subagent_loops": True
                },
                name="name",
                tags=[
                    "tags"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            agent_id,
            conversation_config=conversation_config,
            platform_settings=platform_settings,
            workflow=workflow,
            name=name,
            branch_id=branch_id,
            **dict[str, Any](
                {k: v for k, v in {"tags": tags}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def delete(
        self,
        agent_id: str,
        *,
        branch_id: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete a draft for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            The ID of the agent branch to use

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
            await client.conversational_ai.agents.drafts.delete(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            agent_id, branch_id=branch_id, request_options=request_options
        )


class AsyncRawDraftsClient:
    """
    Async raw-response client for AsyncDraftsClient.
    """

    def __init__(self, client: AsyncDraftsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        agent_id: str,
        *,
        conversation_config: dict,
        platform_settings: dict,
        workflow: AgentWorkflowRequestModel,
        name: str,
        branch_id: str,
        tags: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncDraftsClient.create(
            self._client,
            agent_id,
            conversation_config=conversation_config,
            platform_settings=platform_settings,
            workflow=workflow,
            name=name,
            branch_id=branch_id,
            **dict[str, Any](
                {k: v for k, v in {"tags": tags}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        agent_id: str,
        *,
        branch_id: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncDraftsClient.delete(
            self._client, agent_id, branch_id=branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
