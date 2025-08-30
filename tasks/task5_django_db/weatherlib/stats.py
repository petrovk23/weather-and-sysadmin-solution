from __future__ import annotations

import random
from typing import List, Dict, Any

from .providers import OpenWeatherMapProvider


def fetch_cities_weather(cities: List[str], provider: OpenWeatherMapProvider | None = None) -> List[Dict[str, Any]]:
    provider = provider or OpenWeatherMapProvider()
    results = []
    for name in cities:
        try:
            g = provider.geocode(name)
            if not g:
                continue
            cw = provider.current_weather(g["lat"], g["lon"])
            results.append({
                "city": g["name"],
                "country": g.get("country"),
                "temperature_c": cw.get("temperature"),
                "humidity_percent": cw.get("humidity"),
                "condition": cw.get("condition"),
                "weather_code": cw.get("weather_code"),
            })
        except Exception:
            continue
    return results


def random_cities(source: List[str], n: int = 5) -> List[str]:
    n = min(n, len(source))
    return random.sample(source, n)


def summarize_cities(items: List[Dict[str, Any]]):
    if not items:
        return {"coldest": None, "avg_temp_c": None}
    coldest = min(items, key=lambda x: (x.get("temperature_c") is None, x.get("temperature_c")))
    temps = [x.get("temperature_c") for x in items if isinstance(x.get("temperature_c"), (int, float))]
    avg = sum(temps) / len(temps) if temps else None
    return {"coldest": coldest, "avg_temp_c": avg}

