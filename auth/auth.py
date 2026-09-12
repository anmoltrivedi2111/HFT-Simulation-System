from fyers_apiv3 import fyersModel
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
secret_key = os.getenv("SECRET_KEY")
redirect_url = os.getenv("REDIRECT_URL")

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_url,
    response_type="code",
    
)

response = session.generate_authcode()

print(response)