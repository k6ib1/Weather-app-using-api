import json
import requests


import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry


country = input("Enter a country: ")

base_url_geo = "https://geocoding-api.open-meteo.com/v1/search"
base_url_forecast = "https://api.open-meteo.com/v1/forecast"

# geo locates longitude and latitude through geolocation api (get request)

response_geo = requests.get(base_url_geo, params= {"name" : country, "count" : 1})
geo_info = response_geo.json()
result = geo_info["results"][0]

latitude = result["latitude"]
longitude = result["longitude"]



# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# long and lat requested now put in params

params = {
	"latitude": latitude,
	"longitude": longitude,
	"hourly": "temperature_2m",
}

response = openmeteo.weather_api(base_url_forecast, params = params)
# Process first location. Add a for-loop for multiple locations or weather models
response = response[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {
	"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)
}

hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print("\nHourly data\n", hourly_dataframe)