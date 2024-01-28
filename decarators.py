import requests
from requests import RequestException
import time

API_KEY ="QWZ3TM6ZTDWLH43WN5BZFQ4LE"


def retry(func):
    def wrapper_rety(*args, **kwargs):
        retries = [5, 30]
        for seconds in retries:
            try:
                return func(*args, **kwargs)
            except RequestException:
                print(f"Failed to get data. Retrying in {seconds} seconds")
                time.sleep(seconds)
        return func(*args, **kwargs)
    
    
@retry
def get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?key={API_KEY}"
    response = requests.get(url)
    weather_by_days = response.json()["days"]
    weather_by_hours = weather_by_days[0]["hours"]
    return weather_by_hours


def farenhate_to_selsius(*, farenhate: float) -> int:
    return round((farenhate - 32) * 5 / 9)


def got_dangerous_hours(*, wearher_by_hour: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in wearher_by_hour:
        uvindex = weather["uvindex"]
        time = weather["datetime"]
        celsius = farenhate_to_selsius(farenhate = weather["temp"])
        if uvindex <= 3:
            dangerous_hours.append({"datetime": time, "uvindex": uvindex, "temperature": celsius})
            
    return dangerous_hours
    
date = "2024-01-18"
city = "London, UK"    

weather_by_hour = get_weather_by_hours_for_day_from_api(date=date, city=city)
dangerous_hours = got_dangerous_hours(wearher_by_hour = weather_by_hour)
print(dangerous_hours)
print(weather_by_hour)