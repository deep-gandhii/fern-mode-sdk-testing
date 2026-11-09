from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyUpdateStudioProjectContentV1StudioProjectsProjectIdContentPost,
    EditProjectResponseModel,
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


class ContentClient(BaseService):
    """
    Fern-style resource client for ContentClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._update_config: SdkConfig = {}

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    @property
    def with_raw_response(self) -> "RawContentClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawContentClient(self)

    @cast_models
    def update(
        self,
        project_id: str,
        *,
        from_url: Union[str, None] = SENTINEL,
        from_document: Union[bytes, None] = SENTINEL,
        from_content_json: Optional[str] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> EditProjectResponseModel:
        """
        Updates Studio project content.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        from_url : typing.Optional[str]
            An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        from_document : typing.Optional[core.File]
            An optional .epub, .pdf, .txt or similar file can be provided. If provided, we will initialize the Studio project with its content. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        from_content_json : typing.Optional[str]
            An optional content to initialize the Studio project with. If this is set, 'from_url' and 'from_document' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

                Example:
                [{"name": "Chapter A", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts_node"}]}, {"sub_type": "h1", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts_node"}]}]}, {"name": "Chapter B", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts_node"}]}, {"sub_type": "h2", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts_node"}]}]}]

        auto_convert : typing.Optional[bool]
            Whether to auto convert the Studio project to audio or not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditProjectResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.content.update(
            project_id="21m00Tcm4TlvDq8ikWAM",
            from_url="from_url",
            from_document="from_document",
            from_content_json="[{\\"name\\": \\"Chapter A\\", \\"blocks\\": [{\\"sub_type\\": \\"p\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"A\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"B\\", \\"type\\": \\"tts_node\\"}]}, {\\"sub_type\\": \\"h1\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"C\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"D\\", \\"type\\": \\"tts_node\\"}]}]}, {\\"name\\": \\"Chapter B\\", \\"blocks\\": [{\\"sub_type\\": \\"p\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"E\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"F\\", \\"type\\": \\"tts_node\\"}]}, {\\"sub_type\\": \\"h2\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"G\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"H\\", \\"type\\": \\"tts_node\\"}]}]}]",
            auto_convert=True,
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = (
            BodyUpdateStudioProjectContentV1StudioProjectsProjectIdContentPost(
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "from_url": from_url,
                            "from_document": from_document,
                            "from_content_json": from_content_json,
                            "auto_convert": auto_convert,
                        }.items()
                        if v is not SENTINEL
                    }
                )
            )
        )
        Validator(
            BodyUpdateStudioProjectContentV1StudioProjectsProjectIdContentPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/content",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                EditProjectResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EditProjectResponseModel, response)
            )
        )


class RawContentClient:
    """
    Raw-response client for ContentClient.

    Each method delegates to the matching :class:`ContentClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ContentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def update(
        self,
        project_id: str,
        *,
        from_url: Union[str, None] = SENTINEL,
        from_document: Union[bytes, None] = SENTINEL,
        from_content_json: Optional[str] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditProjectResponseModel]:
        data = ContentClient.update(
            self._client,
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "from_url": from_url,
                        "from_document": from_document,
                        "from_content_json": from_content_json,
                        "auto_convert": auto_convert,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncContentClient(ContentClient):
    """
    Async wrapper for ContentClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawContentClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawContentClient(self)

    def update(
        self,
        project_id: str,
        *,
        from_url: Union[str, None] = SENTINEL,
        from_document: Union[bytes, None] = SENTINEL,
        from_content_json: Optional[str] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EditProjectResponseModel]:  # type: ignore[override]
        """
        Updates Studio project content.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        from_url : typing.Optional[str]
            An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        from_document : typing.Optional[core.File]
            An optional .epub, .pdf, .txt or similar file can be provided. If provided, we will initialize the Studio project with its content. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        from_content_json : typing.Optional[str]
            An optional content to initialize the Studio project with. If this is set, 'from_url' and 'from_document' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

                Example:
                [{"name": "Chapter A", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts_node"}]}, {"sub_type": "h1", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts_node"}]}]}, {"name": "Chapter B", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts_node"}]}, {"sub_type": "h2", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts_node"}]}]}]

        auto_convert : typing.Optional[bool]
            Whether to auto convert the Studio project to audio or not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditProjectResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.content.update(
                project_id="21m00Tcm4TlvDq8ikWAM",
                from_url="from_url",
                from_document="from_document",
                from_content_json="[{\\"name\\": \\"Chapter A\\", \\"blocks\\": [{\\"sub_type\\": \\"p\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"A\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"B\\", \\"type\\": \\"tts_node\\"}]}, {\\"sub_type\\": \\"h1\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"C\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"D\\", \\"type\\": \\"tts_node\\"}]}]}, {\\"name\\": \\"Chapter B\\", \\"blocks\\": [{\\"sub_type\\": \\"p\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"E\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"F\\", \\"type\\": \\"tts_node\\"}]}, {\\"sub_type\\": \\"h2\\", \\"nodes\\": [{\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT0\\", \\"text\\": \\"G\\", \\"type\\": \\"tts_node\\"}, {\\"voice_id\\": \\"6lCwbsX1yVjD49QmpkT1\\", \\"text\\": \\"H\\", \\"type\\": \\"tts_node\\"}]}]}]",
                auto_convert=True,
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "from_url": from_url,
                        "from_document": from_document,
                        "from_content_json": from_content_json,
                        "auto_convert": auto_convert,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawContentClient:
    """
    Async raw-response client for AsyncContentClient.
    """

    def __init__(self, client: AsyncContentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def update(
        self,
        project_id: str,
        *,
        from_url: Union[str, None] = SENTINEL,
        from_document: Union[bytes, None] = SENTINEL,
        from_content_json: Optional[str] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditProjectResponseModel]:
        data = await AsyncContentClient.update(
            self._client,
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "from_url": from_url,
                        "from_document": from_document,
                        "from_content_json": from_content_json,
                        "auto_convert": auto_convert,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
