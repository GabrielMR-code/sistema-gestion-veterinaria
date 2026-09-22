from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter

from .views import (
    PropietarioViewSet,
    MascotaViewSet,
    ConsultaVeterinariaViewSet,
    perfil,
    estadisticas,
    contador
)


def inicio(request):
    return JsonResponse({"mensaje": "API de Gestión Veterinaria activa"})


router = DefaultRouter()
router.register(r"propietarios", PropietarioViewSet)
router.register(r"mascotas", MascotaViewSet)
router.register(r"consultas", ConsultaVeterinariaViewSet)


urlpatterns = [
    path("", inicio),
    path("api/", include(router.urls)),
    path("api/perfil/", perfil),
    path("api/estadisticas/", estadisticas),
    path("api/contador/", contador),
]