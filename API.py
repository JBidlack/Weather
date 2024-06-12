import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('key')


def call(zip):
    response = requests.get('http://api.openweathermap.org/geo/1.0/zip?zip=21228,US&appid='+key)
    print(zip)
    print(response.content)