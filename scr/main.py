import requests

url = "https://oe1me.wiremockapi.cloud/json/1"

res = requests.get(url)
data = res.json()

print(data)