"""
change info set with MY_ to your own info or set your own environment variables for this variables
"""
APP_ID = MY_APP_ID
API_KEY = MY_API_KEY

import requests
from datetime import datetime

GENDER = MY_GENDER
WEIGHT_KG = MY_WEIGHT_KG
HEIGHT_CM = MY_HEIGHT_CM
AGE = MY_AGE

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
text = input("Tell me which exercises you did: ")
api_params = {
    "query":text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age":AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


response = requests.post(url = endpoint, json  = api_params, headers = headers)
data = response.json()


#today = datetime.datetime(datetime.date.today().year,datetime.date.today().month, datetime.date.today().day)
#today_date = today.strftime('%Y%m%d')
#today_time = today.strftime("%X")

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

sheety_endpoint = "https://api.sheety.co/d2ccf30f76084afe96e8da0ee8c275aa/myWorkouts/workouts"

for exercise in data["exercises"]:
    sheety_params = {
        "workout": {
            "date":today_date,
            "time":today_time,
            "exercise":exercise["name"].title(),	
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(sheety_endpoint, json=sheety_params)
    print(sheety_response.text)
    
"""
diferent types of autentication 
#No Authentication  
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
  
#Basic Authentication
sheet_response = requests.post(
  sheet_endpoint, 
  json=sheet_inputs, 
  auth=(
      YOUR USERNAME, 
      YOUR PASSWORD,
  )
)

#Bearer Token Authentication
bearer_headers = {
"Authorization": "Bearer YOUR_TOKEN"
}
sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)
"""