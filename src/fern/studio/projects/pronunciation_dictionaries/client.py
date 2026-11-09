from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyCreatePronunciationDictionariesV1StudioProjectsProjectIdPronunciationDictionariesPost,
    CreatePronunciationDictionaryResponseModel,
    HttpValidationError,
    PronunciationDictionaryVersionLocator,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class PronunciationDictionariesClient(BaseService):
    """
    Fern-style resource client for PronunciationDictionariesClient.
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
    def with_raw_response(self) -> "RawPronunciationDictionariesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawPronunciationDictionariesClient(self)

    @cast_models
    def create(
        self,
        project_id: str,
        *,
        pronunciation_dictionary_locators: List[PronunciationDictionaryVersionLocator],
        invalidate_affected_text: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> CreatePronunciationDictionaryResponseModel:
        """
        Create a set of pronunciation dictionaries acting on a project. This will automatically mark text within this project as requiring reconverting where the new dictionary would apply or the old one no longer does.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        pronunciation_dictionary_locators : typing.Sequence[PronunciationDictionaryVersionLocator]
            A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'.

        invalidate_affected_text : typing.Optional[bool]
            This will automatically mark text in this project for reconversion when the new dictionary applies or the old one no longer does.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePronunciationDictionaryResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.pronunciation_dictionaries.create(
            project_id="21m00Tcm4TlvDq8ikWAM",
            pronunciation_dictionary_locators=[
                {
                    "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                    "version_id": "version_id"
                }
            ],
            invalidate_affected_text=False,
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreatePronunciationDictionariesV1StudioProjectsProjectIdPronunciationDictionariesPost(
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "invalidate_affected_text": invalidate_affected_text
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(
            BodyCreatePronunciationDictionariesV1StudioProjectsProjectIdPronunciationDictionariesPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/pronunciation-dictionaries",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CreatePronunciationDictionaryResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    CreatePronunciationDictionaryResponseModel, response
                )
            )
        )


class RawPronunciationDictionariesClient:
    """
    Raw-response client for PronunciationDictionariesClient.

    Each method delegates to the matching :class:`PronunciationDictionariesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: PronunciationDictionariesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        project_id: str,
        *,
        pronunciation_dictionary_locators: List[PronunciationDictionaryVersionLocator],
        invalidate_affected_text: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatePronunciationDictionaryResponseModel]:
        data = PronunciationDictionariesClient.create(
            self._client,
            project_id,
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "invalidate_affected_text": invalidate_affected_text
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncPronunciationDictionariesClient(PronunciationDictionariesClient):
    """
    Async wrapper for PronunciationDictionariesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawPronunciationDictionariesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawPronunciationDictionariesClient(self)

    def create(
        self,
        project_id: str,
        *,
        pronunciation_dictionary_locators: List[PronunciationDictionaryVersionLocator],
        invalidate_affected_text: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreatePronunciationDictionaryResponseModel]:  # type: ignore[override]
        """
        Create a set of pronunciation dictionaries acting on a project. This will automatically mark text within this project as requiring reconverting where the new dictionary would apply or the old one no longer does.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        pronunciation_dictionary_locators : typing.Sequence[PronunciationDictionaryVersionLocator]
            A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'.

        invalidate_affected_text : typing.Optional[bool]
            This will automatically mark text in this project for reconversion when the new dictionary applies or the old one no longer does.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePronunciationDictionaryResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.pronunciation_dictionaries.create(
                project_id="21m00Tcm4TlvDq8ikWAM",
                pronunciation_dictionary_locators=[
                    {
                        "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                        "version_id": "version_id"
                    }
                ],
                invalidate_affected_text=False,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            project_id,
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "invalidate_affected_text": invalidate_affected_text
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawPronunciationDictionariesClient:
    """
    Async raw-response client for AsyncPronunciationDictionariesClient.
    """

    def __init__(self, client: AsyncPronunciationDictionariesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        project_id: str,
        *,
        pronunciation_dictionary_locators: List[PronunciationDictionaryVersionLocator],
        invalidate_affected_text: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatePronunciationDictionaryResponseModel]:
        data = await AsyncPronunciationDictionariesClient.create(
            self._client,
            project_id,
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "invalidate_affected_text": invalidate_affected_text
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
