from __future__ import annotations

import os
import requests
from typing import Dict, Any, Optional


class WeatherProvider:
    def geocode(self, city: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    def current_weather(self, lat: float, lon: float) -> Dict[str, Any]:
        raise NotImplementedError


class OpenWeatherMapProvider(WeatherProvider):
    GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"
    CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("OPENWEATHERMAP_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "OpenWeatherMapProvider requires OPENWEATHERMAP_API_KEY to be set"
            )

    def geocode(self, city: str) -> Optional[Dict[str, Any]]:
        params = {"q": city, "limit": 1, "appid": self.api_key}
        resp = requests.get(self.GEO_URL, params=params)
        resp.raise_for_status()
        data = resp.json() or []
        if not data:
            return None
        r0 = data[0]
        return {
            "name": r0.get("name"),
            "lat": r0.get("lat"),
            "lon": r0.get("lon"),
            "country": r0.get("country"),
        }

    def current_weather(self, lat: float, lon: float) -> Dict[str, Any]:
        params = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        resp = requests.get(self.CURRENT_URL, params=params)
        resp.raise_for_status()
        data = resp.json() or {}
        main = data.get("main", {})
        wx0 = (data.get("weather") or [{}])[0]
        return {
            "temperature": main.get("temp"),
            "humidity": main.get("humidity"),
            "condition": wx0.get("description") or wx0.get("main"),
            "weather_code": wx0.get("id"),
        }

