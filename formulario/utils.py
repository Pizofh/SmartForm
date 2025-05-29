from docx import Document
from django.conf import settings
import os
from .models import DocumentoGenerado

def generar_documentos(recluta):
    carpeta = os.path.join(settings.MEDIA_ROOT, "documentos", str(recluta.numero_documento))
    os.makedirs(carpeta, exist_ok=True)


    contexto = {
        "nombres": recluta.primer_nombre,
        # …
    }

