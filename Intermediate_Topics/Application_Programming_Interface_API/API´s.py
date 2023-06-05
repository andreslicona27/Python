# An Application Programming Interface is a set of commands, functions, protocols and objects
# that programmers can use to create software or interact with an external system.
from datetime import datetime

# API endpoint is the location of where the api

# RESPONSE CODES
# 1XX Hold on - something is happening, this is ot final
# 2XX Here you go - everything ok, you should have been getting the data
# 3XX Go away - you don't have permission
# 4XX You screwed up - the thing you are looking for might not even exist
# 5XX I screwed up - the server or website is down, or other problem

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)  # this returns the response code, not the json code

# httpstatues.com for all the possible errors you may have
if response.status_code != 404:
    raise Exception("That resource does not exist")

response.raise_for_status()  # does the same as the if, but for all the errors

data = response.json()["iss_position"]["longitude"]
data = response.json()["iss_position"]["latitude"]


# API PARAMETERS
MY_LAT = 51.507351
MY_LONG = -01.27758

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0  # depending on the number you, if is 0 or 1 would be the format you would get
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])  # gives only the hour of the sunrise
print(sunset.split("T")[1].split(":")[0])

# You can add them in here to
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

