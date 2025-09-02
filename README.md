Weather & SysAdmin – Решение

Общ преглед
- Пет отделни папки за всеки таск (както е изискано) + отделна папка със SysAdmin решение.
- Ползва се OpenWeatherMap (Current Weather API v2.5 + Geocoding v1.0) като единствен доставчик.

Инсталация (от корена на репото)
- Изисквания: Python 3.10+
- Създаване на виртуална среда:
  - Linux/macOS: `python -m venv .venv && source .venv/bin/activate`
  - Windows PowerShell: `py -m venv .venv` и после `.\\.venv\\Scripts\\Activate.ps1`
- Инсталиране на зависимости: `pip install -r requirements.txt`
- Настройка на ключ за време:
  - Копирайте `env.example` (или `.env.example`) на `.env` и попълнете `OPENWEATHERMAP_API_KEY=...`,
    или създайте `.env` с един ред: `OPENWEATHERMAP_API_KEY=...`

Стартиране по таскове
- Таск 1 (CLI): `python tasks/task1_cli/weather_cli.py`
- Таск 2 (Tk GUI): `python tasks/task2_tk/app.py` (в headless среда може `--smoketest`)
- Таск 3 (Flask): `FLASK_APP=tasks/task3_flask/app.py flask run -p 5001`
- Таск 4 (Django, без персистентност на данни):
  - `python tasks/task4_django/manage.py migrate` (инициализира системните таблици на Django)
  - `python tasks/task4_django/manage.py runserver 5003`
- Таск 5 (Django + БД, сравнение на последните 10):
  - `python tasks/task5_django_db/manage.py migrate` (създава `tasks/task5_django_db/db.sqlite3`)
  - `python tasks/task5_django_db/manage.py runserver 5005`

Структура
- `tasks/task1_cli/`
- `tasks/task2_tk/`
- `tasks/task3_flask/`
- `tasks/task4_django/`
- `tasks/task5_django_db/`
- `sysadmin_task/` – решение за сегментация на мрежи (на български)
