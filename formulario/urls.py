from django.urls import path, include
from django.views.generic import TemplateView
from .views import ReclutaTabsView

"""
urls.py

Este módulo define las rutas URL del formulario inteligente de reclutamiento. 

Contiene tanto rutas de vistas basadas en clases para la interfaz de usuario, 
como rutas para la API RESTful expuesta por medio de Django REST Framework (DRF).

Rutas definidas:

- Vista principal del formulario (ReclutaTabsView), accesible desde la raíz del módulo.
- Vista de éxito (`formulario_exito`) mostrada luego del envío exitoso del formulario.
- Rutas de API (`/api/`) registradas mediante un `DefaultRouter` de DRF, que expone los siguientes ViewSets:

    - reclutas/: CRUD para la entidad principal `Recluta`.
    - direcciones/: Datos de direcciones anteriores del recluta.
    - datosfamiliares/: Información familiar, incluyendo hijos y hermanos.
    - hijos/: Detalles individuales de cada hijo.
    - hermanos/: Detalles individuales de cada hermano.
    - academica/: Información académica del recluta.
    - referencias/: Referencias personales.
    - defensa/: Contactos en el sector defensa.
    - bienes/: Bienes y rentas declaradas.
    - situacion/: Situación jurídica del aspirante.
    - otros/: Otros datos como viajes y recomendantes.

Estas rutas permiten tanto la visualización como la gestión programática (via API) de toda la información capturada durante el proceso de reclutamiento.
"""

# 🔽 IMPORTANTE: importa el router y tus ViewSets
from rest_framework.routers import DefaultRouter
from . import api_views

# 🔽 Registra tus ViewSets
router = DefaultRouter()
router.register(r'reclutas', api_views.ReclutaViewSet)
router.register(r'direcciones', api_views.DireccionesAnterioresViewSet)
router.register(r'datosfamiliares', api_views.DatosFamiliaresViewSet)
router.register(r'hijos', api_views.HijoViewSet)
router.register(r'hermanos', api_views.HermanoViewSet)
router.register(r'academica', api_views.InformacionAcademicaViewSet)
router.register(r'referencias', api_views.ReferenciasPersonalesViewSet)
router.register(r'defensa', api_views.SectorDefensaViewSet)
router.register(r'bienes', api_views.BienesRentasAEPViewSet)
router.register(r'situacion', api_views.SituacionJuridicaViewSet)
router.register(r'otros', api_views.OtrosDatosViewSet)

urlpatterns = [
    path("", ReclutaTabsView.as_view(), name="formulario_tabs"),
    path("exito/", TemplateView.as_view(template_name="formulario/exito.html"),
         name="formulario_exito"),

    # 🔽 Aquí incluyes tus rutas de API
    path("api/", include(router.urls)),
]
