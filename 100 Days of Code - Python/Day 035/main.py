import requests
# https://openweathermap.org/api/one-call-api
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "75d37a132b8a6a6c40a9b501ce8e98a1"
params = {
    "lat": -22.4256,
    "lon": -45.4528,
    "exclude":"current,minutely,daily",
    "appid": api_key,
}
response = requests.get(OWM_endpoint, params= params)
response.raise_for_status()
weather_data = response.json()
check = 0
weather_slice = weather_data["hourly"][:12]
for i in range(0, 12):
    data = weather_slice[i]["weather"][0]["id"]
    if data < 700:
        print("Bring an Umbrella")
        break

    


    

