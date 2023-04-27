# ALWAYS UNDERSTAND AND READ THE DOCUMENTATION OF THE API THAT YOU ARE USING
import requests
from twilio.rest import Client

OWN_Endpoint = "http://api.openweathermap.org/date/2.5/onecall"
api_key = ""  # key you generate in api provider

account_sid = ""  # ID from twilio, create an account for this
auth_token = ""  # get it from twilio


weather_params = {
    "lat": 51.507351,
    "long": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It´s going to rain today, Remember to bring an umbrella",
    #     from="number twilio gives you",
    #     to="Your verified number"
    # )
    # I don't know why it does not work
