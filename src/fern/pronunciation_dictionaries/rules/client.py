from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules,
    BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules1,
    HttpValidationError,
    PronunciationDictionary,
    PronunciationDictionaryRule,
    PronunciationDictionaryRulesResponseModel,
    RemovePronunciationDictionaryRulesRequest,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class RulesClient(BaseService):
    """
    Fern-style resource client for RulesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._set_config: SdkConfig = {}
        self._add_config: SdkConfig = {}
        self._remove_config: SdkConfig = {}

    def set_set_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_config = config
        return self

    def set_add_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_config = config
        return self

    def set_remove_config(self, config: SdkConfig):
        """
        Sets method-level configuration for remove.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._remove_config = config
        return self

    @property
    def with_raw_response(self) -> "RawRulesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawRulesClient(self)

    @cast_models
    def set(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: List[
            BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules1
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> PronunciationDictionaryRulesResponseModel:
        """
        Replaces all existing rules on the pronunciation dictionary with the provided ones.

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rules : typing.Sequence[BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules1]
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PronunciationDictionaryRulesResponseModel
            Successfully set rules on the pronunciation dictionary

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.pronunciation_dictionaries.rules.set(
            pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
            rules=[
                {
                    "string_to_replace": "string_to_replace",
                    "case_sensitive": True,
                    "word_boundaries": True,
                    "type": "alias",
                    "alias": "alias"
                }
            ],
        )
        """

        Validator(str).validate(
            pronunciation_dictionary_id, "pronunciation_dictionary_id"
        )

        resolved_config = self._get_resolved_config(self._set_config, request_options)

        request_body = BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules(
            rules=rules
        )
        Validator(
            BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries/{{pronunciation_dictionary_id}}/set-rules",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("pronunciation_dictionary_id", pronunciation_dictionary_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                PronunciationDictionaryRulesResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    PronunciationDictionaryRulesResponseModel, response
                )
            )
        )

    @cast_models
    def add(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: List[PronunciationDictionaryRule],
        request_options: Optional[RequestOptions] = None,
    ) -> PronunciationDictionaryRulesResponseModel:
        """
        Add rules to the pronunciation dictionary. If a rule with the same string_to_replace already exists, it will be replaced.

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rules : typing.Sequence[PronunciationDictionaryRule]
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PronunciationDictionaryRulesResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.pronunciation_dictionaries.rules.add(
            pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
            rules=[
                {
                    "string_to_replace": "string_to_replace",
                    "case_sensitive": True,
                    "word_boundaries": True,
                    "type": "alias",
                    "alias": "alias"
                }
            ],
        )
        """

        Validator(str).validate(
            pronunciation_dictionary_id, "pronunciation_dictionary_id"
        )

        resolved_config = self._get_resolved_config(self._add_config, request_options)

        request_body = PronunciationDictionary(rules=rules)
        Validator(PronunciationDictionary).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries/{{pronunciation_dictionary_id}}/add-rules",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("pronunciation_dictionary_id", pronunciation_dictionary_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                PronunciationDictionaryRulesResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    PronunciationDictionaryRulesResponseModel, response
                )
            )
        )

    @cast_models
    def remove(
        self,
        pronunciation_dictionary_id: str,
        *,
        rule_strings: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> PronunciationDictionaryRulesResponseModel:
        """
        Remove rules from the pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rule_strings : typing.Sequence[str]
            List of strings to remove from the pronunciation dictionary.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PronunciationDictionaryRulesResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.pronunciation_dictionaries.rules.remove(
            pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
            rule_strings=[
                "rule_strings"
            ],
        )
        """

        Validator(str).validate(
            pronunciation_dictionary_id, "pronunciation_dictionary_id"
        )

        resolved_config = self._get_resolved_config(
            self._remove_config, request_options
        )

        request_body = RemovePronunciationDictionaryRulesRequest(
            rule_strings=rule_strings
        )
        Validator(RemovePronunciationDictionaryRulesRequest).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/pronunciation-dictionaries/{{pronunciation_dictionary_id}}/remove-rules",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("pronunciation_dictionary_id", pronunciation_dictionary_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                PronunciationDictionaryRulesResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    PronunciationDictionaryRulesResponseModel, response
                )
            )
        )


class RawRulesClient:
    """
    Raw-response client for RulesClient.

    Each method delegates to the matching :class:`RulesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: RulesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def set(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: List[
            BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules1
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PronunciationDictionaryRulesResponseModel]:
        data = RulesClient.set(
            self._client,
            pronunciation_dictionary_id,
            rules=rules,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def add(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: List[PronunciationDictionaryRule],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PronunciationDictionaryRulesResponseModel]:
        data = RulesClient.add(
            self._client,
            pronunciation_dictionary_id,
            rules=rules,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def remove(
        self,
        pronunciation_dictionary_id: str,
        *,
        rule_strings: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PronunciationDictionaryRulesResponseModel]:
        data = RulesClient.remove(
            self._client,
            pronunciation_dictionary_id,
            rule_strings=rule_strings,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncRulesClient(RulesClient):
    """
    Async wrapper for RulesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawRulesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawRulesClient(self)

    def set(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: List[
            BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules1
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PronunciationDictionaryRulesResponseModel]:  # type: ignore[override]
        """
        Replaces all existing rules on the pronunciation dictionary with the provided ones.

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rules : typing.Sequence[BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules1]
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PronunciationDictionaryRulesResponseModel
            Successfully set rules on the pronunciation dictionary

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.pronunciation_dictionaries.rules.set(
                pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
                rules=[
                    {
                        "string_to_replace": "string_to_replace",
                        "case_sensitive": True,
                        "word_boundaries": True,
                        "type": "alias",
                        "alias": "alias"
                    }
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().set)(
            pronunciation_dictionary_id, rules=rules, request_options=request_options
        )

    def add(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: List[PronunciationDictionaryRule],
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PronunciationDictionaryRulesResponseModel]:  # type: ignore[override]
        """
        Add rules to the pronunciation dictionary. If a rule with the same string_to_replace already exists, it will be replaced.

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rules : typing.Sequence[PronunciationDictionaryRule]
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PronunciationDictionaryRulesResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.pronunciation_dictionaries.rules.add(
                pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
                rules=[
                    {
                        "string_to_replace": "string_to_replace",
                        "case_sensitive": True,
                        "word_boundaries": True,
                        "type": "alias",
                        "alias": "alias"
                    }
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().add)(
            pronunciation_dictionary_id, rules=rules, request_options=request_options
        )

    def remove(
        self,
        pronunciation_dictionary_id: str,
        *,
        rule_strings: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PronunciationDictionaryRulesResponseModel]:  # type: ignore[override]
        """
        Remove rules from the pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rule_strings : typing.Sequence[str]
            List of strings to remove from the pronunciation dictionary.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PronunciationDictionaryRulesResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.pronunciation_dictionaries.rules.remove(
                pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
                rule_strings=[
                    "rule_strings"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().remove)(
            pronunciation_dictionary_id,
            rule_strings=rule_strings,
            request_options=request_options,
        )


class AsyncRawRulesClient:
    """
    Async raw-response client for AsyncRulesClient.
    """

    def __init__(self, client: AsyncRulesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def set(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: List[
            BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRules1
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PronunciationDictionaryRulesResponseModel]:
        data = await AsyncRulesClient.set(
            self._client,
            pronunciation_dictionary_id,
            rules=rules,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def add(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: List[PronunciationDictionaryRule],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PronunciationDictionaryRulesResponseModel]:
        data = await AsyncRulesClient.add(
            self._client,
            pronunciation_dictionary_id,
            rules=rules,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def remove(
        self,
        pronunciation_dictionary_id: str,
        *,
        rule_strings: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PronunciationDictionaryRulesResponseModel]:
        data = await AsyncRulesClient.remove(
            self._client,
            pronunciation_dictionary_id,
            rule_strings=rule_strings,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
