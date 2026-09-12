from fyers_apiv3 import fyersModel
from dotenv import load_dotenv
import os

load_dotenv()

client_id =  os.getenv("CLIENT_ID")
secret_key = os.getenv("SECRET_KEY")
redirect_url =os.getenv("REDIRECT_URL") 
response_type = "code"
grant_type = "authorization_code"

auth_code = os.getenv("AUTH_CODE")


session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_url,
    response_type=response_type,
    grant_type=grant_type
)

session.set_token(auth_code)

response = session.generate_token()

print(response)