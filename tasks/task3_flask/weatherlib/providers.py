from __future__ import annotations

import os
import requests


class OpenWeatherMapProvider:
    GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"
    CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str | None = None) -> None:
        import os
        self.api_key = api_key or os.getenv("OPENWEATHERMAP_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENWEATHERMAP_API_KEY not set")

    def geocode(self, city: str):
        r = requests.get(self.GEO_URL, params={"q": city, "limit": 1, "appid": self.api_key})
        r.raise_for_status()
        arr = r.json() or []
        if not arr:
            return None
        x = arr[0]
        return {"name": x.get("name"), "lat": x.get("lat"), "lon": x.get("lon"), "country": x.get("country")}

    def current_weather(self, lat: float, lon: float):
        r = requests.get(self.CURRENT_URL, params={"lat": lat, "lon": lon, "units": "metric", "appid": self.api_key})
        r.raise_for_status()
        d = r.json() or {}
        main = d.get("main", {})
        wx0 = (d.get("weather") or [{}])[0]
        return {"temperature": main.get("temp"), "humidity": main.get("humidity"), "condition": wx0.get("description"), "weather_code": wx0.get("id")}

