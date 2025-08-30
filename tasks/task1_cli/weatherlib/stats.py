from __future__ import annotations

import random
from typing import List, Dict, Any

from .providers import OpenWeatherMapProvider


def fetch_cities_weather(cities: List[str], provider: OpenWeatherMapProvider | None = None) -> List[Dict[str, Any]]:
    provider = provider or OpenWeatherMapProvider()
    results = []
    for name in cities:
        try:
            geo = provider.geocode(name)
            if not geo:
                continue
            cur = provider.current_weather(geo["lat"], geo["lon"])
            results.append({
                "city": geo["name"],
                "country": geo.get("country"),
                "temperature_c": cur.get("temperature"),
                "humidity_percent": cur.get("humidity"),
                "condition": cur.get("condition"),
                "weather_code": cur.get("weather_code"),
                "lat": geo["lat"],
                "lon": geo["lon"],
            })
        except Exception:
            continue
    return results


def random_cities(source: List[str], n: int = 5) -> List[str]:
    n = min(n, len(source))
    return random.sample(source, n)


def summarize_cities(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not items:
        return {"coldest": None, "avg_temp_c": None}
    coldest = min(items, key=lambda x: (x.get("temperature_c") is None, x.get("temperature_c")))
    temps = [x.get("temperature_c") for x in items if isinstance(x.get("temperature_c"), (int, float))]
    avg = sum(temps) / len(temps) if temps else None
    return {"coldest": coldest, "avg_temp_c": avg}

