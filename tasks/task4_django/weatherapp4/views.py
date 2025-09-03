from __future__ import annotations

from django.shortcuts import render, redirect
from django.http import HttpResponse

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weatherlib import DEFAULT_CITIES, OpenWeatherMapProvider
from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
from weatherlib.weather import get_current_weather



def index(request):
    # Empty by default; only fetch on explicit refresh
    items, summary = [], None
    if request.GET.get('refresh') == '1':
        try:
            provider = OpenWeatherMapProvider()
        except Exception as e:
            return HttpResponse("OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", status=500)
        cities = random_cities(DEFAULT_CITIES, 5)
        items = fetch_cities_weather(cities, provider)
        summary = summarize_cities(items)
    resp = render(request, 'weatherapp4/index.html', {'items': items, 'summary': summary})
    resp["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp["Pragma"] = "no-cache"
    resp["Expires"] = "0"
    return resp


def search(request):
    q = request.GET.get('q', '').strip()
    if not q:
        res = None
        resp = render(request, 'weatherapp4/search.html', {'q': q, 'res': res})
        resp["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        resp["Pragma"] = "no-cache"
        resp["Expires"] = "0"
        return resp
    try:
        provider = OpenWeatherMapProvider()
    except Exception:
        return HttpResponse("OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", status=500)
    res = get_current_weather(q, provider)
    resp = render(request, 'weatherapp4/search.html', {'q': q, 'res': res})
    resp["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp["Pragma"] = "no-cache"
    resp["Expires"] = "0"
    return resp
