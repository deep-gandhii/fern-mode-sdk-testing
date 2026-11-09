from typing import Any, Optional, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import (
    BodyPostAgentAvatarV1ConvaiAgentsAgentIdAvatarPost,
    HttpValidationError,
    PostAgentAvatarResponseModel,
)
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class AvatarClient(BaseService):
    """
    Fern-style resource client for AvatarClient.
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
    def with_raw_response(self) -> "RawAvatarClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAvatarClient(self)

    @cast_models
    def create(
        self,
        agent_id: str,
        *,
        avatar_file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> PostAgentAvatarResponseModel:
        """
        Sets the avatar for an agent displayed in the widget

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        avatar_file : core.File
            An image file to be used as the agent's avatar.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAgentAvatarResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.widget.avatar.create(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            avatar_file="avatar_file",
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyPostAgentAvatarV1ConvaiAgentsAgentIdAvatarPost(
            avatar_file=avatar_file
        )
        Validator(BodyPostAgentAvatarV1ConvaiAgentsAgentIdAvatarPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/avatar",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                PostAgentAvatarResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(PostAgentAvatarResponseModel, response)
            )
        )


class RawAvatarClient:
    """
    Raw-response client for AvatarClient.

    Each method delegates to the matching :class:`AvatarClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AvatarClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        agent_id: str,
        *,
        avatar_file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAgentAvatarResponseModel]:
        data = AvatarClient.create(
            self._client,
            agent_id,
            avatar_file=avatar_file,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncAvatarClient(AvatarClient):
    """
    Async wrapper for AvatarClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAvatarClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAvatarClient(self)

    def create(
        self,
        agent_id: str,
        *,
        avatar_file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PostAgentAvatarResponseModel]:  # type: ignore[override]
        """
        Sets the avatar for an agent displayed in the widget

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        avatar_file : core.File
            An image file to be used as the agent's avatar.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAgentAvatarResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.widget.avatar.create(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                avatar_file="avatar_file",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            agent_id, avatar_file=avatar_file, request_options=request_options
        )


class AsyncRawAvatarClient:
    """
    Async raw-response client for AsyncAvatarClient.
    """

    def __init__(self, client: AsyncAvatarClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        agent_id: str,
        *,
        avatar_file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAgentAvatarResponseModel]:
        data = await AsyncAvatarClient.create(
            self._client,
            agent_id,
            avatar_file=avatar_file,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
