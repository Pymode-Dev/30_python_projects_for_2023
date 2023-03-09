"""
The python script that handles api query
"""

import requests

from access_api_key import parse_api_key


BASE_URL: str = "https://api.openweathermap.org/data/2.5/weather"


def build_url(city: list, metrics=False) -> str:
    parse_city: str = "+".join(city) if len(city) > 1 else "".join(city)
    api_key: str = f"{parse_api_key()}"
    units: str = "imperial" if metrics else "metric"
    url: str = f"{BASE_URL}?q={parse_city}&appid={api_key}&units={units}"

    return url


def query_api(url: str) -> dict:
    result = requests.get(url)
    return result.json()
