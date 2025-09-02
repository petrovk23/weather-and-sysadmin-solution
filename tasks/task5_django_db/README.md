Таск 5 – Django с БД (Снимки + Сравнение)

Инсталация
- Python 3.10+
- От корена на репото:
  - Създайте venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Инсталирайте зависимости: `pip install -r requirements.txt`
  - Настройте `.env`:
    - Копирайте `env.example` (или `.env.example`) на `.env` и попълнете `OPENWEATHERMAP_API_KEY=...`,
      или създайте `.env` с един ред: `OPENWEATHERMAP_API_KEY=...`

Стартиране
- Инициализирайте схемата: `python tasks/task5_django_db/manage.py migrate`
  - Това създава SQLite файла `tasks/task5_django_db/db.sqlite3`.
- Стартирайте сървъра: `python tasks/task5_django_db/manage.py runserver 5005`
- Отворете: http://127.0.0.1:5005

Функционалности
- Refresh: записва 5 случайни града (Snapshot + WeatherRecord записи)
- Search: заявка по град без запис в БД
- Compare: последните 10 стойности за град с прости графики
