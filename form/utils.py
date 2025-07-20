from docx import Document
from django.conf import settings
import os
from .models import DocumentoGenerado

def generar_documentos(PersonalData):
    carpeta = os.path.join(settings.MEDIA_ROOT, "documentos", str(PersonalData.document_number))
    os.makedirs(carpeta, exist_ok=True)


    contexto = {
        "names": PersonalData.first_name,
        # …
    }

