from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .update_o_auth_2_client_creds_request import UpdateOAuth2ClientCredsRequest
from .update_basic_auth_request import UpdateBasicAuthRequest
from .update_bearer_auth_request import UpdateBearerAuthRequest
from .update_o_auth_2_jwt_request import UpdateOAuth2JwtRequest


# fernMode variant type for a shared-component member of AuthConnectionsUpdateRequestBody
class AuthConnectionsUpdateRequestBody_Oauth2ClientCredentials(
    UpdateOAuth2ClientCredsRequest
):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateRequestBody
class AuthConnectionsUpdateRequestBody_BasicAuth(UpdateBasicAuthRequest):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateRequestBody
class AuthConnectionsUpdateRequestBody_BearerAuth(UpdateBearerAuthRequest):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateRequestBody
class AuthConnectionsUpdateRequestBody_Oauth2Jwt(UpdateOAuth2JwtRequest):
    pass


# Union type for AuthConnectionsUpdateRequestBody
# Pydantic will attempt to validate against each type in order
AuthConnectionsUpdateRequestBody = Union[
    UpdateOAuth2ClientCredsRequest,
    UpdateBasicAuthRequest,
    UpdateBearerAuthRequest,
    UpdateOAuth2JwtRequest,
]
# TypeAdapter for runtime validation of AuthConnectionsUpdateRequestBody
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AuthConnectionsUpdateRequestBody_adapter = TypeAdapter(AuthConnectionsUpdateRequestBody)
