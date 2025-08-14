#!/usr/bin/env bash
set -e

# Estáticos y migraciones (orden importante)
python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Crea el superusuario si no existe (no falla si ya existe)
python manage.py createsuperuser \
  --noinput \
  --username "${DJANGO_SUPERUSER_USERNAME}" \
  --email "${DJANGO_SUPERUSER_EMAIL}" || true

# Asegura permisos y contraseña siempre (tanto si existía como si se acaba de crear)
python manage.py shell -c "
from django.contrib.auth import get_user_model
U = get_user_model()
u, _ = U.objects.get_or_create(username='${DJANGO_SUPERUSER_USERNAME}', defaults={'email': '${DJANGO_SUPERUSER_EMAIL}'})
u.is_active = True
u.is_staff = True
u.is_superuser = True
u.set_password('${DJANGO_SUPERUSER_PASSWORD}')
if not u.email: u.email = '${DJANGO_SUPERUSER_EMAIL}'
u.save()
print('[admin-init] Superuser listo:', u.username)
"

# Arranca la app
exec gunicorn SmartForm.wsgi:application --bind 0.0.0.0:$PORT
