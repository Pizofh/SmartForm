from docx import Document
from django.conf import settings
import os
from .models import DocumentoGenerado

def generar_documentos(PersonalData):
    carpeta = os.path.join(settings.MEDIA_ROOT, "documentos", str(PersonalData.numero_documento))
    os.makedirs(carpeta, exist_ok=True)


    contexto = {
        "nombres": PersonalData.primer_nombre,
        # …
    }

