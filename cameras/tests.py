from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Camera, Ticket

class CameraTests(APITestCase):

    # Prueba 1: Crear una cámara y validar que se guarde correctamente
    def test_crear_camara_con_estado_valido(self):
        """Verifica que una cámara se cree correctamente con sus campos base"""
        camara = Camera.objects.create(
            id_camera="CAM-TEST-99",
            modelo="Modelo Pro 2026",
            ubicacion="Centro de Bogotá",
            latitud=4.6097,
            longitud=-74.0817,
            estado="Activa",
            localidad="Bogotá"
        )
        self.assertEqual(camara.id_camera, "CAM-TEST-99")
        self.assertEqual(camara.estado, "Activa")

    # Prueba 2: Verificar que el endpoint de cámaras responde con 200 OK
    def test_get_cameras_list_status_code(self):
        """Verifica que el endpoint de cámaras responda exitosamente (200 OK)"""
        url = reverse('camera-list') # Revisa que el nombre coincida con el router de Django REST
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Prueba 3: Validar la relación entre un ticket y su cámara
    def test_ticket_asociado_a_camara(self):
        """Verifica que un ticket se asocie correctamente a una cámara existente"""
        # Creamos una cámara de prueba
        camara = Camera.objects.create(
            id_camera="CAM-REF-01",
            modelo="Fix-Focus",
            ubicacion="Norte de Bogotá",
            latitud=4.6500,
            longitud=-74.0667,
            estado="Inactiva",
            localidad="Usaquén"
        )
        
        # Creamos un ticket que se vincula a esa cámara
        ticket = Ticket.objects.create(
            id_ticket="TCK-REF-01",
            camera=camara,
            tipo="Correctivo",
            prioridad="Alta",
            descripcion="Fallo total de alimentación"
        )
        
        self.assertEqual(ticket.camera.id_camera, "CAM-REF-01")
        self.assertTrue(Ticket.objects.filter(camera=camara).exists())