import requests
from twilio.rest import Client

account_sid = "abc123"  # Enter the account SID
auth_token = "abc123"  # Enter the auth token

API_KEY = "abc123"  # Enter the Twilio API key
# 1943 W Warner Ave, Chicago, IL 60613
MY_LAT = 41.956820  # Enter your latitude here
MY_LONG = -87.677890  # Enter your longitude here

PARAMETERS = {
    "lat": 41.0793,
    "lon": -85.1394,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

# Logic: Step through all weather data (by hour),
# for each hour go into the dict and grab the weather_id,
# check if each id is less than 700 (signifying rain based on the code descriptions online),
# then only take the first 12 entries for hours 0-12.
weather_condition_code = [hour["weather"][0]["id"] for hour in weather_data["hourly"] if hour["weather"][0]["id"] < 700][:12]  # save hours into a list
if weather_condition_code:  # if the condition code list isn't empty (ie there will be rain), then print "Bring and Umbrella"
    # print("Bring an Umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Bring an Umbrella ☔',
        from_='+###########',
        to='+###########'
    )

    print(message.status)



