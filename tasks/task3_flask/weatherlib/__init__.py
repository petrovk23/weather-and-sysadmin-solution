try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

from .geocoding import geocode_city
from .weather import get_current_weather
from .stats import summarize_cities
from .cities import DEFAULT_CITIES
from .providers import OpenWeatherMapProvider

__all__ = [
    "geocode_city",
    "get_current_weather",
    "summarize_cities",
    "DEFAULT_CITIES",
    "OpenWeatherMapProvider",
]

