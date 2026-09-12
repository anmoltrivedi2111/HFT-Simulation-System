from fyers_apiv3 import fyersModel
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")

access_tokens = os.getenv("ACCESS_TOKENS")

fyers = fyersModel.FyersModel(
    client_id=client_id,
    token=access_tokens
)

response = fyers.quotes({"symbols":"NSE:SBIN-EQ"})

print(response)