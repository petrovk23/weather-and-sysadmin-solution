from __future__ import annotations

from typing import Optional, Dict, Any
from .providers import OpenWeatherMapProvider


def get_current_weather(city: str, provider: Optional[OpenWeatherMapProvider] = None) -> Optional[Dict[str, Any]]:
    provider = provider or OpenWeatherMapProvider()
    geo = provider.geocode(city)
    if not geo:
        return None
    wx = provider.current_weather(geo["lat"], geo["lon"])
    return {
        "city": geo["name"],
        "country": geo.get("country"),
        "temperature_c": wx.get("temperature"),
        "humidity_percent": wx.get("humidity"),
        "condition": wx.get("condition"),
        "lat": geo["lat"],
        "lon": geo["lon"],
    }

