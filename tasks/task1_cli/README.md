Task 1 – CLI (OpenWeatherMap)

Setup
- Python 3.10+
- From the repository root:
  - Create venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Install deps: `pip install -r requirements.txt`
  - Create `.env`:
    - Copy `env.example` (or `.env.example`) to `.env`, then set `OPENWEATHERMAP_API_KEY=...`
    - Or create `.env` manually with one line: `OPENWEATHERMAP_API_KEY=...`

Run
- `python tasks/task1_cli/weather_cli.py`
