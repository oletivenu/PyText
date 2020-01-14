import twilio
from twilio.rest import Client

account_sid = "AC172778d91f77c5273a039b3e040061f2"
auth_token = "9ac56e329bd99040a6db94a674bcfc27"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="+919000634141",
    from_="+13367542080",
    body="Hello, how are you"
)
