from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    AddMemberToGroupRequest,
    AddWorkspaceGroupMemberResponseModel,
    BodyDeleteMemberFromUserGroupV1WorkspaceGroupsGroupIdMembersRemovePost,
    DeleteWorkspaceGroupMemberResponseModel,
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


class MembersClient(BaseService):
    """
    Fern-style resource client for MembersClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._remove_config: SdkConfig = {}
        self._add_config: SdkConfig = {}

    def set_remove_config(self, config: SdkConfig):
        """
        Sets method-level configuration for remove.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._remove_config = config
        return self

    def set_add_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_config = config
        return self

    @property
    def with_raw_response(self) -> "RawMembersClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawMembersClient(self)

    @cast_models
    def remove(
        self,
        group_id: str,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> DeleteWorkspaceGroupMemberResponseModel:
        """
        Removes a member from the specified group. Requires `group_members_manage` permission.

        Parameters
        ----------
        group_id : str
            The ID of the target group.

        email : str
            The email of the target workspace member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWorkspaceGroupMemberResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.groups.members.remove(
            group_id="group_id",
            email="email",
        )
        """

        Validator(str).validate(group_id, "group_id")

        resolved_config = self._get_resolved_config(
            self._remove_config, request_options
        )

        request_body = (
            BodyDeleteMemberFromUserGroupV1WorkspaceGroupsGroupIdMembersRemovePost(
                email=email
            )
        )
        Validator(
            BodyDeleteMemberFromUserGroupV1WorkspaceGroupsGroupIdMembersRemovePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/groups/{{group_id}}/members/remove",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("group_id", group_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteWorkspaceGroupMemberResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    DeleteWorkspaceGroupMemberResponseModel, response
                )
            )
        )

    @cast_models
    def add(
        self,
        group_id: str,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> AddWorkspaceGroupMemberResponseModel:
        """
        Adds a member of your workspace to the specified group. Requires `group_members_manage` permission.

        Parameters
        ----------
        group_id : str
            The ID of the target group.

        email : str
            The email of the target workspace member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddWorkspaceGroupMemberResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.groups.members.add(
            group_id="group_id",
            email="email",
        )
        """

        Validator(str).validate(group_id, "group_id")

        resolved_config = self._get_resolved_config(self._add_config, request_options)

        request_body = AddMemberToGroupRequest(email=email)
        Validator(AddMemberToGroupRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/groups/{{group_id}}/members",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("group_id", group_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddWorkspaceGroupMemberResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddWorkspaceGroupMemberResponseModel, response)
            )
        )


class RawMembersClient:
    """
    Raw-response client for MembersClient.

    Each method delegates to the matching :class:`MembersClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: MembersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def remove(
        self,
        group_id: str,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteWorkspaceGroupMemberResponseModel]:
        data = MembersClient.remove(
            self._client, group_id, email=email, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def add(
        self,
        group_id: str,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddWorkspaceGroupMemberResponseModel]:
        data = MembersClient.add(
            self._client, group_id, email=email, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncMembersClient(MembersClient):
    """
    Async wrapper for MembersClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawMembersClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawMembersClient(self)

    def remove(
        self,
        group_id: str,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DeleteWorkspaceGroupMemberResponseModel]:  # type: ignore[override]
        """
        Removes a member from the specified group. Requires `group_members_manage` permission.

        Parameters
        ----------
        group_id : str
            The ID of the target group.

        email : str
            The email of the target workspace member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWorkspaceGroupMemberResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.groups.members.remove(
                group_id="group_id",
                email="email",
            )


        asyncio.run(main())
        """
        return to_async(super().remove)(
            group_id, email=email, request_options=request_options
        )

    def add(
        self,
        group_id: str,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddWorkspaceGroupMemberResponseModel]:  # type: ignore[override]
        """
        Adds a member of your workspace to the specified group. Requires `group_members_manage` permission.

        Parameters
        ----------
        group_id : str
            The ID of the target group.

        email : str
            The email of the target workspace member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddWorkspaceGroupMemberResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.groups.members.add(
                group_id="group_id",
                email="email",
            )


        asyncio.run(main())
        """
        return to_async(super().add)(
            group_id, email=email, request_options=request_options
        )


class AsyncRawMembersClient:
    """
    Async raw-response client for AsyncMembersClient.
    """

    def __init__(self, client: AsyncMembersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def remove(
        self,
        group_id: str,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteWorkspaceGroupMemberResponseModel]:
        data = await AsyncMembersClient.remove(
            self._client, group_id, email=email, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def add(
        self,
        group_id: str,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddWorkspaceGroupMemberResponseModel]:
        data = await AsyncMembersClient.add(
            self._client, group_id, email=email, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
