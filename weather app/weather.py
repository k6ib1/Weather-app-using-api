import json
import requests


import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry



def fetch_weather_data(country):
    response_geo = requests.get(
        base_url_geo,
        params={"name": country, "count": 1}
    )

    geo_info = response_geo.json()
    result = geo_info["results"][0]

    latitude = result["latitude"]
    longitude = result["longitude"]

    # Setup Open-Meteo API client
    cache_session = requests_cache.CachedSession(
        ".cache",
        expire_after=3600
    )

    retry_session = retry(
        cache_session,
        retries=5,
        backoff_factor=0.2
    )

    openmeteo = openmeteo_requests.Client(
        session=retry_session
    )

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
    }

    response = openmeteo.weather_api(
        base_url_forecast,
        params=params
    )

    response = response[0]

    # Process hourly data
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(
                hourly.Time(),
                unit="s",
                utc=True
            ),
            end=pd.to_datetime(
                hourly.TimeEnd(),
                unit="s",
                utc=True
            ),
            freq=pd.Timedelta(
                seconds=hourly.Interval()
            ),
            inclusive="left"
        )
    }

    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data=hourly_data)

    return {
        "latitude": response.Latitude(),
        "longitude": response.Longitude(),
        "elevation": response.Elevation(),
        "timezone_offset": response.UtcOffsetSeconds(),
        "hourly": hourly_dataframe
    }


base_url_geo = "https://geocoding-api.open-meteo.com/v1/search"
base_url_forecast = "https://api.open-meteo.com/v1/forecast"




