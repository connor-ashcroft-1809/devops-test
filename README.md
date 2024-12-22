# fastapi-w-oauth2
A repository with a basic "template" to create a FastApi with Oauth2, clone this repository and add endpoint to main.py


Steps:

create the following .env file

CLIENT_ID = {{client_id}}
TENANT_ID = {{tenant_id}}
AuthorityUrl = "https://login.microsoftonline.com/{{tenant_id}}/v2.0"
JwtKeyUrl = "https://login.microsoftonline.com/common/discovery/keys"

#used to gain access token, not  required for securing FastAPI
#Access Token url = "https://login.microsoftonline.com/{{TENANT_ID}}/oauth2/v2.0/token"