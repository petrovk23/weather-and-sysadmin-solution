Task 2 – Tkinter GUI (OpenWeatherMap)

Setup
- Python 3.10+
- From the repository root:
  - Create venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Install deps: `pip install -r requirements.txt`
  - Create `.env`:
    - Copy `env.example` (or `.env.example`) to `.env`, then set `OPENWEATHERMAP_API_KEY=...`
    - Or create `.env` manually with one line: `OPENWEATHERMAP_API_KEY=...`

Run
- Launch GUI: `python tasks/task2_tk/app.py`
- Headless verification: `python tasks/task2_tk/app.py --smoketest`
