from __future__ import annotations

from django.shortcuts import render, redirect
from django.http import HttpResponse

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weatherlib import DEFAULT_CITIES, OpenWeatherMapProvider
from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
from weatherlib.weather import get_current_weather

from .models import Snapshot, WeatherRecord
from collections import Counter



def index(request):
    # Show empty page by default. Only show latest snapshot when explicitly requested
    # via query parameter ?show=1 (set after a Refresh).
    records = []
    if request.GET.get('show') == '1':
        snap = Snapshot.objects.order_by('-created_at').first()
        if snap:
            records = WeatherRecord.objects.filter(snapshot=snap).order_by('city')

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

    response = render(request, 'weatherapp5/index.html', {'records': records, 'summary': summary})
    # Prevent browser from showing cached content when navigating back
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


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
    # After refreshing, show latest once using query parameter
    from django.urls import reverse
    return redirect(reverse('index') + '?show=1')


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
    response = render(request, 'weatherapp5/search.html', {'q': q, 'res': res})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


def compare(request):
    city = request.GET.get('city', '').strip()
    latest = WeatherRecord.objects.filter(city=city).order_by('-created_at')[:10]
    latest = list(reversed(list(latest)))
    # Count conditions across the last 10 for a simple categorical comparison
    cond_counts = Counter((r.condition or 'Unknown') for r in latest)
    cond_labels = list(cond_counts.keys())
    cond_values = [cond_counts[k] for k in cond_labels]
    # Assign distinct, stable colors per condition label
    palette = [
        '#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f',
        '#edc949', '#af7aa1', '#ff9da7', '#9c755f', '#bab0ab'
    ]
    cond_colors = [palette[i % len(palette)] for i, _ in enumerate(cond_labels)]
    return render(request, 'weatherapp5/compare.html', {
        'city': city,
        'records': latest,
        'cond_labels': cond_labels,
        'cond_values': cond_values,
        'cond_colors': cond_colors,
    })
