from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .create_o_auth_2_client_creds_request import CreateOAuth2ClientCredsRequest
from .create_custom_header_auth_request import CreateCustomHeaderAuthRequest
from .create_basic_auth_request import CreateBasicAuthRequest
from .create_bearer_auth_request import CreateBearerAuthRequest
from .create_o_auth_2_jwt_request import CreateOAuth2JwtRequest
from .create_private_key_jwt_request import CreatePrivateKeyJwtRequest
from .create_mtls_auth_request import CreateMtlsAuthRequest


# fernMode variant type for a shared-component member of AuthConnectionsCreateRequestBody
class AuthConnectionsCreateRequestBody_Oauth2ClientCredentials(
    CreateOAuth2ClientCredsRequest
):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateRequestBody
class AuthConnectionsCreateRequestBody_CustomHeaderAuth(CreateCustomHeaderAuthRequest):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateRequestBody
class AuthConnectionsCreateRequestBody_BasicAuth(CreateBasicAuthRequest):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateRequestBody
class AuthConnectionsCreateRequestBody_BearerAuth(CreateBearerAuthRequest):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateRequestBody
class AuthConnectionsCreateRequestBody_Oauth2Jwt(CreateOAuth2JwtRequest):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateRequestBody
class AuthConnectionsCreateRequestBody_PrivateKeyJwt(CreatePrivateKeyJwtRequest):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateRequestBody
class AuthConnectionsCreateRequestBody_Mtls(CreateMtlsAuthRequest):
    pass


# Union type for AuthConnectionsCreateRequestBody
# Pydantic will attempt to validate against each type in order
AuthConnectionsCreateRequestBody = Union[
    CreateOAuth2ClientCredsRequest,
    CreateCustomHeaderAuthRequest,
    CreateBasicAuthRequest,
    CreateBearerAuthRequest,
    CreateOAuth2JwtRequest,
    CreatePrivateKeyJwtRequest,
    CreateMtlsAuthRequest,
]
# TypeAdapter for runtime validation of AuthConnectionsCreateRequestBody
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AuthConnectionsCreateRequestBody_adapter = TypeAdapter(AuthConnectionsCreateRequestBody)
