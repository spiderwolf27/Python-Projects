import json
import time
import hashlib
import hmac
import base64
import uuid
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Declare empty header dictionary
apiHeader = {}
# open token
token = os.getenv('SWITCHBOT_API_KEY')  # load from .env file
# secret key
secret = os.getenv('SWITCHBOT_SECRET_KEY')  # load from .env file
nonce = uuid.uuid4()
t = int(round(time.time() * 1000))
string_to_sign = '{}{}{}'.format(token, t, nonce)

string_to_sign = bytes(string_to_sign, 'utf-8')
secret = bytes(secret, 'utf-8')

sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
print('Authorization: {}'.format(token))
print('t: {}'.format(t))
print('sign: {}'.format(str(sign, 'utf-8')))
print('nonce: {}'.format(nonce))

# Build api header JSON
apiHeader['Authorization'] = token
apiHeader['Content-Type'] = 'application/json'
apiHeader['charset'] = 'utf8'
apiHeader['t'] = str(t)
apiHeader['sign'] = str(sign, 'utf-8')
apiHeader['nonce'] = str(nonce)

def generate_api_header():
    return apiHeader

if __name__ == "__main__":
    print("Generated API Header:", apiHeader)  # Debugging line
print("this was the get-token.py")
print("=====================================")