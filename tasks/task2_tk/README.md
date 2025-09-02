Таск 2 – Tkinter GUI (OpenWeatherMap)

Инсталация
- Python 3.10+
- От корена на репото:
  - Създайте venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Инсталирайте зависимости: `pip install -r requirements.txt`
  - Настройте `.env`:
    - Копирайте `env.example` (или `.env.example`) на `.env` и попълнете `OPENWEATHERMAP_API_KEY=...`,
      или създайте `.env` с един ред: `OPENWEATHERMAP_API_KEY=...`

Стартиране
- Графичен интерфейс: `python tasks/task2_tk/app.py`
- Headless проверка: `python tasks/task2_tk/app.py --smoketest`
