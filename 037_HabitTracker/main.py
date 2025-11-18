import requests
from datetime import datetime

USERNAME = "raxmon04"
TOKEN = "hw1qAKM0MAqdgQgjc8TA9"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Workout Graph",
#     "unit": "Min",
#     "type": "float",
#     "color": "ajisai",
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# any_day = datetime(year=2025, month=11, day=7)

post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "240",
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response.text)