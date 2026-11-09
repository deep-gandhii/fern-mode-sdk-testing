from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import GetToolExecutionsPageResponseModel, HttpValidationError
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class ExecutionsClient(BaseService):
    """
    Fern-style resource client for ExecutionsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    @property
    def with_raw_response(self) -> "RawExecutionsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawExecutionsClient(self)

    @cast_models
    def get(
        self,
        tool_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        is_error: Union[bool, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        start_time: Union[float, None] = SENTINEL,
        end_time: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetToolExecutionsPageResponseModel:
        """
        Get paginated list of tool executions for a specific tool.

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        is_error : typing.Optional[bool]
            Filter by error status. If not provided, returns all executions.

        agent_id : typing.Optional[str]
            Filter by agent ID.

        branch_id : typing.Optional[str]
            Filter by agent branch ID.

        start_time : typing.Optional[float]
            Filter executions from this Unix timestamp (inclusive).

        end_time : typing.Optional[float]
            Filter executions until this Unix timestamp (inclusive).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetToolExecutionsPageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tools.executions.get(
            tool_id="tool_id",
            cursor="cursor",
            page_size=30,
            is_error=True,
            agent_id="agent_id",
            branch_id="branch_id",
            start_time=8.77,
            end_time=3.44,
        )
        """

        Validator(str).validate(tool_id, "tool_id")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(bool).is_optional().is_nullable().validate(is_error, "is_error")
        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")
        Validator(str).is_optional().is_nullable().validate(branch_id, "branch_id")
        Validator(float).is_optional().is_nullable().validate(start_time, "start_time")
        Validator(float).is_optional().is_nullable().validate(end_time, "end_time")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tools/{{tool_id}}/executions",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("tool_id", tool_id)
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("is_error", is_error, nullable=True)
            .add_query("agent_id", agent_id, nullable=True)
            .add_query("branch_id", branch_id, nullable=True)
            .add_query("start_time", start_time, nullable=True)
            .add_query("end_time", end_time, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetToolExecutionsPageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetToolExecutionsPageResponseModel, response)
            )
        )


class RawExecutionsClient:
    """
    Raw-response client for ExecutionsClient.

    Each method delegates to the matching :class:`ExecutionsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ExecutionsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        tool_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        is_error: Union[bool, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        start_time: Union[float, None] = SENTINEL,
        end_time: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetToolExecutionsPageResponseModel]:
        data = ExecutionsClient.get(
            self._client,
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "is_error": is_error,
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                        "start_time": start_time,
                        "end_time": end_time,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncExecutionsClient(ExecutionsClient):
    """
    Async wrapper for ExecutionsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawExecutionsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawExecutionsClient(self)

    def get(
        self,
        tool_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        is_error: Union[bool, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        start_time: Union[float, None] = SENTINEL,
        end_time: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetToolExecutionsPageResponseModel]:  # type: ignore[override]
        """
        Get paginated list of tool executions for a specific tool.

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        is_error : typing.Optional[bool]
            Filter by error status. If not provided, returns all executions.

        agent_id : typing.Optional[str]
            Filter by agent ID.

        branch_id : typing.Optional[str]
            Filter by agent branch ID.

        start_time : typing.Optional[float]
            Filter executions from this Unix timestamp (inclusive).

        end_time : typing.Optional[float]
            Filter executions until this Unix timestamp (inclusive).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetToolExecutionsPageResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tools.executions.get(
                tool_id="tool_id",
                cursor="cursor",
                page_size=30,
                is_error=True,
                agent_id="agent_id",
                branch_id="branch_id",
                start_time=8.77,
                end_time=3.44,
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "is_error": is_error,
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                        "start_time": start_time,
                        "end_time": end_time,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawExecutionsClient:
    """
    Async raw-response client for AsyncExecutionsClient.
    """

    def __init__(self, client: AsyncExecutionsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        tool_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        is_error: Union[bool, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        start_time: Union[float, None] = SENTINEL,
        end_time: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetToolExecutionsPageResponseModel]:
        data = await AsyncExecutionsClient.get(
            self._client,
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "is_error": is_error,
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                        "start_time": start_time,
                        "end_time": end_time,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
