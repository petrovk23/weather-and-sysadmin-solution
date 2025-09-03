from __future__ import annotations

import os
import sys
from flask import Flask, render_template, request, redirect, url_for, make_response

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from weatherlib import DEFAULT_CITIES, OpenWeatherMapProvider
from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
from weatherlib.weather import get_current_weather


app = Flask(__name__)


@app.route("/")
def index():
    # Empty by default; only fetch when user explicitly refreshes
    items = []
    summary = None
    if request.args.get("refresh") == "1":
        try:
            provider = OpenWeatherMapProvider()
        except Exception:
            return "OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", 500
        cities = random_cities(DEFAULT_CITIES, 5)
        items = fetch_cities_weather(cities, provider)
        summary = summarize_cities(items)
    resp = make_response(render_template("index.html", items=items, summary=summary))
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp


@app.route("/search", methods=["POST"]) 
def search():
    q = request.form.get("q", "").strip()
    if not q:
        # Show not-found the same way as Task 5 even for empty query
        resp = make_response(render_template("search.html", q=q, res=None))
        resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        return resp
    try:
        provider = OpenWeatherMapProvider()
    except Exception:
        return "OPENWEATHERMAP_API_KEY липсва или е невалиден. Добавете го в .env и рестартирайте.", 500
    res = get_current_weather(q, provider)
    resp = make_response(render_template("search.html", q=q, res=res))
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp


if __name__ == "__main__":
    app.run(debug=True, port=5001)
