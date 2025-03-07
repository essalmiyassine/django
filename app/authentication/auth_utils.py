import jwt
from jwt import PyJWKClient
from django.conf import settings

jwk_uri = settings.OAUTH2_JWKS_URI
audience = settings.OAUTH2_AUDIENCE

class OAuth2TokenValidator:
    def __init__(self):
        self.jwks_client = PyJWKClient(jwk_uri)

    def get_public_key(self, token):
        signing_key = self.jwks_client.get_signing_key_from_jwt(token)
        return signing_key.key

    def validate_token(self, token):
        try:
            public_key = self.get_public_key(token)
            decoded_token = jwt.decode(
                token,
                public_key,
                algorithms=["RS256"],  # Ensure this matches your provider
                audience=audience,
                options={"verify_exp": True}
            )
            return decoded_token  # Return claims if valid
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")

token_validator = OAuth2TokenValidator()
