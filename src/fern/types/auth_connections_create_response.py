from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .o_auth_2_client_creds_response import OAuth2ClientCredsResponse
from .refresh_token_auth_response import RefreshTokenAuthResponse
from .basic_auth_response import BasicAuthResponse
from .bearer_auth_response import BearerAuthResponse
from .o_auth_2_jwt_response import OAuth2JwtResponse
from .private_key_jwt_response import PrivateKeyJwtResponse
from .mtls_auth_response import MtlsAuthResponse
from .custom_header_auth_response import CustomHeaderAuthResponse
from .api_integration_o_auth_2_auth_code_response import (
    ApiIntegrationOAuth2AuthCodeResponse,
)
from .api_integration_o_auth_2_custom_app_response import (
    ApiIntegrationOAuth2CustomAppResponse,
)
from .whats_app_auth_response import WhatsAppAuthResponse
from .slack_bot_auth_response import SlackBotAuthResponse
from .url_secret_auth_response import UrlSecretAuthResponse


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_Oauth2ClientCredentials(OAuth2ClientCredsResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_RefreshTokenAuth(RefreshTokenAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_BasicAuth(BasicAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_BearerAuth(BearerAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_Oauth2Jwt(OAuth2JwtResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_PrivateKeyJwt(PrivateKeyJwtResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_Mtls(MtlsAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_CustomHeaderAuth(CustomHeaderAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_ApiIntegrationOauth2AuthCode(
    ApiIntegrationOAuth2AuthCodeResponse
):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_ApiIntegrationOauth2CustomApp(
    ApiIntegrationOAuth2CustomAppResponse
):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_WhatsappAuth(WhatsAppAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_SlackBotAuth(SlackBotAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsCreateResponse
class AuthConnectionsCreateResponse_UrlSecret(UrlSecretAuthResponse):
    pass


# Union type for AuthConnectionsCreateResponse
# Pydantic will attempt to validate against each type in order
AuthConnectionsCreateResponse = Union[
    OAuth2ClientCredsResponse,
    RefreshTokenAuthResponse,
    BasicAuthResponse,
    BearerAuthResponse,
    OAuth2JwtResponse,
    PrivateKeyJwtResponse,
    MtlsAuthResponse,
    CustomHeaderAuthResponse,
    ApiIntegrationOAuth2AuthCodeResponse,
    ApiIntegrationOAuth2CustomAppResponse,
    WhatsAppAuthResponse,
    SlackBotAuthResponse,
    UrlSecretAuthResponse,
]
# TypeAdapter for runtime validation of AuthConnectionsCreateResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AuthConnectionsCreateResponse_adapter = TypeAdapter(AuthConnectionsCreateResponse)
