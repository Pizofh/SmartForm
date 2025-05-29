from django.urls import path
from django.views.generic import TemplateView
from .views import ReclutaTabsView

urlpatterns = [
    path("", ReclutaTabsView.as_view(), name="formulario_tabs"),
    path("exito/", TemplateView.as_view(template_name="formulario/exito.html"),
         name="formulario_exito"),
]
