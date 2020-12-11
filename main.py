import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

END_point = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "NONE"
lat ="NONE"
long = "NONE"




account_sid ='NONE'
auth_token = 'NONE'
client = Client(account_sid, auth_token)




params = {
    "lat": lat, "lon": long, "appid": api_key, "exclude": "current,daily,alerts, minutely"
}



response = requests.get(url=END_point, params=params)
response.raise_for_status()
data = response.json()
condition  = data["hourly"][0]["weather"][0]["id"]


if condition < 720 :
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"http": os.environ["http_proxy"]}
    message = client.messages \
        .create(
        body="It's raining.",
        from_='+NONE',
        to='+NONE'
    )
else:
    message = client.messages \
        .create(
        body="It's not raining .",
        from_='+NONE',
        to='+NONE'
    )




