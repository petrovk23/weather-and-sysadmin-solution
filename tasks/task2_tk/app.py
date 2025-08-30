#!/usr/bin/env python3
import argparse
import threading
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from weatherlib import DEFAULT_CITIES, OpenWeatherMapProvider
from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
from weatherlib.weather import get_current_weather


class App:
    def __init__(self):
        import tkinter as tk
        from tkinter import ttk

        self.root = tk.Tk()
        self.root.title("Weather – Task 2 (Tkinter)")
        self.root.geometry("700x420")
        self.provider = OpenWeatherMapProvider()

        top = ttk.Frame(self.root)
        top.pack(fill=tk.X, padx=10, pady=10)

        self.refresh_btn = ttk.Button(top, text="Refresh (5 random cities)", command=self.refresh)
        self.refresh_btn.pack(side=tk.LEFT)

        ttk.Label(top, text="  Search city:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(top, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_btn = ttk.Button(top, text="Go", command=self.search_city)
        self.search_btn.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self.root, columns=("city", "condition", "temp", "humidity"), show="headings")
        self.tree.heading("city", text="City")
        self.tree.heading("condition", text="Condition")
        self.tree.heading("temp", text="Temp (°C)")
        self.tree.heading("humidity", text="Humidity (%)")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.stats_var = tk.StringVar(value="")
        ttk.Label(self.root, textvariable=self.stats_var).pack(pady=(0, 10))

        self.refresh()

    def set_loading(self, loading: bool):
        import tkinter as tk
        state = tk.DISABLED if loading else tk.NORMAL
        self.refresh_btn.configure(state=state)
        self.search_btn.configure(state=state)
        self.search_entry.configure(state=state)

    def refresh(self):
        import tkinter as tk
        from tkinter import messagebox

        def work():
            try:
                cities = random_cities(DEFAULT_CITIES, 5)
                items = fetch_cities_weather(cities, self.provider)
                self.tree.delete(*self.tree.get_children())
                for it in items:
                    self.tree.insert("", tk.END, values=(
                        f"{it['city']}, {it.get('country','')}",
                        it.get("condition"),
                        it.get("temperature_c"),
                        it.get("humidity_percent"),
                    ))
                s = summarize_cities(items)
                if s["coldest"] and s["avg_temp_c"] is not None:
                    self.stats_var.set(
                        f"Coldest: {s['coldest']['city']} ({s['coldest']['temperature_c']}°C) • "
                        f"Average: {s['avg_temp_c']:.1f}°C"
                    )
                else:
                    self.stats_var.set("No data.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                self.set_loading(False)

        self.set_loading(True)
        threading.Thread(target=work, daemon=True).start()

    def search_city(self):
        from tkinter import messagebox
        q = self.search_var.get().strip()
        if not q:
            return
        def work():
            try:
                res = get_current_weather(q, self.provider)
                if not res:
                    messagebox.showinfo("Result", "City not found.")
                    return
                messagebox.showinfo(
                    "Result",
                    f"{res['city']}, {res.get('country','')}: "
                    f"{res.get('condition')} • {res.get('temperature_c')}°C • "
                    f"humidity {res.get('humidity_percent')}%"
                )
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                self.set_loading(False)
        self.set_loading(True)
        threading.Thread(target=work, daemon=True).start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoketest", action="store_true")
    args = parser.parse_args()

    if args.smoketest:
        provider = OpenWeatherMapProvider()
        from weatherlib.stats import random_cities, fetch_cities_weather, summarize_cities
        from weatherlib.cities import DEFAULT_CITIES
        items = fetch_cities_weather(random_cities(DEFAULT_CITIES, 5), provider)
        s = summarize_cities(items)
        print("Smoketest OK. Items:")
        for it in items:
            print(f"- {it['city']}: {it.get('condition')}, {it.get('temperature_c')}°C")
        if s.get('avg_temp_c') is not None:
            print(f"Average: {s['avg_temp_c']:.1f}°C")
        sys.exit(0)

    try:
        App().root.mainloop()
    except Exception as e:
        print("Tkinter GUI could not start:", e)

