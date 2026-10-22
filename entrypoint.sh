#!/usr/bin/env bash
set -euo pipefail

# Run application startup steps with the runtime environment supplied by the
# platform / Compose. Never create, elevate, or reset administrator accounts
# automatically: use 'python manage.py createsuperuser' deliberately instead.
python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Render supplies PORT; local Compose uses 8000 when it is not configured.
exec gunicorn SmartForm.wsgi:application --bind "0.0.0.0:${PORT:-8000}"
