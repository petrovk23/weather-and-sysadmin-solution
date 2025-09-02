from __future__ import annotations

import os
import sys
from flask import Flask, render_template, request, redirect, url_for

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from weatherlib import DEFAULT_CITIES, OpenWeatherMapProvider
from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
from weatherlib.weather import get_current_weather


app = Flask(__name__)


@app.route("/")
def index():
    try:
        provider = OpenWeatherMapProvider()
    except Exception:
        return "OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", 500
    cities = random_cities(DEFAULT_CITIES, 5)
    items = fetch_cities_weather(cities, provider)
    summary = summarize_cities(items)
    return render_template("index.html", items=items, summary=summary)


@app.route("/search", methods=["POST"]) 
def search():
    q = request.form.get("q", "").strip()
    if not q:
        return redirect(url_for("index"))
    try:
        provider = OpenWeatherMapProvider()
    except Exception:
        return "OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", 500
    res = get_current_weather(q, provider)
    return render_template("search.html", q=q, res=res)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
