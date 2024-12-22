from fastapi import FastAPI, Depends
from auth.jwt_auth_handler import JWTAuthHandler
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI application
app = FastAPI(title="FastAPI", version="0.0.1", openapi_url="/api/v1/openapi.json")

# Initialize JWTAuthHandler with environment variables
jwt_bearer = JWTAuthHandler(
    audience=os.getenv("CLIENT_ID"),
    authority_url=os.getenv("AuthorityUrl"),
    jwks_url=os.getenv("JwtKeyUrl"),
    local_testing=False
)

@app.get(path="/secure", dependencies=[Depends(jwt_bearer)])
def secure_endpoint():
    return {'hello': 'secure'}

@app.get(path="/")
def public_endpoint():
    return {'hello': 'not secure'}