from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from .auth_utils import token_validator

class AuthenticatedUser(AnonymousUser):
    def __init__(self, username):
        self.username = username

    @property
    def is_authenticated(self):
        return True

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ")[1]

        try:
            decoded_token = token_validator.validate_token(token)

            # Extract user identifier (adjust this based on your JWT claims)
            user_id = decoded_token.get("sub", "unknown_user")

            # Return a custom authenticated user object
            user = AuthenticatedUser(username=user_id)

            return (user, decoded_token)
        except ValueError as e:
            raise AuthenticationFailed(str(e))
