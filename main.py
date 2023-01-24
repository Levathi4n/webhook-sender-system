print("Created by Oxida")
import requests 

status = input("Status: ")
url = "" #webhook url

data = {
    "content" : "***From our Server***",
    "username" : "Information"
}

data["embeds"] = [
    {
        "description" : f"***Status: {status}***",
        "title" : "Result",
    }
]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
