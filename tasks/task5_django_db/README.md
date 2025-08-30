Task 5 – Django With DB (Snapshots + Compare)

Setup
- Python 3.10+
- From the repository root:
  - Create venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Install deps: `pip install -r requirements.txt`
  - Create `.env`:
    - Copy `env.example` (or `.env.example`) to `.env`, then set `OPENWEATHERMAP_API_KEY=...`
    - Or create `.env` manually with one line: `OPENWEATHERMAP_API_KEY=...`

Run
- Initialize DB schema: `python tasks/task5_django_db/manage.py migrate`
  - This creates the SQLite database file at `tasks/task5_django_db/db.sqlite3`.
- Start server: `python tasks/task5_django_db/manage.py runserver 5005`
- Open: http://127.0.0.1:5005

Features
- Refresh: stores 5 random city readings (Snapshot + WeatherRecord rows)
- Search: on-demand query without persisting
- Compare: last 10 values for a city with simple charts
