Таск 3 – Flask Web (OpenWeatherMap)

Инсталация
- Python 3.10+
- От корена на репото:
  - Създайте venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Инсталирайте зависимости: `pip install -r requirements.txt`
  - Настройте `.env`:
    - Копирайте `env.example` (или `.env.example`) на `.env` и попълнете `OPENWEATHERMAP_API_KEY=...`,
      или създайте `.env` с един ред: `OPENWEATHERMAP_API_KEY=...`

Стартиране
- Стартирайте: `FLASK_APP=tasks/task3_flask/app.py flask run -p 5001`
- Отворете: http://127.0.0.1:5001
