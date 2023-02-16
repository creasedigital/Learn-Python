import requests

url = "https://goal.com/en-gb"

res = requests.get(url)

print(res.status_code)
print(res.headers)

print(res)
# print(res.text)
