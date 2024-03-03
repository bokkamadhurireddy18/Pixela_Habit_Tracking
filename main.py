import requests
import os
from datetime import date

#1. create user
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url= pixela_endpoint, json= user_params)
#print(response.text)

#2. create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response= requests.post(url= graph_endpoint, json= graph_params, headers=headers)
# print(response.text)

#3. create distance cycled today
today= date.today()
graph_value_post= f"{graph_endpoint}/{graph_params["id"]}"
graph_value = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20.20"
}
# response= requests.post(url= graph_value_post, json=graph_value, headers=headers)
# print(response.text)

#4. update a pixel in the graph
#lets say I've cycled only 4 km, instead of 20.20
graph_value_update= f"{graph_value_post}/{graph_value["date"]}"
update_value = {
    "quantity": "4.25"
}
# response= requests.put(url= graph_value_update, json=update_value, headers=headers)
# print(response.text)

#5. delete a pixel from the graph
# response= requests.delete(url= graph_value_update, headers=headers)
# print(response.text)