from rest_framework import serializers
from .models import Propietario, Mascota, ConsultaVeterinaria


class PropietarioSerializer(serializers.ModelSerializer):

    def validate_identificacion(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "La identificación es obligatoria."
            )
        return value

    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "El nombre es obligatorio."
            )
        return value

    class Meta:
        model = Propietario
        fields = "__all__"


class MascotaSerializer(serializers.ModelSerializer):

    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "El nombre de la mascota es obligatorio."
            )
        return value

    def validate_peso(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "El peso debe ser mayor que 0."
            )
        return value

    class Meta:
        model = Mascota
        fields = "__all__"


class ConsultaVeterinariaSerializer(serializers.ModelSerializer):

    def validate_motivo(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "El motivo es obligatorio."
            )
        return value

    def validate_costo(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "El costo no puede ser negativo."
            )
        return value

    class Meta:
        model = ConsultaVeterinaria
        fields = "__all__"