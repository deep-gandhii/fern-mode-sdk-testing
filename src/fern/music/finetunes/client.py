from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyCreateMusicFinetuneV1MusicFinetunesPost,
    BodyCreateMusicFinetuneV1MusicFinetunesPostModelId,
    BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility,
    FinetuneCreatedBy,
    FinetuneVisibility,
    HttpValidationError,
    ListSort,
    MusicFinetunePageResponseModel,
    MusicFinetuneResponseModel,
    SortDirection2,
    UpdateMusicFinetuneRequestModel,
    UpdateMusicFinetuneRequestModelVisibility,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class FinetunesClient(BaseService):
    """
    Fern-style resource client for FinetunesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

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
    def with_raw_response(self) -> "RawFinetunesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawFinetunesClient(self)

    @cast_models
    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        visibility: Union[FinetuneVisibility, None] = SENTINEL,
        created_by: Union[FinetuneCreatedBy, None] = SENTINEL,
        sort: Union[ListSort, None] = SENTINEL,
        sort_direction: Union[SortDirection2, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> MusicFinetunePageResponseModel:
        """
        List music finetunes accessible to you (your own, workspace-shared, and ElevenLabs-curated), with optional filtering, sorting, and cursor pagination.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching the next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many finetunes to return. Max 100, default 50.

        visibility : typing.Optional[FinetuneVisibility]
            Filter by visibility. 'private' returns private finetunes; 'workspace' returns workspace-shared finetunes; 'public' returns public finetunes, which are currently ElevenLabs curated finetunes. Omit to return all accessible finetunes.

        created_by : typing.Optional[FinetuneCreatedBy]
            Filter by creator. 'self' returns finetunes you created; 'workspace' returns finetunes created by workspace teammates; 'elevenlabs' returns ElevenLabs curated finetunes. Omit to return finetunes from all creators.

        sort : typing.Optional[ListSort]
            Sort by field (created_at or name)

        sort_direction : typing.Optional[SortDirection2]
            Sort direction (asc or desc)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetunePageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import FinetuneVisibility, FinetuneCreatedBy, ListSort, SortDirection2

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.music.finetunes.list(
            cursor="cursor",
            page_size=50,
            visibility="private",
            created_by="self",
            sort="created_at",
            sort_direction="asc",
        )
        """

        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(FinetuneVisibility).is_optional().is_nullable().validate(
            visibility, "visibility"
        )
        Validator(FinetuneCreatedBy).is_optional().is_nullable().validate(
            created_by, "created_by"
        )
        Validator(ListSort).is_optional().is_nullable().validate(sort, "sort")
        Validator(SortDirection2).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/finetunes",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("visibility", visibility, nullable=True)
            .add_query("created_by", created_by, nullable=True)
            .add_query("sort", sort, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                MusicFinetunePageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MusicFinetunePageResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        name: str,
        primary_genre: str,
        files: Optional[List[bytes]] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        visibility: Union[
            BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility, None
        ] = SENTINEL,
        model_id: Optional[
            BodyCreateMusicFinetuneV1MusicFinetunesPostModelId
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> MusicFinetuneResponseModel:
        """
        Create a new music finetune

        Parameters
        ----------
        name : str
            Name for the finetune (5-200 characters).

        primary_genre : str
            Primary musical genre of the finetune.

        files : typing.Optional[typing.Sequence[core.File]]
            Audio files to train on.

        tags : typing.Optional[typing.Sequence[str]]
            Tags to associate with the finetune.

        visibility : typing.Optional[BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility]
            Finetune visibility. Only 'private' and 'workspace' can be set.

        model_id : typing.Optional[BodyCreateMusicFinetuneV1MusicFinetunesPostModelId]
            The model to create a finetune for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetuneResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.music.finetunes.create(
            name="minim ut reprehenderit",
            primary_genre="primary_genre",
            files=[
                "files"
            ],
            tags=[
                "tags"
            ],
            visibility="private",
            model_id="music_v1",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateMusicFinetuneV1MusicFinetunesPost(
            name=name,
            primary_genre=primary_genre,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "files": files,
                        "tags": tags,
                        "visibility": visibility,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateMusicFinetuneV1MusicFinetunesPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/finetunes",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                MusicFinetuneResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MusicFinetuneResponseModel, response)
            )
        )

    @cast_models
    def get(
        self, finetune_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> MusicFinetuneResponseModel:
        """
        Get a music finetune.

        Parameters
        ----------
        finetune_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetuneResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.music.finetunes.get(
            finetune_id="finetune_id",
        )
        """

        Validator(str).validate(finetune_id, "finetune_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/finetunes/{{finetune_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("finetune_id", finetune_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                MusicFinetuneResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MusicFinetuneResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        finetune_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        primary_genre: Union[str, None] = SENTINEL,
        visibility: Union[UpdateMusicFinetuneRequestModelVisibility, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> MusicFinetuneResponseModel:
        """
        Update a music finetune.

        Parameters
        ----------
        finetune_id : str

        name : typing.Optional[str]
            Updated name for the finetune.

        tags : typing.Optional[typing.Sequence[str]]
            Replacement set of tags.

        primary_genre : typing.Optional[str]
            Updated primary musical genre.

        visibility : typing.Optional[UpdateMusicFinetuneRequestModelVisibility]
            Finetune visibility. Only 'private' and 'workspace' can be set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetuneResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.music.finetunes.update(
            finetune_id="finetune_id",
            name="velit",
            tags=[
                "tags"
            ],
            primary_genre="primary_genre",
            visibility="private",
        )
        """

        Validator(str).validate(finetune_id, "finetune_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = UpdateMusicFinetuneRequestModel(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "tags": tags,
                        "primary_genre": primary_genre,
                        "visibility": visibility,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(UpdateMusicFinetuneRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/finetunes/{{finetune_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("finetune_id", finetune_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                MusicFinetuneResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MusicFinetuneResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, finetune_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> MusicFinetuneResponseModel:
        """
        Delete a music finetune

        Parameters
        ----------
        finetune_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetuneResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.music.finetunes.delete(
            finetune_id="finetune_id",
        )
        """

        Validator(str).validate(finetune_id, "finetune_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/finetunes/{{finetune_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("finetune_id", finetune_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                MusicFinetuneResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MusicFinetuneResponseModel, response)
            )
        )


class RawFinetunesClient:
    """
    Raw-response client for FinetunesClient.

    Each method delegates to the matching :class:`FinetunesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: FinetunesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        visibility: Union[FinetuneVisibility, None] = SENTINEL,
        created_by: Union[FinetuneCreatedBy, None] = SENTINEL,
        sort: Union[ListSort, None] = SENTINEL,
        sort_direction: Union[SortDirection2, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MusicFinetunePageResponseModel]:
        data = FinetunesClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "visibility": visibility,
                        "created_by": created_by,
                        "sort": sort,
                        "sort_direction": sort_direction,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        name: str,
        primary_genre: str,
        files: Optional[List[bytes]] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        visibility: Union[
            BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility, None
        ] = SENTINEL,
        model_id: Optional[
            BodyCreateMusicFinetuneV1MusicFinetunesPostModelId
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MusicFinetuneResponseModel]:
        data = FinetunesClient.create(
            self._client,
            name=name,
            primary_genre=primary_genre,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "files": files,
                        "tags": tags,
                        "visibility": visibility,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, finetune_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[MusicFinetuneResponseModel]:
        data = FinetunesClient.get(
            self._client, finetune_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        finetune_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        primary_genre: Union[str, None] = SENTINEL,
        visibility: Union[UpdateMusicFinetuneRequestModelVisibility, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MusicFinetuneResponseModel]:
        data = FinetunesClient.update(
            self._client,
            finetune_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "tags": tags,
                        "primary_genre": primary_genre,
                        "visibility": visibility,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, finetune_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[MusicFinetuneResponseModel]:
        data = FinetunesClient.delete(
            self._client, finetune_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncFinetunesClient(FinetunesClient):
    """
    Async wrapper for FinetunesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawFinetunesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawFinetunesClient(self)

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        visibility: Union[FinetuneVisibility, None] = SENTINEL,
        created_by: Union[FinetuneCreatedBy, None] = SENTINEL,
        sort: Union[ListSort, None] = SENTINEL,
        sort_direction: Union[SortDirection2, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[MusicFinetunePageResponseModel]:  # type: ignore[override]
        """
        List music finetunes accessible to you (your own, workspace-shared, and ElevenLabs-curated), with optional filtering, sorting, and cursor pagination.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching the next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many finetunes to return. Max 100, default 50.

        visibility : typing.Optional[FinetuneVisibility]
            Filter by visibility. 'private' returns private finetunes; 'workspace' returns workspace-shared finetunes; 'public' returns public finetunes, which are currently ElevenLabs curated finetunes. Omit to return all accessible finetunes.

        created_by : typing.Optional[FinetuneCreatedBy]
            Filter by creator. 'self' returns finetunes you created; 'workspace' returns finetunes created by workspace teammates; 'elevenlabs' returns ElevenLabs curated finetunes. Omit to return finetunes from all creators.

        sort : typing.Optional[ListSort]
            Sort by field (created_at or name)

        sort_direction : typing.Optional[SortDirection2]
            Sort direction (asc or desc)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetunePageResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import FinetuneVisibility, FinetuneCreatedBy, ListSort, SortDirection2

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.music.finetunes.list(
                cursor="cursor",
                page_size=50,
                visibility="private",
                created_by="self",
                sort="created_at",
                sort_direction="asc",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "visibility": visibility,
                        "created_by": created_by,
                        "sort": sort,
                        "sort_direction": sort_direction,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        name: str,
        primary_genre: str,
        files: Optional[List[bytes]] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        visibility: Union[
            BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility, None
        ] = SENTINEL,
        model_id: Optional[
            BodyCreateMusicFinetuneV1MusicFinetunesPostModelId
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[MusicFinetuneResponseModel]:  # type: ignore[override]
        """
        Create a new music finetune

        Parameters
        ----------
        name : str
            Name for the finetune (5-200 characters).

        primary_genre : str
            Primary musical genre of the finetune.

        files : typing.Optional[typing.Sequence[core.File]]
            Audio files to train on.

        tags : typing.Optional[typing.Sequence[str]]
            Tags to associate with the finetune.

        visibility : typing.Optional[BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility]
            Finetune visibility. Only 'private' and 'workspace' can be set.

        model_id : typing.Optional[BodyCreateMusicFinetuneV1MusicFinetunesPostModelId]
            The model to create a finetune for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetuneResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.music.finetunes.create(
                name="minim ut reprehenderit",
                primary_genre="primary_genre",
                files=[
                    "files"
                ],
                tags=[
                    "tags"
                ],
                visibility="private",
                model_id="music_v1",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            name=name,
            primary_genre=primary_genre,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "files": files,
                        "tags": tags,
                        "visibility": visibility,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, finetune_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[MusicFinetuneResponseModel]:  # type: ignore[override]
        """
        Get a music finetune.

        Parameters
        ----------
        finetune_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetuneResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.music.finetunes.get(
                finetune_id="finetune_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(finetune_id, request_options=request_options)

    def update(
        self,
        finetune_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        primary_genre: Union[str, None] = SENTINEL,
        visibility: Union[UpdateMusicFinetuneRequestModelVisibility, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[MusicFinetuneResponseModel]:  # type: ignore[override]
        """
        Update a music finetune.

        Parameters
        ----------
        finetune_id : str

        name : typing.Optional[str]
            Updated name for the finetune.

        tags : typing.Optional[typing.Sequence[str]]
            Replacement set of tags.

        primary_genre : typing.Optional[str]
            Updated primary musical genre.

        visibility : typing.Optional[UpdateMusicFinetuneRequestModelVisibility]
            Finetune visibility. Only 'private' and 'workspace' can be set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetuneResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.music.finetunes.update(
                finetune_id="finetune_id",
                name="velit",
                tags=[
                    "tags"
                ],
                primary_genre="primary_genre",
                visibility="private",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            finetune_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "tags": tags,
                        "primary_genre": primary_genre,
                        "visibility": visibility,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, finetune_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[MusicFinetuneResponseModel]:  # type: ignore[override]
        """
        Delete a music finetune

        Parameters
        ----------
        finetune_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MusicFinetuneResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.music.finetunes.delete(
                finetune_id="finetune_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(finetune_id, request_options=request_options)


class AsyncRawFinetunesClient:
    """
    Async raw-response client for AsyncFinetunesClient.
    """

    def __init__(self, client: AsyncFinetunesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        visibility: Union[FinetuneVisibility, None] = SENTINEL,
        created_by: Union[FinetuneCreatedBy, None] = SENTINEL,
        sort: Union[ListSort, None] = SENTINEL,
        sort_direction: Union[SortDirection2, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MusicFinetunePageResponseModel]:
        data = await AsyncFinetunesClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "visibility": visibility,
                        "created_by": created_by,
                        "sort": sort,
                        "sort_direction": sort_direction,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        name: str,
        primary_genre: str,
        files: Optional[List[bytes]] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        visibility: Union[
            BodyCreateMusicFinetuneV1MusicFinetunesPostVisibility, None
        ] = SENTINEL,
        model_id: Optional[
            BodyCreateMusicFinetuneV1MusicFinetunesPostModelId
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MusicFinetuneResponseModel]:
        data = await AsyncFinetunesClient.create(
            self._client,
            name=name,
            primary_genre=primary_genre,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "files": files,
                        "tags": tags,
                        "visibility": visibility,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, finetune_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[MusicFinetuneResponseModel]:
        data = await AsyncFinetunesClient.get(
            self._client, finetune_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        finetune_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        primary_genre: Union[str, None] = SENTINEL,
        visibility: Union[UpdateMusicFinetuneRequestModelVisibility, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MusicFinetuneResponseModel]:
        data = await AsyncFinetunesClient.update(
            self._client,
            finetune_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "tags": tags,
                        "primary_genre": primary_genre,
                        "visibility": visibility,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, finetune_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[MusicFinetuneResponseModel]:
        data = await AsyncFinetunesClient.delete(
            self._client, finetune_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
