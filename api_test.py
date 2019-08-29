# api_test.py
import requests

url = "https://api.genius.com/search?q=Kendrick%20Lamar"


my_headers = {
    "Authorization": "Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-"
}

response = requests.get(url, headers=my_headers)
print(response.text)
