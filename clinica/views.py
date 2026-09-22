from rest_framework import viewsets
from .models import Propietario, Mascota, ConsultaVeterinaria
from .serializers import (
    PropietarioSerializer,
    MascotaSerializer,
    ConsultaVeterinariaSerializer
)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    def get_queryset(self):
        queryset = Mascota.objects.all()

        especie = self.request.query_params.get("especie")
        activas = self.request.query_params.get("activas")
        propietario = self.request.query_params.get("propietario")

        if especie:
            queryset = queryset.filter(especie__iexact=especie)

        if activas:
            queryset = queryset.filter(activo=activas.lower() == "true")

        if propietario:
            queryset = queryset.filter(propietario_id=propietario)

        return queryset


class ConsultaVeterinariaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaVeterinaria.objects.all()
    serializer_class = ConsultaVeterinariaSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def perfil(request):
    return Response({
        "usuario": request.user.username,
        "email": request.user.email,
        "mensaje": "Perfil autenticado correctamente"
    })


@api_view(["GET"])
@permission_classes([IsAdminUser])
def estadisticas(request):
    return Response({
        "propietarios": Propietario.objects.count(),
        "mascotas": Mascota.objects.count(),
        "consultas": ConsultaVeterinaria.objects.count(),
    })


@api_view(["GET"])
def contador(request):
    visitas = request.session.get("visitas", 0)
    visitas += 1
    request.session["visitas"] = visitas

    return Response({
        "visitas": visitas
    })