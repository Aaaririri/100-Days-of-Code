import requests
import datetime
"""
https://pixe.la/ 
you need to request your own username and password and your graph's name
"""
USERNAME = "aaaririri1"
PASSWORD = "senhatopzeira1"
params_pixela = {
    "token":PASSWORD, 
    "username":USERNAME, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
    }

#response = requests.post("https://pixe.la/v1/users", json = params_pixela)
GRAPHID = "graphbike"
params_graph = {
    "id":GRAPHID,
    "name":"Biking",
    "unit":"Km",
    "type":"float",
    "color":"momiji"
    }

graph_endpoint = "https://pixe.la/v1/users/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN":PASSWORD
}

#response = requests.post(url = graph_endpoint, json = params_graph, headers = headers)

today = datetime.datetime(datetime.date.today().year,datetime.date.today().month, datetime.date.today().day)

pixel_endpoint = "https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
pixel_params = {
    "date":today.strftime('%Y%m%d'),
    "quantity":"15"
}
#response = requests.post(url = pixel_endpoint, json = pixel_params, headers = headers)


update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{pixel_params['date']}"


delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{pixel_params['date']}"
#response = requests.delete(url = delete_endpoint, headers = headers)
