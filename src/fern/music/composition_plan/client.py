from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types.composition_plan_create_response import (
    CompositionPlanCreateResponse_adapter,
)
from ...types import (
    BodyGenerateCompositionPlanV1MusicPlanPost,
    BodyGenerateCompositionPlanV1MusicPlanPostModelId,
    BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan,
    CompositionPlanCreateResponse,
    HttpValidationError,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class CompositionPlanClient(BaseService):
    """
    Fern-style resource client for CompositionPlanClient.
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
    def with_raw_response(self) -> "RawCompositionPlanClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawCompositionPlanClient(self)

    @cast_models
    def create(
        self,
        *,
        prompt: str,
        music_length_ms: Union[int, None] = SENTINEL,
        source_composition_plan: Union[
            BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan, None
        ] = SENTINEL,
        model_id: Optional[
            BodyGenerateCompositionPlanV1MusicPlanPostModelId
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> CompositionPlanCreateResponse:
        """
        Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier.

        Parameters
        ----------
        prompt : str
            A simple text prompt to compose a plan from.

        music_length_ms : typing.Optional[int]
            The length of the composition plan to generate in milliseconds. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        source_composition_plan : typing.Optional[BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan]
            An optional composition plan to use as a source for the new composition plan.

        model_id : typing.Optional[BodyGenerateCompositionPlanV1MusicPlanPostModelId]
            The model to use for the generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompositionPlanCreateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.music.composition_plan.create(
            prompt="prompt",
            music_length_ms=123103,
            source_composition_plan={
                "positive_global_styles": [
                    "positive_global_styles"
                ],
                "negative_global_styles": [
                    "negative_global_styles"
                ],
                "sections": [
                    {
                        "section_name": "section_name",
                        "positive_local_styles": [
                            "positive_local_styles"
                        ],
                        "negative_local_styles": [
                            "negative_local_styles"
                        ],
                        "duration_ms": 9189,
                        "lines": [
                            "lines"
                        ],
                        "source_from": {
                            "song_id": "song_id",
                            "range": {
                                "start_ms": 9,
                                "end_ms": 4
                            },
                            "negative_ranges": [
                                {
                                    "start_ms": 9,
                                    "end_ms": 4
                                }
                            ]
                        }
                    }
                ]
            },
            model_id="music_v1",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyGenerateCompositionPlanV1MusicPlanPost(
            prompt=prompt,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "music_length_ms": music_length_ms,
                        "source_composition_plan": source_composition_plan,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyGenerateCompositionPlanV1MusicPlanPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/music/plan",
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
                CompositionPlanCreateResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CompositionPlanCreateResponse, response)
            )
        )


class RawCompositionPlanClient:
    """
    Raw-response client for CompositionPlanClient.

    Each method delegates to the matching :class:`CompositionPlanClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: CompositionPlanClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        prompt: str,
        music_length_ms: Union[int, None] = SENTINEL,
        source_composition_plan: Union[
            BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan, None
        ] = SENTINEL,
        model_id: Optional[
            BodyGenerateCompositionPlanV1MusicPlanPostModelId
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CompositionPlanCreateResponse]:
        data = CompositionPlanClient.create(
            self._client,
            prompt=prompt,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "music_length_ms": music_length_ms,
                        "source_composition_plan": source_composition_plan,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncCompositionPlanClient(CompositionPlanClient):
    """
    Async wrapper for CompositionPlanClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawCompositionPlanClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawCompositionPlanClient(self)

    def create(
        self,
        *,
        prompt: str,
        music_length_ms: Union[int, None] = SENTINEL,
        source_composition_plan: Union[
            BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan, None
        ] = SENTINEL,
        model_id: Optional[
            BodyGenerateCompositionPlanV1MusicPlanPostModelId
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CompositionPlanCreateResponse]:  # type: ignore[override]
        """
        Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier.

        Parameters
        ----------
        prompt : str
            A simple text prompt to compose a plan from.

        music_length_ms : typing.Optional[int]
            The length of the composition plan to generate in milliseconds. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.

        source_composition_plan : typing.Optional[BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan]
            An optional composition plan to use as a source for the new composition plan.

        model_id : typing.Optional[BodyGenerateCompositionPlanV1MusicPlanPostModelId]
            The model to use for the generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompositionPlanCreateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.music.composition_plan.create(
                prompt="prompt",
                music_length_ms=123103,
                source_composition_plan={
                    "positive_global_styles": [
                        "positive_global_styles"
                    ],
                    "negative_global_styles": [
                        "negative_global_styles"
                    ],
                    "sections": [
                        {
                            "section_name": "section_name",
                            "positive_local_styles": [
                                "positive_local_styles"
                            ],
                            "negative_local_styles": [
                                "negative_local_styles"
                            ],
                            "duration_ms": 9189,
                            "lines": [
                                "lines"
                            ],
                            "source_from": {
                                "song_id": "song_id",
                                "range": {
                                    "start_ms": 9,
                                    "end_ms": 4
                                },
                                "negative_ranges": [
                                    {
                                        "start_ms": 9,
                                        "end_ms": 4
                                    }
                                ]
                            }
                        }
                    ]
                },
                model_id="music_v1",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            prompt=prompt,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "music_length_ms": music_length_ms,
                        "source_composition_plan": source_composition_plan,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawCompositionPlanClient:
    """
    Async raw-response client for AsyncCompositionPlanClient.
    """

    def __init__(self, client: AsyncCompositionPlanClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        prompt: str,
        music_length_ms: Union[int, None] = SENTINEL,
        source_composition_plan: Union[
            BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan, None
        ] = SENTINEL,
        model_id: Optional[
            BodyGenerateCompositionPlanV1MusicPlanPostModelId
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CompositionPlanCreateResponse]:
        data = await AsyncCompositionPlanClient.create(
            self._client,
            prompt=prompt,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "music_length_ms": music_length_ms,
                        "source_composition_plan": source_composition_plan,
                        "model_id": model_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
