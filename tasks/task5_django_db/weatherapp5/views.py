from __future__ import annotations

from django.shortcuts import render, redirect
from django.http import HttpResponse

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weatherlib import DEFAULT_CITIES, OpenWeatherMapProvider
from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
from weatherlib.weather import get_current_weather

from .models import Snapshot, WeatherRecord



def index(request):
    snap = Snapshot.objects.order_by('-created_at').first()
    records = WeatherRecord.objects.filter(snapshot=snap).order_by('city') if snap else []
    summary = None
    if records:
        items = [{
            'city': r.city,
            'country': r.country,
            'temperature_c': r.temperature_c,
            'humidity_percent': r.humidity_percent,
            'condition': r.condition,
        } for r in records]
        summary = summarize_cities(items)
    return render(request, 'weatherapp5/index.html', {'records': records, 'summary': summary})


def refresh(request):
    try:
        provider = OpenWeatherMapProvider()
    except Exception:
        return HttpResponse("OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", status=500)
    cities = random_cities(DEFAULT_CITIES, 5)
    items = fetch_cities_weather(cities, provider)
    snap = Snapshot.objects.create()
    for it in items:
        WeatherRecord.objects.create(
            snapshot=snap,
            city=it['city'],
            country=it.get('country'),
            temperature_c=it.get('temperature_c'),
            humidity_percent=it.get('humidity_percent'),
            condition=it.get('condition'),
        )
    return redirect('index')


def search(request):
    q = request.GET.get('q', '').strip()
    if not q:
        res = None
    else:
        try:
            provider = OpenWeatherMapProvider()
        except Exception:
            return HttpResponse("OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", status=500)
        res = get_current_weather(q, provider)
    return render(request, 'weatherapp5/search.html', {'q': q, 'res': res})


def compare(request):
    city = request.GET.get('city', '').strip()
    latest = WeatherRecord.objects.filter(city=city).order_by('-created_at')[:10]
    latest = list(reversed(list(latest)))
    return render(request, 'weatherapp5/compare.html', {'city': city, 'records': latest})
