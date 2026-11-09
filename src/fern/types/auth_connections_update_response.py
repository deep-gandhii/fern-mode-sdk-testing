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


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_Oauth2ClientCredentials(OAuth2ClientCredsResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_RefreshTokenAuth(RefreshTokenAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_BasicAuth(BasicAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_BearerAuth(BearerAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_Oauth2Jwt(OAuth2JwtResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_PrivateKeyJwt(PrivateKeyJwtResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_Mtls(MtlsAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_CustomHeaderAuth(CustomHeaderAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_ApiIntegrationOauth2AuthCode(
    ApiIntegrationOAuth2AuthCodeResponse
):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_ApiIntegrationOauth2CustomApp(
    ApiIntegrationOAuth2CustomAppResponse
):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_WhatsappAuth(WhatsAppAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_SlackBotAuth(SlackBotAuthResponse):
    pass


# fernMode variant type for a shared-component member of AuthConnectionsUpdateResponse
class AuthConnectionsUpdateResponse_UrlSecret(UrlSecretAuthResponse):
    pass


# Union type for AuthConnectionsUpdateResponse
# Pydantic will attempt to validate against each type in order
AuthConnectionsUpdateResponse = Union[
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
# TypeAdapter for runtime validation of AuthConnectionsUpdateResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AuthConnectionsUpdateResponse_adapter = TypeAdapter(AuthConnectionsUpdateResponse)
