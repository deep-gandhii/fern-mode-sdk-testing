from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyCreateAgentTestFolderV1ConvaiAgentTestingFoldersPost,
    BodyUpdateAgentTestFolderV1ConvaiAgentTestingFoldersFolderIdPatch,
    CreateAgentTestFolderResponseModel,
    GetAgentTestFolderResponseModel,
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


class FoldersClient(BaseService):
    """
    Fern-style resource client for FoldersClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
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
    def with_raw_response(self) -> "RawFoldersClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawFoldersClient(self)

    @cast_models
    def create(
        self,
        *,
        name: str,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> CreateAgentTestFolderResponseModel:
        """
        Creates a folder for organizing agent tests.

        Parameters
        ----------
        name : str
            The name of the folder to create

        parent_folder_id : typing.Optional[str]
            The ID of the parent folder. If not provided, the folder will be created at the root level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentTestFolderResponseModel
            Folder successfully created

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.folders.create(
            name="name",
            parent_folder_id="parent_folder_id",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateAgentTestFolderV1ConvaiAgentTestingFoldersPost(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"parent_folder_id": parent_folder_id}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateAgentTestFolderV1ConvaiAgentTestingFoldersPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/folders",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CreateAgentTestFolderResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreateAgentTestFolderResponseModel, response)
            )
        )

    @cast_models
    def get(
        self, folder_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetAgentTestFolderResponseModel:
        """
        Gets an agent test folder by ID, including its folder path.

        Parameters
        ----------
        folder_id : str
            The folder ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentTestFolderResponseModel
            Folder details retrieved successfully

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.folders.get(
            folder_id="tfld_7301khxdkycse5f88fzjdtrterzm",
        )
        """

        Validator(str).validate(folder_id, "folder_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/folders/{{folder_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("folder_id", folder_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetAgentTestFolderResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAgentTestFolderResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        folder_id: str,
        *,
        name: str,
        request_options: Optional[RequestOptions] = None,
    ) -> GetAgentTestFolderResponseModel:
        """
        Updates an agent test folder. Currently only supports updating the folder name.

        Parameters
        ----------
        folder_id : str
            The folder ID.

        name : str
            The new name for the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentTestFolderResponseModel
            Folder successfully updated

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.folders.update(
            folder_id="tfld_7301khxdkycse5f88fzjdtrterzm",
            name="name",
        )
        """

        Validator(str).validate(folder_id, "folder_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = (
            BodyUpdateAgentTestFolderV1ConvaiAgentTestingFoldersFolderIdPatch(name=name)
        )
        Validator(
            BodyUpdateAgentTestFolderV1ConvaiAgentTestingFoldersFolderIdPatch
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/folders/{{folder_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("folder_id", folder_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetAgentTestFolderResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAgentTestFolderResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self,
        folder_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes an agent test folder by ID. Use force=true to delete a non-empty folder and all its contents.

        Parameters
        ----------
        folder_id : str
            The folder ID.

        force : typing.Optional[bool]
            Force delete. Required for deleting non-empty folders.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Folder successfully deleted

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.folders.delete(
            folder_id="tfld_7301khxdkycse5f88fzjdtrterzm",
            force=False,
        )
        """

        Validator(str).validate(folder_id, "folder_id")
        Validator(bool).is_optional().is_nullable().validate(force, "force")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/folders/{{folder_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("folder_id", folder_id)
            .add_query("force", force, nullable=True)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)


class RawFoldersClient:
    """
    Raw-response client for FoldersClient.

    Each method delegates to the matching :class:`FoldersClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: FoldersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        name: str,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentTestFolderResponseModel]:
        data = FoldersClient.create(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"parent_folder_id": parent_folder_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, folder_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentTestFolderResponseModel]:
        data = FoldersClient.get(
            self._client, folder_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        folder_id: str,
        *,
        name: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentTestFolderResponseModel]:
        data = FoldersClient.update(
            self._client, folder_id, name=name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        folder_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        FoldersClient.delete(
            self._client,
            folder_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)


class AsyncFoldersClient(FoldersClient):
    """
    Async wrapper for FoldersClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawFoldersClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawFoldersClient(self)

    def create(
        self,
        *,
        name: str,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreateAgentTestFolderResponseModel]:  # type: ignore[override]
        """
        Creates a folder for organizing agent tests.

        Parameters
        ----------
        name : str
            The name of the folder to create

        parent_folder_id : typing.Optional[str]
            The ID of the parent folder. If not provided, the folder will be created at the root level.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentTestFolderResponseModel
            Folder successfully created

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.folders.create(
                name="name",
                parent_folder_id="parent_folder_id",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"parent_folder_id": parent_folder_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, folder_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetAgentTestFolderResponseModel]:  # type: ignore[override]
        """
        Gets an agent test folder by ID, including its folder path.

        Parameters
        ----------
        folder_id : str
            The folder ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentTestFolderResponseModel
            Folder details retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.folders.get(
                folder_id="tfld_7301khxdkycse5f88fzjdtrterzm",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(folder_id, request_options=request_options)

    def update(
        self,
        folder_id: str,
        *,
        name: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetAgentTestFolderResponseModel]:  # type: ignore[override]
        """
        Updates an agent test folder. Currently only supports updating the folder name.

        Parameters
        ----------
        folder_id : str
            The folder ID.

        name : str
            The new name for the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentTestFolderResponseModel
            Folder successfully updated

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.folders.update(
                folder_id="tfld_7301khxdkycse5f88fzjdtrterzm",
                name="name",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            folder_id, name=name, request_options=request_options
        )

    def delete(
        self,
        folder_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Deletes an agent test folder by ID. Use force=true to delete a non-empty folder and all its contents.

        Parameters
        ----------
        folder_id : str
            The folder ID.

        force : typing.Optional[bool]
            Force delete. Required for deleting non-empty folders.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Folder successfully deleted

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.folders.delete(
                folder_id="tfld_7301khxdkycse5f88fzjdtrterzm",
                force=False,
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            folder_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )


class AsyncRawFoldersClient:
    """
    Async raw-response client for AsyncFoldersClient.
    """

    def __init__(self, client: AsyncFoldersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        name: str,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentTestFolderResponseModel]:
        data = await AsyncFoldersClient.create(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"parent_folder_id": parent_folder_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, folder_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentTestFolderResponseModel]:
        data = await AsyncFoldersClient.get(
            self._client, folder_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        folder_id: str,
        *,
        name: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentTestFolderResponseModel]:
        data = await AsyncFoldersClient.update(
            self._client, folder_id, name=name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        folder_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        await AsyncFoldersClient.delete(
            self._client,
            folder_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)
