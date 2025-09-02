Таск 4 – Django Web (без персистентност на метео данни)

Инсталация
- Python 3.10+
- От корена на репото:
  - Създайте venv: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\\.venv\\Scripts\\Activate.ps1`)
  - Инсталирайте зависимости: `pip install -r requirements.txt`
  - Настройте `.env`:
    - Копирайте `env.example` (или `.env.example`) на `.env` и попълнете `OPENWEATHERMAP_API_KEY=...`,
      или създайте `.env` с един ред: `OPENWEATHERMAP_API_KEY=...`

Стартиране
- Инициализирайте системните таблици: `python tasks/task4_django/manage.py migrate`
  - Този таск не записва метео данни; създават се само стандартните таблици на Django.
- Стартирайте сървъра: `python tasks/task4_django/manage.py runserver 5003`
- Отворете: http://127.0.0.1:5003
