#!/usr/bin/env bash
set -e

# 1) Recolecta estáticos para WhiteNoise
python manage.py collectstatic --noinput

# 2) Aplica migraciones
python manage.py migrate --noinput

python manage.py loaddata superuser.json

# 3) Arranca gunicorn escuchando en $PORT (Render lo inyecta)
exec gunicorn SmartForm.wsgi:application --bind 0.0.0.0:$PORT
