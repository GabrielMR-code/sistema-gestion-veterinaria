from django.test import TestCase
from .models import Propietario, Mascota, ConsultaVeterinaria
from rest_framework.test import APIClient


class ClinicaTests(TestCase):

    def setUp(self):
        self.propietario = Propietario.objects.create(
            identificacion="999999999",
            nombre="Usuario Prueba",
            telefono="8888-9999",
            email="prueba@example.com"
        )

        self.mascota = Mascota.objects.create(
            nombre="Firulais",
            especie="Perro",
            raza="Mestizo",
            fecha_nacimiento="2020-01-01",
            peso=12.5,
            activo=True,
            propietario=self.propietario
        )

    def test_crear_propietario(self):
        self.assertEqual(Propietario.objects.count(), 1)

    def test_crear_mascota(self):
        self.assertEqual(self.mascota.nombre, "Firulais")

    def test_mascota_pertenece_a_propietario(self):
        self.assertEqual(self.mascota.propietario, self.propietario)

    def test_api_mascotas(self):
        client = APIClient()
        response = client.get("/clinica/api/mascotas/")
        self.assertEqual(response.status_code, 200)