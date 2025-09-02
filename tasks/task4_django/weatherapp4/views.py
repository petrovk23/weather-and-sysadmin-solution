from __future__ import annotations

from django.shortcuts import render, redirect
from django.http import HttpResponse

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weatherlib import DEFAULT_CITIES, OpenWeatherMapProvider
from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
from weatherlib.weather import get_current_weather



def index(request):
    try:
        provider = OpenWeatherMapProvider()
    except Exception as e:
        return HttpResponse("OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", status=500)
    cities = random_cities(DEFAULT_CITIES, 5)
    items = fetch_cities_weather(cities, provider)
    summary = summarize_cities(items)
    return render(request, 'weatherapp4/index.html', {'items': items, 'summary': summary})


def search(request):
    q = request.GET.get('q', '').strip()
    if not q:
        return redirect('index')
    try:
        provider = OpenWeatherMapProvider()
    except Exception:
        return HttpResponse("OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", status=500)
    res = get_current_weather(q, provider)
    return render(request, 'weatherapp4/search.html', {'q': q, 'res': res})
