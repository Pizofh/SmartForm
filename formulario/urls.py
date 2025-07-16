from django.urls import path, include
from django.views.generic import TemplateView
from .views import PersonalDataTabsView


# 🔽 IMPORTANTE: importa el router y tus ViewSets
from rest_framework.routers import DefaultRouter
from . import api_views

# 🔽 Registra tus ViewSets
router = DefaultRouter()
router.register(r'PersonalData', api_views.PersonalDataViewSet)

router.register(r'FamilyData', api_views.FamilyDataViewSet)
router.register(r'Child', api_views.ChildViewSet)
router.register(r'Sibling', api_views.SiblingViewSet)
router.register(r'academica', api_views.InformacionAcademicaViewSet)
router.register(r'bienes', api_views.BienesRentasAEPViewSet)
router.register(r'situacion', api_views.SituacionJuridicaViewSet)


urlpatterns = [
    path("", PersonalDataTabsView.as_view(), name="formulario_tabs"),
    path("exito/", TemplateView.as_view(template_name="formulario/exito.html"),
         name="formulario_exito"),

    # 🔽 Aquí incluyes tus rutas de API
    path("api/", include(router.urls)),
]
