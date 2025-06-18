# FormularioInteligenteIndumil

Formulario web inteligente desarrollado para INDUMIL, orientado a la recolección eficiente de datos de reclutamiento. Incluye validaciones avanzadas, secciones dinámicas por pestañas, carga de archivos y generación automática de documentos.

## 🛠️ Tecnologías utilizadas

- Python 3
- Django
- Bootstrap 5
- crispy-forms
- django-recaptcha
- htmx
- SQLite (modo local)

## 🚀 Funcionalidades

- Formulario en pestañas para recolectar:
  - Datos personales, identidad, contacto, familiares, educación, experiencia, economía.
- Validación con reCAPTCHA.
- Subida de archivos (hojas de vida, certificados).
- Generación de documentos `.docx`.
- Seguridad básica integrada.

## ⚙️ Instalación local

1. Clona el repositorio:

git clone https://github.com/tuusuario/FormularioInteligenteIndumil.git
cd FormularioInteligenteIndumil
Crea un entorno virtual e instálalo:

2. Crea un entorno virtual e instálalo:

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

3.  Configura el archivo .env si es necesario (por ejemplo para la clave de reCAPTCHA).

4.  Aplica migraciones:

python manage.py migrate

5. Ejecuta el servidor:

python manage.py runserver
Accede desde el navegador en http://localhost:8000


📝 Notas
Si estás en entorno de pruebas o desarrollo, el CAPTCHA se puede desactivar con un flag en la configuración.
Los archivos se almacenan en la carpeta ../media.


## 📄 Licencia

Este proyecto es propiedad de INDUMIL. Su uso externo requiere autorización expresa.

