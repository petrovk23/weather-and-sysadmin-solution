Weather And SysAdmin Solution

Overview
- Implements the Weather tasks in five separate folders (as requested) and the SysAdmin network design.
- Uses OpenWeatherMap (Current Weather API v2.5 + Geocoding v1.0).

Setup
- Requirements: Python 3.10+
- From this folder:
  - Create venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Install dependencies: `pip install -r requirements.txt`
  - Create environment file:
    - Either copy `env.example` (or `.env.example`) to `.env`,
      or create a new `.env` with one line: `OPENWEATHERMAP_API_KEY=...`

Run (per task)
- Task 1 (CLI): `python tasks/task1_cli/weather_cli.py`
- Task 2 (Tk GUI): `python tasks/task2_tk/app.py` (headless: `--smoketest`)
- Task 3 (Flask): `FLASK_APP=tasks/task3_flask/app.py flask run -p 5001`
- Task 4 (Django, no DB persistence):
  - `python tasks/task4_django/manage.py migrate`  (sets up Django’s built‑in tables; Task 4 doesn’t store weather data)
  - `python tasks/task4_django/manage.py runserver 5003`
- Task 5 (Django + DB, compare last 10):
  - `python tasks/task5_django_db/manage.py migrate`  (creates `tasks/task5_django_db/db.sqlite3`)
  - `python tasks/task5_django_db/manage.py runserver 5005`

Folders
- `tasks/task1_cli/`
- `tasks/task2_tk/`
- `tasks/task3_flask/`
- `tasks/task4_django/`
- `tasks/task5_django_db/`
- `sysadmin_task/`: network segmentation solution (Bulgarian)
