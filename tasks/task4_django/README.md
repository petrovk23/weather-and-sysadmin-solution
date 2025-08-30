Task 4 – Django Web (no DB persistence)

Setup
- Python 3.10+
- From the repository root:
  - Create venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Install deps: `pip install -r requirements.txt`
  - Create `.env`:
    - Copy `env.example` (or `.env.example`) to `.env`, then set `OPENWEATHERMAP_API_KEY=...`
    - Or create `.env` manually with one line: `OPENWEATHERMAP_API_KEY=...`

Run
- Initialize Django system tables: `python tasks/task4_django/manage.py migrate`
  - This sets up Django’s built-in tables; Task 4 itself does not store weather data.
- Start server: `python tasks/task4_django/manage.py runserver 5003`
- Open: http://127.0.0.1:5003
