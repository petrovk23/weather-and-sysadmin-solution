from __future__ import annotations

from typing import Optional, Dict, Any
from .providers import OpenWeatherMapProvider


def geocode_city(name: str, provider: Optional[OpenWeatherMapProvider] = None) -> Optional[Dict[str, Any]]:
    provider = provider or OpenWeatherMapProvider()
    return provider.geocode(name)

