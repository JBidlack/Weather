import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('key')


def call(zip):
    response = requests.get('http://api.openweathermap.org/geo/1.0/zip?zip='+ str(zip) + ',US&appid='+key)
    zipInfo = json.loads(response.text)
    lat = zipInfo["lat"]
    lon = zipInfo["lon"]
    print(lat)
    print(lon)
    print(key)

    weather = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid="+key)
    print(weather.text)