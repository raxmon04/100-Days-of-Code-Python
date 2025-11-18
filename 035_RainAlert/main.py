import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY") # export OWM_API_KEY =382110248420a5ca23f272a4dd677518 in der Konsole
auth_token = os.environ.get("AUTH_TOKEN") # export AUTH_TOKEN=982e5120f26355c875518c4a359b06e3 in der Konsole

client = Client(account_sid, auth_token)

weather_params = {
    "lat": 47.050167,
    "lon": 8.309307,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umberella",
        from_="+12175823677",
        to="+41764490912",
    )
    print(message.status)