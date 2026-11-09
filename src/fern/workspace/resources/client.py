from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePost,
    BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole,
    BodyUnshareWorkspaceResourceV1WorkspaceResourcesResourceIdUnsharePost,
    HttpValidationError,
    ResourceMetadataResponseModel,
    WorkspaceResourceType,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class ResourcesClient(BaseService):
    """
    Fern-style resource client for ResourcesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}
        self._share_config: SdkConfig = {}
        self._unshare_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_share_config(self, config: SdkConfig):
        """
        Sets method-level configuration for share.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._share_config = config
        return self

    def set_unshare_config(self, config: SdkConfig):
        """
        Sets method-level configuration for unshare.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._unshare_config = config
        return self

    @property
    def with_raw_response(self) -> "RawResourcesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawResourcesClient(self)

    @cast_models
    def get(
        self,
        resource_id: str,
        *,
        resource_type: WorkspaceResourceType,
        request_options: Optional[RequestOptions] = None,
    ) -> ResourceMetadataResponseModel:
        """
        Gets the metadata of a resource by ID.

        Parameters
        ----------
        resource_id : str
            The ID of the target resource.

        resource_type : WorkspaceResourceType
            Resource type of the target resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourceMetadataResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import WorkspaceResourceType

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.resources.get(
            resource_id="resource_id",
            resource_type="voice",
        )
        """

        Validator(str).validate(resource_id, "resource_id")
        Validator(WorkspaceResourceType).validate(resource_type, "resource_type")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/resources/{{resource_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("resource_id", resource_id)
            .add_query("resource_type", resource_type)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ResourceMetadataResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ResourceMetadataResponseModel, response)
            )
        )

    @cast_models
    def share(
        self,
        resource_id: str,
        *,
        role: BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole,
        resource_type: WorkspaceResourceType,
        user_email: Union[str, None] = SENTINEL,
        group_id: Union[str, None] = SENTINEL,
        workspace_api_key_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Grants a role (one of 'admin', 'editor', 'commenter', or 'viewer') on a workspace resource to a user, group, or workspace (service account) API key. This overrides any existing role the target has on the resource. To target a user or service account, pass only the user email; the user must be in your workspace. To target a group, pass only the group id. To target a workspace (service account) API key, pass the api key id; the resource will be shared with the service account associated with that key. You must have admin access to the resource to share it.

        Parameters
        ----------
        resource_id : str
            The ID of the target resource.

        role : BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole
            Role to grant to the target: one of 'admin', 'editor', 'commenter', or 'viewer'.

        resource_type : WorkspaceResourceType
            Resource types that can be shared in the workspace. The name always need to match the collection names

        user_email : typing.Optional[str]
            The email of the user or service account.

        group_id : typing.Optional[str]
            The ID of the target group. Use 'default' to set the resource's baseline role — every workspace member receives this role unless they hold a higher one through a direct user grant, group membership, or workspace (service account) API key.

        workspace_api_key_id : typing.Optional[str]
            The ID of the target workspace (service account) API key. This is not the API key string itself that you pass in the header for authentication — it is the key's ID, which workspace admins can find under Developers → Service Accounts.

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
        client.workspace.resources.share(
            resource_id="resource_id",
            role="admin",
            resource_type="voice",
            user_email="user_email",
            group_id="group_id",
            workspace_api_key_id="workspace_api_key_id",
        )
        """

        Validator(str).validate(resource_id, "resource_id")

        resolved_config = self._get_resolved_config(self._share_config, request_options)

        request_body = (
            BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePost(
                role=role,
                resource_type=resource_type,
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "user_email": user_email,
                            "group_id": group_id,
                            "workspace_api_key_id": workspace_api_key_id,
                        }.items()
                        if v is not SENTINEL
                    }
                ),
            )
        )
        Validator(
            BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/resources/{{resource_id}}/share",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("resource_id", resource_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def unshare(
        self,
        resource_id: str,
        *,
        resource_type: WorkspaceResourceType,
        user_email: Union[str, None] = SENTINEL,
        group_id: Union[str, None] = SENTINEL,
        workspace_api_key_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Removes any existing role on a workspace resource from a user, group, or workspace (service account) API key. To target a user or service account, pass only the user email; the user must be in your workspace. To target a group, pass only the group id. To target a workspace (service account) API key, pass the api key id; the resource will be unshared from the service account associated with that key. You must have admin access to the resource to unshare it. You cannot remove permissions from the user who created the resource.

        Parameters
        ----------
        resource_id : str
            The ID of the target resource.

        resource_type : WorkspaceResourceType
            Resource types that can be shared in the workspace. The name always need to match the collection names

        user_email : typing.Optional[str]
            The email of the user or service account.

        group_id : typing.Optional[str]
            The ID of the target group. Use 'default' to set the resource's baseline role — every workspace member receives this role unless they hold a higher one through a direct user grant, group membership, or workspace (service account) API key.

        workspace_api_key_id : typing.Optional[str]
            The ID of the target workspace (service account) API key. This is not the API key string itself that you pass in the header for authentication — it is the key's ID, which workspace admins can find under Developers → Service Accounts.

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
        client.workspace.resources.unshare(
            resource_id="resource_id",
            resource_type="voice",
            user_email="user_email",
            group_id="group_id",
            workspace_api_key_id="workspace_api_key_id",
        )
        """

        Validator(str).validate(resource_id, "resource_id")

        resolved_config = self._get_resolved_config(
            self._unshare_config, request_options
        )

        request_body = (
            BodyUnshareWorkspaceResourceV1WorkspaceResourcesResourceIdUnsharePost(
                resource_type=resource_type,
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "user_email": user_email,
                            "group_id": group_id,
                            "workspace_api_key_id": workspace_api_key_id,
                        }.items()
                        if v is not SENTINEL
                    }
                ),
            )
        )
        Validator(
            BodyUnshareWorkspaceResourceV1WorkspaceResourcesResourceIdUnsharePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/resources/{{resource_id}}/unshare",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("resource_id", resource_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawResourcesClient:
    """
    Raw-response client for ResourcesClient.

    Each method delegates to the matching :class:`ResourcesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ResourcesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        resource_id: str,
        *,
        resource_type: WorkspaceResourceType,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ResourceMetadataResponseModel]:
        data = ResourcesClient.get(
            self._client,
            resource_id,
            resource_type=resource_type,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def share(
        self,
        resource_id: str,
        *,
        role: BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole,
        resource_type: WorkspaceResourceType,
        user_email: Union[str, None] = SENTINEL,
        group_id: Union[str, None] = SENTINEL,
        workspace_api_key_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = ResourcesClient.share(
            self._client,
            resource_id,
            role=role,
            resource_type=resource_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "user_email": user_email,
                        "group_id": group_id,
                        "workspace_api_key_id": workspace_api_key_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def unshare(
        self,
        resource_id: str,
        *,
        resource_type: WorkspaceResourceType,
        user_email: Union[str, None] = SENTINEL,
        group_id: Union[str, None] = SENTINEL,
        workspace_api_key_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = ResourcesClient.unshare(
            self._client,
            resource_id,
            resource_type=resource_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "user_email": user_email,
                        "group_id": group_id,
                        "workspace_api_key_id": workspace_api_key_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncResourcesClient(ResourcesClient):
    """
    Async wrapper for ResourcesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawResourcesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawResourcesClient(self)

    def get(
        self,
        resource_id: str,
        *,
        resource_type: WorkspaceResourceType,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ResourceMetadataResponseModel]:  # type: ignore[override]
        """
        Gets the metadata of a resource by ID.

        Parameters
        ----------
        resource_id : str
            The ID of the target resource.

        resource_type : WorkspaceResourceType
            Resource type of the target resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourceMetadataResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import WorkspaceResourceType

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.resources.get(
                resource_id="resource_id",
                resource_type="voice",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            resource_id, resource_type=resource_type, request_options=request_options
        )

    def share(
        self,
        resource_id: str,
        *,
        role: BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole,
        resource_type: WorkspaceResourceType,
        user_email: Union[str, None] = SENTINEL,
        group_id: Union[str, None] = SENTINEL,
        workspace_api_key_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Grants a role (one of 'admin', 'editor', 'commenter', or 'viewer') on a workspace resource to a user, group, or workspace (service account) API key. This overrides any existing role the target has on the resource. To target a user or service account, pass only the user email; the user must be in your workspace. To target a group, pass only the group id. To target a workspace (service account) API key, pass the api key id; the resource will be shared with the service account associated with that key. You must have admin access to the resource to share it.

        Parameters
        ----------
        resource_id : str
            The ID of the target resource.

        role : BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole
            Role to grant to the target: one of 'admin', 'editor', 'commenter', or 'viewer'.

        resource_type : WorkspaceResourceType
            Resource types that can be shared in the workspace. The name always need to match the collection names

        user_email : typing.Optional[str]
            The email of the user or service account.

        group_id : typing.Optional[str]
            The ID of the target group. Use 'default' to set the resource's baseline role — every workspace member receives this role unless they hold a higher one through a direct user grant, group membership, or workspace (service account) API key.

        workspace_api_key_id : typing.Optional[str]
            The ID of the target workspace (service account) API key. This is not the API key string itself that you pass in the header for authentication — it is the key's ID, which workspace admins can find under Developers → Service Accounts.

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
            await client.workspace.resources.share(
                resource_id="resource_id",
                role="admin",
                resource_type="voice",
                user_email="user_email",
                group_id="group_id",
                workspace_api_key_id="workspace_api_key_id",
            )


        asyncio.run(main())
        """
        return to_async(super().share)(
            resource_id,
            role=role,
            resource_type=resource_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "user_email": user_email,
                        "group_id": group_id,
                        "workspace_api_key_id": workspace_api_key_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def unshare(
        self,
        resource_id: str,
        *,
        resource_type: WorkspaceResourceType,
        user_email: Union[str, None] = SENTINEL,
        group_id: Union[str, None] = SENTINEL,
        workspace_api_key_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Removes any existing role on a workspace resource from a user, group, or workspace (service account) API key. To target a user or service account, pass only the user email; the user must be in your workspace. To target a group, pass only the group id. To target a workspace (service account) API key, pass the api key id; the resource will be unshared from the service account associated with that key. You must have admin access to the resource to unshare it. You cannot remove permissions from the user who created the resource.

        Parameters
        ----------
        resource_id : str
            The ID of the target resource.

        resource_type : WorkspaceResourceType
            Resource types that can be shared in the workspace. The name always need to match the collection names

        user_email : typing.Optional[str]
            The email of the user or service account.

        group_id : typing.Optional[str]
            The ID of the target group. Use 'default' to set the resource's baseline role — every workspace member receives this role unless they hold a higher one through a direct user grant, group membership, or workspace (service account) API key.

        workspace_api_key_id : typing.Optional[str]
            The ID of the target workspace (service account) API key. This is not the API key string itself that you pass in the header for authentication — it is the key's ID, which workspace admins can find under Developers → Service Accounts.

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
            await client.workspace.resources.unshare(
                resource_id="resource_id",
                resource_type="voice",
                user_email="user_email",
                group_id="group_id",
                workspace_api_key_id="workspace_api_key_id",
            )


        asyncio.run(main())
        """
        return to_async(super().unshare)(
            resource_id,
            resource_type=resource_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "user_email": user_email,
                        "group_id": group_id,
                        "workspace_api_key_id": workspace_api_key_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawResourcesClient:
    """
    Async raw-response client for AsyncResourcesClient.
    """

    def __init__(self, client: AsyncResourcesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        resource_id: str,
        *,
        resource_type: WorkspaceResourceType,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ResourceMetadataResponseModel]:
        data = await AsyncResourcesClient.get(
            self._client,
            resource_id,
            resource_type=resource_type,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def share(
        self,
        resource_id: str,
        *,
        role: BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole,
        resource_type: WorkspaceResourceType,
        user_email: Union[str, None] = SENTINEL,
        group_id: Union[str, None] = SENTINEL,
        workspace_api_key_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncResourcesClient.share(
            self._client,
            resource_id,
            role=role,
            resource_type=resource_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "user_email": user_email,
                        "group_id": group_id,
                        "workspace_api_key_id": workspace_api_key_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def unshare(
        self,
        resource_id: str,
        *,
        resource_type: WorkspaceResourceType,
        user_email: Union[str, None] = SENTINEL,
        group_id: Union[str, None] = SENTINEL,
        workspace_api_key_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncResourcesClient.unshare(
            self._client,
            resource_id,
            resource_type=resource_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "user_email": user_email,
                        "group_id": group_id,
                        "workspace_api_key_id": workspace_api_key_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
