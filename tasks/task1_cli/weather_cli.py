#!/usr/bin/env python3
import sys
import os
from typing import List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from weatherlib import DEFAULT_CITIES, OpenWeatherMapProvider
from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
from weatherlib.weather import get_current_weather


def print_city(item):
    cond = item.get("condition")
    print(f"- {item['city']}, {item.get('country','')}: {cond}, "
          f"{item.get('temperature_c')}°C, humidity {item.get('humidity_percent')}%")


def main(args: List[str]):
    provider = OpenWeatherMapProvider()
    cities = random_cities(DEFAULT_CITIES, 5)
    print("Randomly selected cities:")
    print(", ".join(cities))
    items = fetch_cities_weather(cities, provider)
    print("\nCurrent weather:")
    for it in items:
        print_city(it)
    summary = summarize_cities(items)
    print("\nStats:")
    if summary["coldest"]:
        c = summary["coldest"]
        print(f"Coldest: {c['city']} ({c.get('temperature_c')}°C)")
    if summary["avg_temp_c"] is not None:
        print(f"Average temperature: {summary['avg_temp_c']:.1f}°C")

    try:
        q = input("\nEnter a city name to query (or just Enter to exit): ").strip()
    except EOFError:
        q = ""
    if q:
        res = get_current_weather(q, provider)
        if not res:
            print("City not found.")
        else:
            cond = res.get("condition")
            print(f"{res['city']}, {res.get('country','')}: {cond}, "
                  f"{res.get('temperature_c')}°C, humidity {res.get('humidity_percent')}%")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

