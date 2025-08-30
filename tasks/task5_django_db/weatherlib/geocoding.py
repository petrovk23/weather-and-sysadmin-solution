from .providers import OpenWeatherMapProvider


def geocode_city(name: str, provider: OpenWeatherMapProvider | None = None):
    provider = provider or OpenWeatherMapProvider()
    return provider.geocode(name)

