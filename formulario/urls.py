from django.urls import path, include
from django.views.generic import TemplateView
from .views import ReclutaTabsView

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
