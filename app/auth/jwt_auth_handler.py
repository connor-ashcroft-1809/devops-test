from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt import PyJWKClient
from typing import Optional

class JWTAuthHandler(HTTPBearer):
    """JWT Authentication for FastAPI."""
    def __init__(self, audience: str, authority_url: str, jwks_url: str, local_testing: bool = False):
        super().__init__(auto_error=True)
        self.audience = audience
        self.authority_url = authority_url
        self.jwks_url = jwks_url
        self.local_testing = local_testing
        self.jwks_client = PyJWKClient(self.jwks_url)

    async def __call__(self, request: Request) -> str:
        """Handle incoming requests and validate JWT."""
        if self.local_testing:
            return "test_token"  # Simplified local testing token

        credentials: Optional[HTTPAuthorizationCredentials] = await super().__call__(request)
        if not credentials or credentials.scheme != "Bearer":
            raise HTTPException(status_code=403, detail="Invalid or missing token scheme.")

        return self._validate_jwt(credentials.credentials)

    def _validate_jwt(self, token: str) -> str:
        """Validate JWT and return the payload."""
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token)
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=self.audience,
                issuer=self.authority_url,
                options={
                    "verify_signature": True,
                    "verify_exp": True,
                    "verify_nbf": True,
                    "verify_iat": True,
                    "verify_aud": True,
                    "verify_iss": True,
                },
            )
            return payload
        except jwt.PyJWTError as e:
            raise HTTPException(status_code=403, detail="Invalid or expired token.") from e
