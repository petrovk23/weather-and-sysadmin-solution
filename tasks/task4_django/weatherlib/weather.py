from .providers import OpenWeatherMapProvider


def get_current_weather(city: str, provider: OpenWeatherMapProvider | None = None):
    provider = provider or OpenWeatherMapProvider()
    g = provider.geocode(city)
    if not g:
        return None
    cw = provider.current_weather(g["lat"], g["lon"])
    return {
        "city": g["name"],
        "country": g.get("country"),
        "temperature_c": cw.get("temperature"),
        "humidity_percent": cw.get("humidity"),
        "condition": cw.get("condition"),
    }

