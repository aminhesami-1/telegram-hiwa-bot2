import requests
import json
import random

# url = "https://api2.ippanel.com/api/v1/sms/send/webservice/single"
url = "https://api2.ippanel.com/api/v1/sms/pattern/normal/send"

v_code = random.randint(1, 3)
# payload = json.dumps({
#   "recipient": [
#     # "09010971383",
#     "09024830315",
#   ],
#   "sender": "+983000505",
#   "message": "amin"
# })

payload = json.dumps(
    {
        "code": "bpgsf8m6zu",
        "sender": "+983000505",
        "recipient": "09024830315",
        "variable": {"amount": f"{v_code}"},
    }
)

headers = {
    "apikey": "F4nixrUXZG99qaDnMiqvG5Oyl5zlzYo8_8j1Vy5XZ3M=",
    "Content-Type": "application/json",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)